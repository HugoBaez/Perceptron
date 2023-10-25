import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import datetime

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from ventana import Ui_ventana
from PyQt5.QtCore import QEventLoop, QTimer
import matplotlib.patches as patches

class Ui_MainWindow(QMainWindow, object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1392, 801)
        MainWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
        self.graf = Grafica()
        self.percep = Perceptron()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.f_superior = QtWidgets.QFrame(self.frame_3)
        self.f_superior.setGeometry(QtCore.QRect(0, -10, 1391, 50))
        self.f_superior.setMinimumSize(QtCore.QSize(0, 50))
        self.f_superior.setMaximumSize(QtCore.QSize(16777215, 50))
        self.f_superior.setStyleSheet("background-color: #2a8b8b;")
        self.f_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_superior.setObjectName("f_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.f_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.f_superior)
        self.label.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"padding: 10px 10px 0px 10px;\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(1102, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_min = QtWidgets.QPushButton(self.f_superior)
        self.bt_min.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_min.setMaximumSize(QtCore.QSize(50, 50))
        self.bt_min.setStyleSheet("QPushButton {\n"
"    padding-top: 20px;\n"
"    border: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#75c58e;\n"
"}")
        self.bt_min.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/mini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_min.setIcon(icon)
        self.bt_min.setIconSize(QtCore.QSize(40, 40))
        self.bt_min.setObjectName("bt_min")
        self.horizontalLayout.addWidget(self.bt_min, 0, QtCore.Qt.AlignBottom)
        self.bt_x = QtWidgets.QPushButton(self.f_superior)
        self.bt_x.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_x.setMaximumSize(QtCore.QSize(40, 40))
        self.bt_x.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#ff356f;\n"
"}\n"
"")
        self.bt_x.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_x.setIcon(icon1)
        self.bt_x.setIconSize(QtCore.QSize(40, 40))
        self.bt_x.setObjectName("bt_x")
        self.horizontalLayout.addWidget(self.bt_x)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 40, 1391, 761))
        self.frame_2.setStyleSheet("background-color: #75c58e;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 311, 31))
        self.label_2.setStyleSheet("font: 14pt \"Roboto\";\n"
"color: #3b5540;\n"
"font-weight: bold;\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 101, 31))
        self.label_3.setStyleSheet("font: 14pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(60, 130, 31, 31))
        self.label_4.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 31, 31))
        self.label_5.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(160, 130, 31, 31))
        self.label_6.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(160, 180, 31, 31))
        self.label_7.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(100, 220, 31, 31))
        self.label_8.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.RA_x1 = QtWidgets.QTextEdit(self.frame_4)
        self.RA_x1.setGeometry(QtCore.QRect(90, 130, 61, 31))
        self.RA_x1.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.RA_x1.setObjectName("RA_x1")
        self.RA_x2 = QtWidgets.QTextEdit(self.frame_4)
        self.RA_x2.setGeometry(QtCore.QRect(90, 180, 61, 31))
        self.RA_x2.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.RA_x2.setObjectName("RA_x2")
        self.Na = QtWidgets.QTextEdit(self.frame_4)
        self.Na.setGeometry(QtCore.QRect(140, 220, 61, 31))
        self.Na.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.Na.setObjectName("Na")
        self.RA_y1 = QtWidgets.QTextEdit(self.frame_4)
        self.RA_y1.setGeometry(QtCore.QRect(190, 130, 61, 31))
        self.RA_y1.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.RA_y1.setObjectName("RA_y1")
        self.RA_y2 = QtWidgets.QTextEdit(self.frame_4)
        self.RA_y2.setGeometry(QtCore.QRect(190, 180, 61, 31))
        self.RA_y2.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.RA_y2.setObjectName("RA_y2")
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setGeometry(QtCore.QRect(280, 180, 31, 31))
        self.label_21.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.RB_y1 = QtWidgets.QTextEdit(self.frame_4)
        self.RB_y1.setGeometry(QtCore.QRect(410, 130, 61, 31))
        self.RB_y1.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.RB_y1.setObjectName("RB_y1")
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(380, 180, 31, 31))
        self.label_18.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.RB_x1 = QtWidgets.QTextEdit(self.frame_4)
        self.RB_x1.setGeometry(QtCore.QRect(310, 130, 61, 31))
        self.RB_x1.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.RB_x1.setObjectName("RB_x1")
        self.Nb = QtWidgets.QTextEdit(self.frame_4)
        self.Nb.setGeometry(QtCore.QRect(360, 220, 61, 31))
        self.Nb.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.Nb.setObjectName("Nb")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(380, 130, 31, 31))
        self.label_20.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.RB_x2 = QtWidgets.QTextEdit(self.frame_4)
        self.RB_x2.setGeometry(QtCore.QRect(310, 180, 61, 31))
        self.RB_x2.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.RB_x2.setObjectName("RB_x2")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(280, 130, 31, 31))
        self.label_16.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.RB_y2 = QtWidgets.QTextEdit(self.frame_4)
        self.RB_y2.setGeometry(QtCore.QRect(410, 180, 61, 31))
        self.RB_y2.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.RB_y2.setObjectName("RB_y2")
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setGeometry(QtCore.QRect(320, 220, 31, 31))
        self.label_19.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(330, 90, 101, 31))
        self.label_17.setStyleSheet("font: 14pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.GR_ok = QtWidgets.QPushButton(self.frame_4)
        self.GR_ok.setGeometry(QtCore.QRect(220, 270, 81, 41))
        self.GR_ok.setStyleSheet("QPushButton {\n"
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
        self.GR_ok.setObjectName("GR_ok")
        self.GR_ok.clicked.connect(self.obtener_reg)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(0, 350, 501, 131))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(100, 10, 311, 31))
        self.label_22.setStyleSheet("font: 14pt \"Roboto\";\n"
"color: #3b5540;\n"
"font-weight: bold;\n"
"")
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.BoxEntre = QtWidgets.QComboBox(self.frame_5)
        self.BoxEntre.setGeometry(QtCore.QRect(70, 60, 221, 31))
        self.BoxEntre.setStyleSheet("QComboBox {\n"
"    border: none;\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"    background: #3b5540;\n"
"}\n"
"\n"
"QComboBox::drop-down:checked {\n"
"    background-color: #bfff91; \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(\"arrow.png\");\n"
"    background: url(\"arrow.png\") no-repeat center center;\n"
"    width: 10px;\n"
"    border: none;\n"
"     background: #3b5540;\n"
"    background-size: contain;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"}\n"
"")
        self.BoxEntre.setObjectName("BoxEntre")
        self.BoxEntre.addItem("Pintar paso por paso")
        self.BoxEntre.addItem("Resultado inmediato")
        self.bt_entre = QtWidgets.QPushButton(self.frame_5)
        self.bt_entre.setGeometry(QtCore.QRect(310, 60, 101, 31))
        self.bt_entre.setStyleSheet("QPushButton {\n"
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
        self.bt_entre.setObjectName("bt_entre")
        self.BoxEntre.raise_()
        self.bt_entre.raise_()
        self.label_22.raise_()
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(0, 480, 501, 131))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setGeometry(QtCore.QRect(100, 10, 311, 31))
        self.label_23.setStyleSheet("font: 14pt \"Roboto\";\n"
"color: #3b5540;\n"
"font-weight: bold;\n"
"")
        self.label_23.setTextFormat(QtCore.Qt.AutoText)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.BoxReco = QtWidgets.QComboBox(self.frame_6)
        self.BoxReco.setGeometry(QtCore.QRect(70, 50, 221, 31))
        self.BoxReco.setStyleSheet("QComboBox {\n"
"    border: none;\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"    background: #3b5540;\n"
"}\n"
"\n"
"QComboBox::drop-down:checked {\n"
"    background-color: #bfff91; \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(\"arrow.png\");\n"
"    background: url(\"arrow.png\") no-repeat center center;\n"
"    width: 10px;\n"
"    border: none;\n"
"     background: #3b5540;\n"
"    background-size: contain;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"}\n"
"")
        self.BoxReco.setObjectName("BoxReco")
        self.BoxReco.addItem("Generar datos al azar")
        self.BoxReco.addItem("Cargar un archivo")
        self.bt_reco = QtWidgets.QPushButton(self.frame_6)
        self.bt_reco.setGeometry(QtCore.QRect(310, 50, 101, 31))
        self.bt_reco.setStyleSheet("QPushButton {\n"
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
        self.bt_reco.setObjectName("bt_reco")
        self.label_archivo = QtWidgets.QLabel(self.frame_6)
        self.label_archivo.setGeometry(QtCore.QRect(100, 90, 311, 31))
        self.label_archivo.setStyleSheet("font: 10pt \"Roboto\";\n"
"color: white;\n"
"")
        self.label_archivo.setTextFormat(QtCore.Qt.AutoText)
        self.label_archivo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_archivo.setObjectName("label_archivo")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(0, 610, 501, 151))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setGeometry(QtCore.QRect(30, 60, 251, 31))
        self.label_9.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setGeometry(QtCore.QRect(30, 100, 251, 31))
        self.label_10.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.peso2 = QtWidgets.QTextEdit(self.frame_7)
        self.peso2.setGeometry(QtCore.QRect(380, 60, 81, 31))
        self.peso2.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.peso2.setObjectName("peso2")
        self.CP_ok = QtWidgets.QPushButton(self.frame_7)
        self.CP_ok.setGeometry(QtCore.QRect(380, 100, 81, 31))
        self.CP_ok.setStyleSheet("QPushButton {\n"
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
        self.CP_ok.setObjectName("CP_ok")
        self.CP_ok.clicked.connect(self.enviaPesos)
        self.coefici = QtWidgets.QTextEdit(self.frame_7)
        self.coefici.setGeometry(QtCore.QRect(290, 100, 81, 31))
        self.coefici.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.coefici.setObjectName("coefici")
        self.peso1 = QtWidgets.QTextEdit(self.frame_7)
        self.peso1.setGeometry(QtCore.QRect(290, 60, 81, 31))
        self.peso1.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 10pt \"Roboto\";")
        self.peso1.setObjectName("peso1")
        self.label_25 = QtWidgets.QLabel(self.frame_7)
        self.label_25.setGeometry(QtCore.QRect(110, 10, 311, 31))
        self.label_25.setStyleSheet("font: 14pt \"Roboto\";\n"
"color: #3b5540;\n"
"font-weight: bold;\n"
"")
        self.label_25.setTextFormat(QtCore.Qt.AutoText)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setGeometry(QtCore.QRect(500, 680, 891, 81))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.porcentaje = QtWidgets.QLabel(self.frame_8)
        self.porcentaje.setGeometry(QtCore.QRect(300, 20, 311, 31))
        self.porcentaje.setStyleSheet("font: 14pt \"Roboto\";\n"
"color: #3b5540;\n"
"font-weight: bold;\n"
"")
        self.porcentaje.setTextFormat(QtCore.Qt.AutoText)
        self.porcentaje.setAlignment(QtCore.Qt.AlignCenter)
        self.porcentaje.setObjectName("porcentaje")
        self.bt_salir = QtWidgets.QPushButton(self.frame_8)
        self.bt_salir.setGeometry(QtCore.QRect(760, 30, 101, 31))
        self.bt_salir.setStyleSheet("QPushButton {\n"
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
        self.bt_salir.setObjectName("bt_salir")
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setGeometry(QtCore.QRect(500, 0, 891, 681))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_9)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 851, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.graf)
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Perceptrón"))
        self.label_2.setText(_translate("MainWindow", "Generación de regiones"))
        self.label_3.setText(_translate("MainWindow", "Región A"))
        self.label_4.setText(_translate("MainWindow", "X1"))
        self.label_5.setText(_translate("MainWindow", "X2"))
        self.label_6.setText(_translate("MainWindow", "Y1"))
        self.label_7.setText(_translate("MainWindow", "Y2"))
        self.label_8.setText(_translate("MainWindow", "Na"))
        self.RA_x1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.RA_x2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Na.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.RA_y1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.RA_y2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "X2"))
        self.RB_y1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "Y2"))
        self.RB_x1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Nb.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "Y1"))
        self.RB_x2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "X1"))
        self.RB_y2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "Nb"))
        self.label_17.setText(_translate("MainWindow", "Región B"))
        self.GR_ok.setText(_translate("MainWindow", "OK"))
        self.label_22.setText(_translate("MainWindow", "Entrenamiento"))
        self.bt_entre.setText(_translate("MainWindow", "Entrenar"))
        self.label_23.setText(_translate("MainWindow", "Reconocimiento"))
        self.BoxReco.setItemText(0, _translate("MainWindow", "Generar datos al azar"))
        self.BoxReco.setItemText(1, _translate("MainWindow", "Cargar un archivo"))
        self.bt_reco.setText(_translate("MainWindow", "Reconocer"))
        self.label_archivo.setText(_translate("MainWindow", "Prueba"))
        self.label_9.setText(_translate("MainWindow", "Intervalo: Pesos del neurón"))
        self.label_10.setText(_translate("MainWindow", "Coeficiente de aprendizaje"))
        self.peso2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CP_ok.setText(_translate("MainWindow", "OK"))
        self.coefici.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.peso1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "Cambio de parametros"))
        self.porcentaje.setText(_translate("MainWindow", "Porcentaje: ___ %"))
        self.bt_salir.setText(_translate("MainWindow", "Salir"))
        self.bt_min.clicked.connect(MainWindow.showMinimized)
        self.bt_x.clicked.connect(MainWindow.close)
        self.bt_salir.clicked.connect(MainWindow.close)
        self.bt_reco.clicked.connect(self.recono)
        self.bt_entre.clicked.connect(self.entrenamiento)
        
        self.bt_entre.setEnabled(False)
        self.bt_reco.setEnabled(False)
        self.CP_ok.setEnabled(False)
        self.BoxEntre.setEnabled(False)
        self.BoxReco.setEnabled(False)
        self.peso1.setEnabled(False)
        self.peso2.setEnabled(False)
        self.coefici.setEnabled(False)
        
        
    
    #Funcion conectada al boton GR_ok para graficar las regiones
    def obtener_reg(self):
        self.graf.grafica_regiones(int(self.Na.toPlainText()), int(self.RA_x1.toPlainText()), int(self.RA_y1.toPlainText()), int(self.RA_x2.toPlainText()), int(self.RA_y2.toPlainText()), int(self.Nb.toPlainText()), int(self.RB_x1.toPlainText()), int(self.RB_y1.toPlainText()), int(self.RB_x2.toPlainText()), int(self.RB_y2.toPlainText()))
        self.CP_ok.setEnabled(True)
        self.peso1.setEnabled(True)
        self.peso2.setEnabled(True)
        self.coefici.setEnabled(True)
        
    def enviaPesos(self):
            self.percep.setPesosCoefi(float(self.peso1.toPlainText()), float(self.peso2.toPlainText()), float(self.coefici.toPlainText()))
            print(f'Peso 1: {float(self.peso1.toPlainText())}, Peso 2: {float(self.peso2.toPlainText())}, Coefi: {float(self.coefici.toPlainText())}')
            self.BoxEntre.setEnabled(True)
            self.bt_entre.setEnabled(True)
            
    def entrenamiento(self):
            select = self.BoxEntre.currentText()
            if select == "Pintar paso por paso":
                self.percep.entrenamientoP(self.graf, self.porcentaje)
            else:
                self.percep.entrenamientoI(self.graf)
            self.porcentaje.setText(f"Porcentaje: {self.percep.porcentaje} %")
            self.BoxReco.setEnabled(True)
            self.bt_reco.setEnabled(True)
            
    def recono(self):
            select = self.BoxReco.currentText()
            if select == "Generar datos al azar":
                self.nueva_ventana = MainWindow()
                self.ui = Ui_ventana()
                self.ui.setupUi(self.nueva_ventana, (min(self.graf.x1a, self.graf.x1b), min(self.graf.y1a, self.graf.y1b)), (max(self.graf.x2a, self.graf.x2b), max(self.graf.y2a, self.graf.y2b)))
                self.nueva_ventana.show()
                self.ui.datoRetornado.connect(self.aleatorio)
            else:
                file_path, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
                if file_path:
                        points = np.loadtxt(file_path, delimiter=",")
                self.graf.graficaRecono(points)
                # Obtener las entradas y las etiquetas reales de los nuevos puntos
                '''
                conta = 0
                for puntos in points:
                        punto = puntos[:2]
                        S = puntos[-1] - self.percep.salida_real_neuron(punto)
                        if S != 0:
                                conta += 1
                '''
                entradas = points[:, :2]
                etiquetas_reales = points[:, -1]

                # Clasificar los nuevos puntos utilizando el perceptrón
                etiquetas_predichas = np.array([self.percep.salida_real_neuron(punto) for punto in entradas])

                # Calcular el porcentaje de aciertos excluyendo los puntos fuera de las regiones
                aciertos = 0
                total = 0
                for i, etiqueta_predicha in enumerate(etiquetas_predichas):
                        if etiquetas_reales[i] == -1 and etiqueta_predicha == -1 and self.graf.x1a <= entradas[i, 0] <= self.graf.x2a and self.graf.y1a <= entradas[i, 1] <= self.graf.y2a:
                                aciertos += 1
                        elif etiquetas_reales[i] == 1 and etiqueta_predicha == 1 and self.graf.x1b <= entradas[i, 0] <= self.graf.x2b and self.graf.y1b <= entradas[i, 1] <= self.graf.y2b:
                                aciertos += 1
                        total += 1
                
                # Calcular el porcentaje de aciertos
                self.porcentaje.setText(f'Porcentaje: {round((aciertos / total) * 100, 1)} %')
                #self.porcentaje.setText(f'Porcentaje: {round(100 - (conta / len(points)) * 100, 1)} %')
                
                
    def aleatorio(self, points):
            self.nueva_ventana.close()
            self.graf.graficaRecono(points)
            '''
            conta = 0
            for puntos in points:
                punto = puntos[:2]
                S = puntos[-1] - self.percep.salida_real_neuron(punto)
                if S != 0:
                        conta += 1
            '''
            entradas = points[:, :2]
            etiquetas_reales = points[:, -1]

            # Clasificar los nuevos puntos utilizando el perceptrón
            etiquetas_predichas = np.array([self.percep.salida_real_neuron(punto) for punto in entradas])
            print(f'Etiquetas reales: \n {etiquetas_reales}')
            print(f'Etiquetas predichas: \n {etiquetas_predichas}')
            # Calcular el porcentaje de aciertos excluyendo los puntos fuera de las regiones
            aciertos = 0
            total = 0
            for i, etiqueta_predicha in enumerate(etiquetas_predichas):
                if etiquetas_reales[i] == -1 and etiqueta_predicha == -1 and self.graf.x1a <= entradas[i, 0] <= self.graf.x2a and self.graf.y1a <= entradas[i, 1] <= self.graf.y2a:
                        aciertos += 1
                elif etiquetas_reales[i] == 1 and etiqueta_predicha == 1 and self.graf.x1b <= entradas[i, 0] <= self.graf.x2b and self.graf.y1b <= entradas[i, 1] <= self.graf.y2b:
                        aciertos += 1
                total += 1

            # Calcular el porcentaje de aciertos
            self.porcentaje.setText(f'Porcentaje: {round((aciertos / total) * 100, 1)} %')
        
            #self.porcentaje.setText(f'Porcentaje: {round(100 - (conta / len(points)) * 100, 1)} %')
    
    
                

