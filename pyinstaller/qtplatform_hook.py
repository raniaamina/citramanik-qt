import os
import sys

if sys.platform == "linux":
    os.environ["QT_QPA_PLATFORM"] = "xcb"
