import configparser
import os
import sys
import shutil
from appdirs import user_config_dir, site_config_dir

from citramanik import __version__, __title__

CONFIG_NAME = "citramanik.conf"
CONFIG_DIR = user_config_dir(__title__)

if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

class CitramanikConfigs():
    """
    Citramanik Configurations
    """
    def __init__(self, output_dir="", quality=98, dpi=96, threads_config=4, inkscape_path=None, use_flatpak=False, ghostscript_path=None, pngquant_path=None):
        self.__output_dir = output_dir
        self.__quality = quality
        self.__dpi = dpi
        self.__threads_config = threads_config
        self.__inkscape_path = inkscape_path
        self.__ghostscript_path = ghostscript_path
        self.__pngquant_path = pngquant_path
        self.__use_flatpak = use_flatpak
        self.__version = __version__

    def __repr__(self):
        return "CitramanikConfigs: " + str({
            "version": self.__version,
            "outputdir": self.__output_dir,
            "quality": self.__quality,
            "dpi": self.__dpi,
            "threads": self.__threads_config,
            "inkscape_path": self.__inkscape_path,
            "inkscape_use_flatpak": self__use_flatpak,
            "ghostscript_path": self.__ghostscript_path,
            "pngquant_path": self.__pngquant_path})

    def get_current_version(self):
        """ Get application release version """

        return self.__version

    def get_output_dir(self):
        """ Last output directory for saving your exports """

        return self.__output_dir

    def set_output_dir(self, value=None):
        if not value:
            self.__output_dir = os.path.expanduser("~/")
        self.__output_dir = value

    def get_quality(self):
        """ Quality of Rasterized Images, valid for JPG, PDF, EPS.
        Default value is 96 """

        return self.__quality or 98

    def set_quality(self, value=96):
        if value < 1 or value > 100:
            raise ValueError("Quality out of range 1-100")
        self.__quality = value

    def get_dpi(self):
        """ Exports DPI. Default value is 96 """

        return self.__dpi or 96

    def set_dpi(self, value):
        if value < 1:
            raise ValueError("DPI cannot less than 1")
        self.__dpi = value

    def get_threads_config(self):
        """ Concurrent export process number. Default value is 4 """

        return self.__threads_config or 4

    def set_threads_config(self, value):
        self.__threads_config = value

    def get_inkscape_path(self):
        """ Inkscape Path used for exporting. Usually in /usr/bin/inkscape """

        return self.__inkscape_path or self.detect_inkscape() or ""

    def set_inkscape_path(self, location):
        self.__inkscape_path = location

    def is_use_flatpak(self):
        """ Inkscape Path used for exporting. Usually in /usr/bin/inkscape """

        return self.__use_flatpak

    def set_use_flatpak(self, status):
        self.__use_flatpak = status

    def get_ghostscript_path(self):
        """ Ghostscript Path used for exporting JPG, PDF, and EPS. Usually in /usr/bin/gs """

        return self.__ghostscript_path or self.detect_ghostscript() or ""

    def set_ghostscript_path(self, location):
        self.__ghostscript_path = location

    def get_pngquant_path(self):
        """ Pngquant Path used for optimizing PNG. Usually in /usr/bin/pngquant """

        return self.__pngquant_path or self.detect_pngquant() or ""

    def set_pngquant_path(self, location):
        self.__pngquant_path = location

    def detect_inkscape(self):
        """ Search for inkscape in system PATH.
        Return path of inkscape or None if not found.

        On Windows, it will check if there is inkscape in installation directory"""

        if sys.platform.startswith("win"):
            inkscapeDir = "inkscape/bin/inkscape.com"
            if os.path.exists(inkscapeDir):
                return inkscapeDir
            else:
                return shutil.which("inkscape")
        else:
            return shutil.which("inkscape")

    def detect_ghostscript(self):
        """ Search for ghostscript in system PATH.
        Return path of ghostscript or None if not found. """

        if sys.platform.startswith("win"):
            # in windows, we use 32-bit version of Ghostscript, even your system is 64-bit
            gsDir = "gs/gs9.53.3/bin/gswin32c.exe"
            if os.path.exists(gsDir):
                return gsDir
            else:
                return shutil.which("gswin32c")
        else:
            return shutil.which("gs")

    def detect_pngquant(self):
        """ Search for pngquant in system PATH.
        Return path of pngquant or None if not found. """

        if sys.platform.startswith("win"):
            pngquantDir = "pngquant/pngquant.exe"
            if os.path.exists(pngquantDir):
                return pngquantDir
            else:
                return shutil.which("pngquant")
        else:
            return shutil.which("pngquant")

    def write_to_file(self):
        """ Write Citramanik configurations to user config directory. """

        config = configparser.ConfigParser()
        config["Citramanik"] = { "Version": self.get_current_version() }

        config["Settings"] = {
            "InkscapePath"      : self.get_inkscape_path(),
            "InkscapeUseFlatpak": self.is_use_flatpak(),
            "GhostscriptPath"   : self.get_ghostscript_path(),
            "PngquantPath"      : self.get_pngquant_path(),
            "Threads"           : self.get_threads_config()
        }

        config["Exports"] = {
            "LastOutputDir" : self.get_output_dir(),
            "DPI"           : self.get_dpi(),
            "Quality"       : self.get_quality()
        }

        with open(os.path.join(CONFIG_DIR, CONFIG_NAME), "w") as f:
            config.write(f)

    def load_from_file(self):
        """ Load Citramanik configurations from user config directory """

        config = configparser.ConfigParser()
        res = config.read([os.path.join(CONFIG_DIR, CONFIG_NAME)])

        if not res:
            self.write_to_file()
            return self.load_from_file()

        try:
            self.set_threads_config(config.getint("Settings", "Threads"))
            self.set_inkscape_path(config.get("Settings", "InkscapePath"))
            self.set_use_flatpak(config.get("Settings", "InkscapeUseFlatpak"))
            self.set_ghostscript_path(config.get("Settings", "GhostscriptPath"))
            self.set_pngquant_path(config.get("Settings", "PngquantPath"))

            self.set_output_dir(config.get("Exports", "LastOutputDir"))
            self.set_dpi(config.getint("Exports", "DPI"))
            self.set_quality(config.getint("Exports", "Quality"))
        except:
            self.set_threads_config(self.get_threads_config())
            self.set_inkscape_path(self.get_inkscape_path())
            self.set_use_flatpak(False)
            self.set_ghostscript_path(self.get_ghostscript_path())
            self.set_pngquant_path(self.get_pngquant_path())

            self.set_output_dir("")
            self.set_dpi(self.get_dpi())
            self.set_quality(self.get_quality())

        if self.get_current_version() > config.get("Citramanik", "version"):
            self.write_to_file()

        return self