#Clase que ayuda a mover la ventana
class MainWindow(Ui_MainWindow):
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

#Clase grafica
class Grafica(FigureCanvas):
        #Se inicializa una grafica vacia
        def __init__(self, parent=None):     
                self.fig , self.ax = plt.subplots(1, dpi=100,
                sharey=True, facecolor='#75c58e')
                super().__init__(self.fig) 
                # Establecer límites de los ejes x e y
                self.ax.set_xlim(-40, 40)
                self.ax.set_ylim(-40, 40)

                # Dibujar gráfica vacía sin puntos
                self.ax.plot([], [])
                
                # Ajustar automáticamente los márgenes y espaciado
                self.fig.tight_layout()
        
        #Funcion que grafica las regiones
        def grafica_regiones(self, na, x1a, y1a, x2a, y2a, nb, x1b, y1b, x2b, y2b):
                self.x1a = x1a
                self.x2a = x2a
                self.y1a = y1a
                self.y2a = y2a
                
                self.x1b = x1b
                self.x2b = x2b
                self.y1b = y1b
                self.y2b = y2b
                self.ax.clear()  # Limpiar la gráfica actual
                xs = np.random.randint(x1a, x2a, na)
                ys = np.random.randint(y1a, y2a, na)
                self.a = np.column_stack((xs, ys, np.full(na, -1)))
                xs = np.random.randint(x1b, x2b, nb)
                ys = np.random.randint(y1b, y2b, nb)
                self.b = np.column_stack((xs, ys, np.full(nb, 1)))

                # Dibujar los puntos en la gráfica usando el objeto ax
                self.ax.scatter(self.a[:, 0], self.a[:, 1], color='red')
                self.ax.scatter(self.b[:, 0], self.b[:, 1], color='blue')
                
                self.ax.add_patch(patches.Rectangle((x1a, y1a), x2a - x1a, y2a - y1a, linewidth=1, edgecolor='red', facecolor='none'))
                self.ax.add_patch(patches.Rectangle((x1b, y1b), x2b - x1b, y2b - y1b, linewidth=1, edgecolor='blue', facecolor='none'))

                # Actualizar la gráfica en el lienzo
                self.draw()
                
                self.all_points = np.concatenate((self.a, self.b), axis=0)
                np.random.shuffle(self.all_points)
                # Obtener la fecha y hora actual
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y%m%d%H%M%S")

                # Crear la carpeta si no existe
                folder_name = timestamp
                if not os.path.exists(folder_name):
                        os.makedirs(folder_name)

                # Guardar las coordenadas en archivos de texto
                file_a = os.path.join(folder_name, "puntos.txt")
                np.savetxt(file_a, self.all_points, fmt='%d', delimiter=',')
        
        def graficaLinea(self, pesos, umbral):
                self.ax.clear()  # Limpiar la gráfica actual
                # Dibujar los puntos en la gráfica usando el objeto ax
                self.ax.scatter(self.a[:, 0], self.a[:, 1], color='red')
                self.ax.scatter(self.b[:, 0], self.b[:, 1], color='blue')
                self.ax.add_patch(patches.Rectangle((self.x1a, self.y1a), self.x2a - self.x1a, self.y2a - self.y1a, linewidth=1, edgecolor='red', facecolor='none'))
                self.ax.add_patch(patches.Rectangle((self.x1b, self.y1b), self.x2b - self.x1b, self.y2b - self.y1b, linewidth=1, edgecolor='blue', facecolor='none'))

                w1, w2 = pesos
                
                self.x = np.linspace(min(self.x1a, self.x1b), max(self.x2a, self.x2b), 100)
                self.y = (umbral - w1 * self.x) / w2
                self.ax.plot(self.x, self.y, color='green')
                self.draw()
        
        def graficaParcial(self, pesos, umbral, puntos):
                self.ax.clear()  # Limpiar la gráfica actual
                for p in puntos:
                        print(f'Puntos: {p}')
                        if p[-1] == -1:
                                self.ax.scatter(p[0], p[1], color='red')
                        else:
                                self.ax.scatter(p[0], p[1], color='blue')
                self.ax.add_patch(patches.Rectangle((self.x1a, self.y1a), self.x2a - self.x1a, self.y2a - self.y1a, linewidth=1, edgecolor='red', facecolor='none'))
                self.ax.add_patch(patches.Rectangle((self.x1b, self.y1b), self.x2b - self.x1b, self.y2b - self.y1b, linewidth=1, edgecolor='blue', facecolor='none'))
                w1, w2 = pesos
                self.x = np.linspace(min(self.x1a, self.x1b), max(self.x2a, self.x2b), 100)
                self.y = (umbral - w1 * self.x) / w2
                self.ax.plot(self.x, self.y, color='green')
                self.draw()
                loop = QEventLoop()
                QTimer.singleShot(1000, loop.quit)  # Retraso de 1 segundo (1000 ms)
                loop.exec_()
        
        def graficaRecono(self, puntos):
                self.ax.clear()  # Limpiar la gráfica actual
                self.ax.scatter(self.a[:, 0], self.a[:, 1], color='red')
                self.ax.scatter(self.b[:, 0], self.b[:, 1], color='blue')
                self.ax.add_patch(patches.Rectangle((self.x1a, self.y1a), self.x2a - self.x1a, self.y2a - self.y1a, linewidth=1, edgecolor='red', facecolor='none'))
                self.ax.add_patch(patches.Rectangle((self.x1b, self.y1b), self.x2b - self.x1b, self.y2b - self.y1b, linewidth=1, edgecolor='blue', facecolor='none'))
                self.ax.plot(self.x, self.y, color='green')
                
                for p in puntos:
                        if p[-1] == -1:
                                self.ax.scatter(p[0], p[1], color='orange')
                        else:
                                self.ax.scatter(p[0], p[1], color='violet')
                self.draw()
                
