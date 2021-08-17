import os
import sys

if sys.platform == "linux":
    os.environ["FONTCONFIG_FILE"] = "/etc/fonts/fonts.conf"
    os.environ["FONTCONFIG_PATH"] = "/etc/fonts/"
