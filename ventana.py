import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QFileDialog

import numpy as np

class Ui_ventana(QMainWindow, object):
    datoRetornado = QtCore.pyqtSignal(np.ndarray)
    
    def setupUi(self, MainWindow, esquina1, esquina2):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
        MainWindow.resize(370, 271)
        self.esquina1 = esquina1
        self.esquina2 = esquina2
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -7, 371, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: #75c58e;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 371, 41))
        self.frame_3.setStyleSheet("background-color: #2a8b8b;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(292, 7, 41, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#75c58e;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/mini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(332, 7, 41, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#ff356f;\n"
"}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(90, 130, 91, 21))
        self.label.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 180, 81, 41))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    border-radius: 10px;\n"
"    background-color: #3b5540;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #bfff91;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(190, 120, 81, 41))
        self.textEdit.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";"
"border-radius: 10px;\n")
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.frame_2)
        
        self.pushButton.clicked.connect(MainWindow.showMinimized)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.ok)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cantidad:"))
        self.pushButton_3.setText(_translate("MainWindow", "OK"))
    
    def ok(self):
        print("PResionado")
        self.generaPuntos(int(self.textEdit.toPlainText()))
        
    def generaPuntos(self, n):
        na = int(n/2)
        nb = n - na
        xs = np.random.randint(self.esquina1[0], self.esquina2[0], na)
        ys = np.random.randint(self.esquina1[1], self.esquina2[1], na)
        a = np.column_stack((xs, ys, np.full(na, -1)))
        xs = np.random.randint(self.esquina1[0], self.esquina2[0], nb)
        ys = np.random.randint(self.esquina1[1], self.esquina2[1], nb)
        b = np.column_stack((xs, ys, np.full(nb, 1)))

        all_points = np.concatenate((a, b), axis=0)
        np.random.shuffle(all_points)
        
        # Guardar el arreglo en un archivo de texto
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
        if file_path:
            np.savetxt(file_path, all_points, fmt="%d", delimiter=",")
        self.datoRetornado.emit(all_points)

#Clase que ayuda a mover la ventana
class MainWindow(Ui_ventana):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
            