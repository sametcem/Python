import sys

from PyQt5 import QtWidgets,QtGui



def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("python.png"))

    etiket1.setText("This is a text.")
    etiket1.move(220,30)
    etiket2.move(70,100)

    pencere.setGeometry(100,100,500,500) #desltop location 0 0, 500 500 size.

    pencere.show()

    sys.exit(app.exec_())


Pencere()


