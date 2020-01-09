import sys

from PyQt5 import QtWidgets

def Window():

    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()

    w.setWindowTitle("PyQt5 Ders 1")

    w.show()

    sys.exit(app.exec_())


Window()


