import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Okey")
    cancel = QtWidgets.QPushButton("Cancel")

    h_box = QtWidgets.QHBoxLayout() # Yatay

    h_box.addStretch() # float:left
    h_box.addWidget(okay)
    #h_box.addStretch()  # center
    h_box.addWidget(cancel)
    #h_box.addStretch()  # float:right

    v_box = QtWidgets.QVBoxLayout() # Dikey

    v_box.addStretch()
    v_box.addLayout(h_box)



    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 4")

    pencere.setLayout(v_box) #put container box

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())


Pencere()