class Perceptron:
    def __init__(self):
        self.umbral = np.random.uniform(0, 0.25)

    def setPesosCoefi(self, rango1_pesos, rango2_pesos, coeficiente_aprendizaje):
        self.pesos = np.random.uniform(rango1_pesos, rango2_pesos, 2)
        self.coeficiente_aprendizaje = coeficiente_aprendizaje
        
    def salida_real_neuron(self, entrada):
        calculo = self.pesos.dot(entrada) - self.umbral
        if calculo >= 0:
            y = 1
        else:
            y = -1
        return y

    def entrenamientoI(self, graf):
        entradas =  graf.all_points.copy()
        conta = 0
        n = len(entradas)
        while len(entradas) > 0:
            for puntos in entradas:
                punto = puntos[:2]
                S = puntos[-1] - self.salida_real_neuron(punto)
                print(f'{punto},{puntos[-1]}')
                print(f'Resultado: {S}')
                if S != 0:
                    conta += 1
                    for i in range(len(self.pesos)):
                        delta = self.coeficiente_aprendizaje * S * punto[i]
                        self.pesos[i] += delta
                        print(f'Peso: {self.pesos[i]}')
                    self.umbral -= self.coeficiente_aprendizaje * S
                    print(f'Umbral: {self.umbral}')
                entradas = entradas[1:]
        self.porcentaje = round(100 - (conta / n) * 100, 1)
        graf.graficaLinea(self.pesos, self.umbral)

    def entrenamientoP(self, graf, porcen):
        entradas =  graf.all_points.copy()
        conta = 0
        pintar = []
        n = len(entradas)
        while len(entradas):
            for puntos in entradas:
                pintar.append(puntos)
                punto = puntos[:2]
                S = puntos[-1] - self.salida_real_neuron(punto)
                print(f'{punto},{puntos[-1]}')
                print(f'Resultado: {S}')
                if S != 0:
                    conta += 1
                    for i in range(len(self.pesos)):
                        delta = self.coeficiente_aprendizaje * S * punto[i]
                        self.pesos[i] += delta
                        print(f'Peso: {self.pesos[i]}')
                    self.umbral -= self.coeficiente_aprendizaje * S
                    print(f'Umbral: {self.umbral}')
                entradas = entradas[1:]
                self.porcentaje = round(100 - (conta / n) * 100, 1)
                porcen.setText(f"Porcentaje: {self.porcentaje} %")
                graf.graficaParcial(self.pesos, self.umbral, pintar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())