from PyQt5.QtWidgets import QApplication
import sys
from mainWindow import GUI

if __name__ == '__main__':
    app=QApplication(sys.argv)
    runGui=GUI()
    runGui.showFullScreen()
    # runGui.show()
    sys.exit(app.exec_())