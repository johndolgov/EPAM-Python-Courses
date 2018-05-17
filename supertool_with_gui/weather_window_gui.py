import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from weather_gui import Ui_MainWindow

app = QtWidgets.QApplication([])

class MainApplication(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainApplication, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.show()

window = MainApplication()
window.show()

sys.exit(app.exec_())