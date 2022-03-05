
# use semantic versioning (major, minor, patch)
version_info = ( 1, 3, 1 )

__author__ =  "Devlovers ID"
__title__ = "citramanik-qt"
__version__ = ".".join(map(str, version_info))
__release_date__ = "2022-03-01"
__download_url__ = "https://getcitramanik.dev-is.my.id"
__website_url__ = "https://citramanik.dev-is.my.id"
__donate_url__ = "https://support.dev-is.my.id"

import os
# Directory of the current file
__current_directory__ = os.path.dirname(os.path.abspath(__file__))


def get_versions():
    """ return versions for later used in citramanik components """

    import sys
    import platform

    import PyQt5
    import PyQt5.QtCore

    if not sys.platform == 'darwin':
        system = platform.system()
    else:
        system = 'Darwin'

    return {
        "citramanik": __version__,
        "release_date": __release_date__,
        "pyqt_version": PyQt5.QtCore.PYQT_VERSION_STR,
        "qt_version": PyQt5.QtCore.QT_VERSION_STR,
        "system": system,
        "sysrelease": platform.release()
    }
