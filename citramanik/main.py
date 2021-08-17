import sys
from PyQt5 import QtWidgets

from citramanik.handler.gui import CitramanikWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = CitramanikWindow()
    main_window.show()
    main_window.updater.retrieve_latest_version()
    app.exec_()

if __name__ == "__main__":
    main()
