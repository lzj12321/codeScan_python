# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QInputDialog, QLineEdit,QLabel,QFrame
from PyQt5.QtGui import QIntValidator, QPixmap, QPainter, QPen, QLinearGradient
from YamlTool import Yaml_Tool
import numpy as np
from coordinate import Coordinate
import sys
from codeAndBoxState import CodeState,BoxState,InputDataState
from codeAndBoxCheck import CodeAndBoxCheck


class GUI(QWidget):

    def __init__(self):
        super(GUI, self).__init__()
        self.isCommonPackMode = True
        #choose =QMessageBox.question(self, 'Question', '工业电源装箱模式？', QMessageBox.Yes | QMessageBox.No,
        #                              QMessageBox.Yes)
        #if choose == QMessageBox.No:
         #   self.isCommonPackMode = True
       # else:
        #    self.isCommonPackMode = False
         #   self.packState={}

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 85, 255)")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 85, 255)")
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(200, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 85, 255)")
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(910, 640, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(164, 0, 0)")
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(910, 570, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(164, 0, 0)")
        self.label_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(910, 500, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(164, 0, 0)")
        self.label_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(50, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 159, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(910, 670, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color: rgb(255, 0, 0)")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(910, 600, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("color: rgb(255, 0, 0)")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setGeometry(QtCore.QRect(910, 530, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("color: rgb(255, 0, 0)")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(240, 10, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(92, 53, 102)")
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(910, 220, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 85, 255)")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_8 = QtWidgets.QLineEdit(self)
        self.lineEdit_8.setGeometry(QtCore.QRect(350, 120, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAutoFillBackground(False)
        self.lineEdit_8.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(250, 90, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(78, 154, 6)")
        self.label_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_11.setLineWidth(2)
        self.label_11.setMidLineWidth(2)
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(320, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 85, 255)")
        self.label_12.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(440, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 85, 255)")
        self.label_13.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(self)
        self.lineEdit_9.setGeometry(QtCore.QRect(360, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self)
        self.lineEdit_10.setGeometry(QtCore.QRect(480, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(750, 10, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(0, 85, 255)")
        self.label_14.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.lineEdit_11 = QtWidgets.QLineEdit(self)
        self.lineEdit_11.setGeometry(QtCore.QRect(640, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(550, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(0, 85, 255)")
        self.label_18.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.lineEdit_12 = QtWidgets.QLineEdit(self)
        self.lineEdit_12.setGeometry(QtCore.QRect(350, 90, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setAutoFillBackground(False)
        self.lineEdit_12.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(910, 290, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(0, 85, 255)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(910, 430, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 170, 0)")
        self.label_16.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.lineEdit_13 = QtWidgets.QLineEdit(self)
        self.lineEdit_13.setGeometry(QtCore.QRect(910, 390, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("color: rgb(0, 170, 0)")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self)
        self.lineEdit_14.setGeometry(QtCore.QRect(910, 460, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("color: rgb(0, 170, 0)")
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(910, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 170, 0)")
        self.label_17.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 5, 181, 100))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit_15 = QtWidgets.QLineEdit(self)
        self.lineEdit_15.setGeometry(QtCore.QRect(800, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(710, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 85, 255)")
        self.label_19.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.lineEdit_16 = QtWidgets.QLineEdit(self)
        self.lineEdit_16.setGeometry(QtCore.QRect(770, 120, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setAutoFillBackground(False)
        self.lineEdit_16.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_16.setText("")
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self)
        self.lineEdit_17.setGeometry(QtCore.QRect(950, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setAutoFillBackground(False)
        self.lineEdit_17.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self)
        self.lineEdit_18.setGeometry(QtCore.QRect(790, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setAutoFillBackground(False)
        self.lineEdit_18.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setGeometry(QtCore.QRect(700, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("color: rgb(0, 85, 255)")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self)
        self.checkBox_3.setGeometry(QtCore.QRect(860, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("color: rgb(0, 85, 255)")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self)
        self.checkBox_4.setGeometry(QtCore.QRect(700, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet("color: rgb(0, 85, 255)")
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 50, 51, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(170, 0, 255)")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(0, 200, 911, 521))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(100)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setMouseTracking(True)
        self.label_9.setStyleSheet("color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147))")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setLineWidth(3)
        self.label_9.setMidLineWidth(3)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(890, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 85, 255)")
        self.label_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(960, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(0, 0, 0)")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(self)
        self.dataIni()
        self.paramIni()
        self.uiIni()
        self.initializeSignalAndSlot()
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.alterUiPackMode()

    def addUncommonPackModeControls(self):
        self.hintLabel = QLabel(self)
        self.hintLabel.setGeometry(410, 160, 210, 31)
        self.hintLabel.setVisible(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hintLabel.setFont(font)
        self.hintLabel.setLineWidth(3)
        self.hintLabel.setFrameShape(QFrame.Panel)
        self.hintLabel.setFrameShadow(QFrame.Raised)
        self.hintLabel.setAlignment(Qt.AlignCenter)

        self.codeRangeLabel = QLabel(self)
        self.codeRangeLabel.setGeometry(QtCore.QRect(630, 160, 80, 31))
        self.codeRangeLabel.setText('条码范围')
        self.codeRangeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.codeRangeLabel.setFont(font)
        self.codeRangeLabel.setStyleSheet("color: rgb(0, 85, 255)")
        self.codeRangeLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.codeRangeLabel.setFrameShadow(QtWidgets.QFrame.Raised)

        self.codeRangeLineedit = QLineEdit(self)
        self.codeRangeLineedit.setGeometry(QtCore.QRect(705, 160, 180, 31))
        self.codeRangeLineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.codeRangeLineedit.setFont(font)
        pass

    def alterUiPackMode(self):
        if self.data["isCommonPackMode"]:
            self.hintLabel.setVisible(False)
            self.codeRangeLabel.setVisible(False)
            self.codeRangeLineedit.setVisible(False)
        else:
            self.label_13.setVisible(False)
            self.lineEdit_10.setVisible(False)

            self.label_18.setVisible(False)
            self.lineEdit_11.setVisible(False)

            self.label_19.setVisible(False)
            self.lineEdit_15.setVisible(False)

            self.label_12.setText("个数")

            self.hintLabel.setVisible(True)
            self.codeRangeLabel.setVisible(True)
            self.codeRangeLineedit.setVisible(True)

    def initializeSignalAndSlot(self):
        self.lineEdit_8.returnPressed.connect(self.onCodeInputEnd)
        self.checkBox_2.clicked.connect(self.onBoxNumberLengthCheckBoxClicked)
        self.checkBox_3.clicked.connect(self.onCodeLengthCheckBoxClicked)
        self.checkBox_4.clicked.connect(self.onFixCodeCheckBoxClicked)
        self.pushButton.clicked.connect(self.confirmButtonClicked)
        self.pushButton_4.clicked.connect(self.resetButtonClicked)
        self.pushButton_2.clicked.connect(self.versionButtonClicked)
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "箱号"))
        self.label_2.setText(_translate("MainWindow", "型号"))
        self.label_3.setText(_translate("MainWindow", "周期"))
        self.label_5.setText(_translate("MainWindow", "条码重复数量"))
        self.label_6.setText(_translate("MainWindow", "漏测条码数量"))
        self.label_7.setText(_translate("MainWindow", "条码错误数量"))
        self.label_8.setText(_translate("MainWindow", "TE扫码装箱系统"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_12.setText(_translate("MainWindow", "层数"))
        self.label_13.setText(_translate("MainWindow", "排数"))
        self.label_14.setText(_translate("MainWindow", "TE服务器连接状态"))
        self.label_18.setText(_translate("MainWindow", "每排格子数"))
        self.pushButton_4.setText(_translate("MainWindow", "重置"))
        self.label_16.setText(_translate("MainWindow", "当天装机数量"))
        self.label_17.setText(_translate("MainWindow", "当天装箱数量"))
        self.label_19.setText(_translate("MainWindow", "每格盒子数"))
        self.checkBox_2.setText(_translate("MainWindow", "箱号位数"))
        self.checkBox_3.setText(_translate("MainWindow", "条码位数"))
        self.checkBox_4.setText(_translate("MainWindow", "固定码"))
        self.pushButton_2.setText(_translate("MainWindow", "V1.6"))
        self.label_9.setText(_translate("MainWindow", "WELCOME!"))
        self.label_10.setText(_translate("MainWindow", "周期位置"))

    def dataIni(self):
        self.checkTool = CodeAndBoxCheck()
        self.data = self.checkTool.loadPackData()
        self.data["isCommonPackMode"] = self.isCommonPackMode
        if not self.data['isCommonPackMode']:
            self.data['maxPackNum'] = 0
            self.data['packedNum'] = 0
        if not self.checkTool.mysqlConnectState():
            return
        self.data=self.checkTool.loadDayPackedData(self.data)

        self.isScanedCodesOnBox = False
        self.codeLabelArray = []
        self.preScanCodeArray = []
        self.boxCodesArray = []
        self.isScanCodeTwiceTime = []
        pass

    def paramIni(self):
        if not self.checkTool.mysqlConnectState():
            return
        self.paintParamIni()

        if self.data['maxPackNum'] > self.data['packedNum'] and self.data["isCommonPackMode"] and self.data['packedNum']>0:
            choose = QMessageBox.question(self, 'Question', '加载上一次数据？', QMessageBox.Yes | QMessageBox.No,
                                          QMessageBox.Yes)
            if choose == QMessageBox.Yes:
                self.lineEdit_2.setText(self.data['model'])
                self.lineEdit.setText(self.data['boxNumber'])
                if self.data['weekNum'] != '':
                    self.lineEdit_3.setText(str(self.data['weekNum']))
                if self.data['layerNumEachBox'] != 0:
                    self.lineEdit_9.setText(str(self.data['layerNumEachBox']))
                if self.data['lineNumEachLayer'] != 0:
                    self.lineEdit_10.setText(str(self.data['lineNumEachLayer']))
                if self.data['pointNumEachLine'] != 0:
                    self.lineEdit_11.setText(str(self.data['pointNumEachLine']))
                if self.data['adapterNumEachPoint'] != 0:
                    self.lineEdit_15.setText(str(self.data['adapterNumEachPoint']))
                return

        self.data['weekNum'] = 0
        self.data['layerNumEachBox'] = 0
        self.data['lineNumEachLayer'] = 0
        self.data['pointNumEachLine'] = 0
        self.data['adapterNumEachPoint'] = 0
        self.data['maxPackNum'] = 0
        self.data['packedNum'] = 0

    def uiIni(self):
        self.logoIni()
        self.addUncommonPackModeControls()

        if self.data['isCheckFixCode']:
            self.lineEdit_16.setEnabled(False)
        else:
            self.lineEdit_16.setEnabled(True)

        if self.data['isCheckCodeLength']:
            self.lineEdit_17.setEnabled(False)
        else:
            self.lineEdit_17.setEnabled(True)

        if self.data['isCheckBoxNumberLength']:
            self.lineEdit_18.setEnabled(False)
        else:
            self.lineEdit_18.setEnabled(True)

        if self.checkTool.mysqlConnectState():
            self.label_14.setStyleSheet('background:green')
        else:
            self.label_14.setStyleSheet('background:red')
            return

        self.lineEdit_9.setValidator(QIntValidator(0, 1000))
        self.lineEdit_10.setValidator(QIntValidator(0, 1000))
        self.lineEdit_11.setValidator(QIntValidator(0, 1000))
        self.lineEdit_4.setValidator(QIntValidator(0, 1000))
        self.lineEdit_15.setValidator(QIntValidator(0, 1000))
        self.lineEdit_18.setValidator(QIntValidator(0, 1000))
        self.lineEdit_17.setValidator(QIntValidator(0, 1000))
        self.lineEdit_12.setReadOnly(True)

        if self.data['weekNumPosition'] != 0:
            self.lineEdit_4.setText(str(self.data['weekNumPosition']))
        self.checkBox_2.setChecked(self.data['isCheckBoxNumberLength'])
        self.checkBox_3.setChecked(self.data['isCheckCodeLength'])
        self.checkBox_4.setChecked(self.data['isCheckFixCode'])

        self.lineEdit_16.setText(self.data['fixCode'])
        if self.data['codeLength'] != 0:
            self.lineEdit_17.setText(str(self.data['codeLength']))
        if self.data['boxNumberLength'] != 0:
            self.lineEdit_18.setText(str(self.data['boxNumberLength']))

        self.lineEdit_13.setText(str(self.data['dayPackedBoxNum']))
        self.lineEdit_14.setText(str(self.data['dayPackedAdapterNum']))
        self.lineEdit_7.setText(str(self.data['dayErrorCodeNum']))
        self.lineEdit_6.setText(str(self.data['dayUntestCodeNum']))
        self.lineEdit_5.setText(str(self.data['dayDuplicateCodeNum']))

        self.lineEdit_2.setFocus()

        if self.data['packedNum'] != 0:
            self.enterScanMode()

    def paintEvent(self, QPaintEvent):
        if not self.checkTool.mysqlConnectState():
            return
        self.reDrawUi()

    def iniUnCommonPackModeUi(self,data):
        self.label_9.setVisible(False)
        for i in range(0, len(self.codeLabelArray), 1):
            self.codeLabelArray[i].deleteLater()
        self.codeLabelArray.clear()
        _row = 0
        for i in range(0, data["maxPackNum"], 1):
            _label = QLabel(self)
            _label.setStyleSheet("background:gray")
            _x = self.drawStartX
            _y = self.drawStartY + (self.gapBetweenCircle * i) * 2
            if _y > self.drawEndY:
                _x = self.drawStartX + 410
                _y = self.drawStartY + (self.gapBetweenCircle * (i - _row)) * 2
            else:
                _row += 1
            _label.setGeometry(_x, _y, 400, self.circleRadius / 1.2)
            _label.setVisible(True)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            _label.setFont(font)
            _label.setAlignment(QtCore.Qt.AlignCenter)
            self.codeLabelArray.append(_label)
        pass

    def loadUncommonPackData(self):
        self._packData=self.yamlTool.getValue("packData.yaml")
        if self.data['maxPackNum'] != self._packData['maxPackNum']:
            QMessageBox.warning(self, "Warning", "输入的数据与上一次装箱的数据不一致，无法重新加载,请检查数据后再确认！")
            return False
        self.data['packedNum'] = self._packData["packedNum"]
        self.isScanedCodesOnBox= True
        self.iniUnCommonPackModeUi(self._packData)
        _index = 0
        for code in self._packData["codes"]:
            _code=self._packData["codes"][code]
            self.preScanCodeArray.append(_code)
            self.codeLabelArray[_index].setText(_code)
            _index += 1

        _index = 0
        for codeState in self._packData["codesState"]:
            _codeState = self._packData["codesState"][codeState]
            self.isScanCodeTwiceTime.append(_codeState)
            if _codeState:
                self.codeLabelArray[_index].setStyleSheet("background:green")
            _index += 1

        return True

    def confirmButtonClicked(self):
        if not self.checkTool.mysqlConnectState():
            return

        self.getInputData()
        self.isScanedCodesOnBox = False

        if self.checkTool.checkInputDataIsValid(self.data) == InputDataState.INPUTDATA_INVALID:
            QMessageBox.warning(self, "Warning", "请确认数据是否输入正确！")
            return

        self.label_9.clear()

        checkBoxNumFlag, _packedPointNum = self.checkTool.checkBoxNumber(self.data)
        if checkBoxNumFlag == BoxState.DUPLICATE_BOX_NUMBER:
            QMessageBox.warning(self, "WARNING", "输入的箱号重复,请重新输入！")
            self.packNextBox()
            return
        elif checkBoxNumFlag == BoxState.UNDEFINED_BOX_NUMBER:
            QMessageBox.warning(self,"WARNING",'输入的箱号不合法，请重新输入！')
            self.packNextBox()
            return
        elif checkBoxNumFlag == BoxState.UNFILLED_BOX_NUMBER:
            button = QMessageBox.question(self,"Attention","加载该箱数据继续装载?",
                                   QMessageBox.Yes | QMessageBox.No)
            if button == QMessageBox.No:
                QMessageBox.warning(self, "WARNING", "输入的箱号重复,请重新输入！")
                self.packNextBox()
                return
            else:
                if self.data["isCommonPackMode"]:
                    self.data['packedNum'] = _packedPointNum
                    self.enterScanMode()
                else:
                    if self.loadUncommonPackData():
                        self.enterScanMode()
        elif checkBoxNumFlag == BoxState.VALID_BOX_NUMBER:
            self.data['packedNum'] = 0
            if not self.data["isCommonPackMode"]:
                self.iniUnCommonPackModeUi(self.data)
            self.enterScanMode()
            pass

        if self.data['maxPackNum'] <= self.data['packedNum']:
            QMessageBox.warning(self, "Warning", "输入数据异常MaxPackNum<=packedNum")
            return
        pass

    def resetUI(self):
        if not self.checkTool.mysqlConnectState():
            return
        self.lineEdit_2.setFocus()
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_10.setEnabled(True)
        self.lineEdit_11.setEnabled(True)
        self.lineEdit_15.setEnabled(True)

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_15.clear()

        if not self.paintParamIni():
            return

        self.iniPaintArray()
        self.calcPaintArray()

        self.updateProductProgress()
        self.lineEdit_8.clear()
        if self.data["isCommonPackMode"]:
            self.repaint()
        self.pushButton.setEnabled(True)
        self.lineEdit_2.setFocus()
        pass

    def resetPackData(self):
        if not self.checkTool.mysqlConnectState():
            return
        self.data['model'] = ''
        self.data['boxNumber'] = ''
        self.data['weekNum'] = ''
        self.data['adapterNumEachLayer'] = 0
        self.data['layerNumEachBox'] = 0
        self.data['numAdapterEachLine'] = 0
        self.data['pointNumEachLine'] = 0
        self.data['adapterNumEachPoint'] = 0
        self.data['packedNum'] = 0
        self.data['maxPackNum'] = 0
        self.data['lineNumEachLayer'] = 0

    def enterScanMode(self):
        if not self.checkTool.mysqlConnectState():
            return

        if self.data["isCommonPackMode"]:
            self.iniPaintArray()
            self.calcPaintArray()
        else:
            self.hintLabel.setText("请开始扫入需装箱条码！")
            self.codeRangeLineedit.setEnabled(False)

        self.lineEdit_8.clear()
        self.label_9.setText('')
        self.repaint()
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_15.setEnabled(False)

        self.lineEdit_8.setFocus()
        self.pushButton.setEnabled(False)
        pass

    def resetButtonClicked(self):
        if not self.checkTool.mysqlConnectState():
            return

        choose = QMessageBox.question(self,"重置","重置所有数据？",QMessageBox.Yes|QMessageBox.No)
        if choose == QMessageBox.No:
            self.lineEdit_8.setFocus()
            return

        if not self.data["isCommonPackMode"]:
            self.hintLabel.clear()
            self.clearUnCommonPackModeData()
            self.codeRangeLineedit.setEnabled(True)

        self.resetPackData()
        self.resetUI()
        pass

    def versionButtonClicked(self):
        if QMessageBox.Yes == QMessageBox.question(self,"Warning!","重置扫码错误数据？",QMessageBox.Yes,QMessageBox.No):
            _passwd,isOk=QInputDialog.getText(self, "Warning", "请输入密码确认", QLineEdit.Password,"")

            if _passwd=='te998' and isOk:
                self.checkTool.clearUntestCodeRecord()
                self.data=self.checkTool.loadDayPackedData(self.data)
                self.repaint()
            elif isOk and _passwd!='te998':
                QMessageBox.warning(self,"Warning","密码错误！")
            else:
                pass
        pass

    def clearUnCommonPackModeData(self):
        for i in range(0, len(self.codeLabelArray), 1):
            self.codeLabelArray[i].deleteLater()
        self.codeLabelArray.clear()
        self.boxCodesArray.clear()
        self.preScanCodeArray.clear()
        self.isScanCodeTwiceTime.clear()
        pass

    def paintParamIni(self):
        self.maxRow = 0
        self.maxCol = 0
        if not self.checkTool.mysqlConnectState():
            return
        self.yamlTool=Yaml_Tool()
        self.params=self.yamlTool.getValue('deviceParam.yaml')
        self.circleRadius=self.params['drawParam']['circleRadius']
        self.gapBetweenCircle= self.params['drawParam']['gapBetweenCircle']
        self.drawStartX=self.label_9.x()+self.circleRadius+3
        self.drawStartY=self.label_9.y()+self.circleRadius+3
        self.drawEndX=self.label_9.rect().right()-self.circleRadius-1
        self.drawEndY=self.label_9.y()+self.label_9.height()-self.circleRadius-1

        if self.circleRadius == 0 or self.gapBetweenCircle == 0:
            QMessageBox.warning(self, "Warning", "参数异常(circleRadius==0||gapBetweenCircle==0),无法初始化！")
            exit(0)

        self.paintFlagArray=np.zeros([self.maxRow,self.maxCol],dtype=int)
        self.validCoordinate=[]
        return True
        pass

    def logoIni(self):
        self.logPixMap=QPixmap('PI_LOGO.png')
        self.fitPixMap=self.logPixMap.scaled(self.label_4.width(),
                                             self.label_4.height(),
                                             Qt.IgnoreAspectRatio,
                                             Qt.SmoothTransformation)
        self.label_4.setPixmap(self.fitPixMap)
        pass

    def iniPaintArray(self):
        self.validCoordinate.clear()
        startX = self.drawStartX
        startY = self.drawStartY

        self.maxRow = 0
        self.maxCol = 0

        while startX <= self.drawEndX:
            self.maxCol += 1
            startX += (self.circleRadius + self.gapBetweenCircle)

        while startY <= self.drawEndY:
            self.maxRow += 1
            startY += (self.circleRadius + self.gapBetweenCircle)

        self.paintFlagArray = np.zeros([self.maxRow, self.maxCol], dtype=int)

    def calcPaintArray(self):
        if self.data['adapterNumEachLayer'] == 0 \
                or self.data['layerNumEachBox'] == 0\
                or self.data['numAdapterEachLine'] == 0:
            return

        if self.circleRadius <= 3:
            QMessageBox.warning(self, "Warning!", "输入超范围，请联系相关人员！")
            return

        startCol = 0
        startRow = 0
        if (self.data['adapterNumEachLayer'] % self.data['numAdapterEachLine']) == 0:
            offset = 0
        else:
            offset = 1

        rowEachLayer = int((self.data['adapterNumEachLayer']/self.data['numAdapterEachLine']))+offset
        markPointNum = 0
        ii = 0
        jj = 0
        kk = 0

        for i in range(0, self.data['layerNumEachBox'], 1):
            ii = i
            layerCount = 0
            tempRow = startRow
            for k in range(0, rowEachLayer, 1):
                kk = k
                if not startRow < self.maxRow:
                    break
                tempCol = startCol
                for j in range(0, self.data['numAdapterEachLine'], 1):
                    jj = j
                    if not startCol < self.maxCol:
                        break
                    if layerCount < self.data['adapterNumEachLayer']:
                        self.paintFlagArray[startRow][startCol] = CodeState.VALID_POINT
                        coordinate = Coordinate(startRow, startCol)
                        self.validCoordinate.append(coordinate)

                        if markPointNum < self.data['packedNum']:
                            self.paintFlagArray[startRow][startCol] = CodeState.PACKED_POINT
                            markPointNum += 1
                    else:
                        self.paintFlagArray[startRow][startCol] = CodeState.INI_FLAG
                    startCol += 1
                    layerCount += 1
                startRow += 1
                startCol = tempCol

            if (self.maxCol-startCol-1) > (self.data['numAdapterEachLine']*2):
                startCol += (1+self.data['numAdapterEachLine'])
                startRow = tempRow
            elif (self.maxRow-startRow-1) > rowEachLayer:
                startCol = 0
                startRow += 1
            else:
                break

        if ii != self.data['layerNumEachBox']-1 \
                or kk != rowEachLayer-1 \
                or jj != self.data['numAdapterEachLine']-1\
                or self.maxRow<self.data['lineNumEachLayer']\
                or self.maxCol<self.data['numAdapterEachLine']:
            self.circleRadius=int(self.circleRadius/1.05)
            self.gapBetweenCircle=int(self.gapBetweenCircle/1.05)
            if self.gapBetweenCircle<6:
                self.gapBetweenCircle=5
            self.iniPaintArray()
            self.calcPaintArray()

    def updateProductProgress(self):
        self.label_11.setText(str(self.data['packedNum']) + "/" + str(self.data['maxPackNum']))
        self.lineEdit_13.setText(str(self.data['dayPackedBoxNum']))
        self.lineEdit_14.setText(str(self.data['dayPackedAdapterNum']))
        self.lineEdit_7.setText(str(self.data['dayErrorCodeNum']))
        self.lineEdit_6.setText(str(self.data['dayUntestCodeNum']))
        self.lineEdit_5.setText(str(self.data['dayDuplicateCodeNum']))

    def reDrawUi(self):
        self.updateProductProgress()
        if not self.data["isCommonPackMode"]:
            return
        paint=QPainter()
        paint.begin(self)

        startX=self.drawStartX
        startY=self.drawStartY
        countPointFlag=0

        for i in range(0,self.maxRow,1):
            for j in range(0,self.maxCol,1):
                drawX=startX+j*(self.circleRadius+self.gapBetweenCircle)
                drawY=startY+i*(self.circleRadius+self.gapBetweenCircle)
                if self.paintFlagArray[i][j] == CodeState.INI_FLAG:
                    pass
                elif self.paintFlagArray[i][j] == CodeState.VALID_POINT:
                    paint.setPen(QPen(QtCore.Qt.gray,4,QtCore.Qt.SolidLine))
                    linearGradient = QLinearGradient(0, 0, 400, 400)
                    linearGradient.setColorAt(1.0, Qt.gray)
                    paint.setBrush(linearGradient)
                    paint.drawEllipse(drawX,drawY, self.circleRadius, self.circleRadius)
                    countPointFlag += 1

                elif self.paintFlagArray[i][j] == CodeState.PACKED_POINT:
                    paint.setPen(QPen(QtCore.Qt.green, 4, QtCore.Qt.SolidLine))
                    linearGradient = QLinearGradient(0, 0, 400, 400)
                    linearGradient.setColorAt(1.0, Qt.green)
                    paint.setBrush(linearGradient)
                    paint.drawEllipse(drawX,drawY, self.circleRadius, self.circleRadius)
                    countPointFlag += 1
                elif self.paintFlagArray[i][j] == CodeState.DUPLICATE_CODE_POINT:
                    paint.setPen(QPen(QtCore.Qt.magenta,4,QtCore.Qt.SolidLine))
                    linearGradient = QLinearGradient(0, 0, 400, 400)
                    linearGradient.setColorAt(1.0, Qt.magenta)
                    paint.setBrush(linearGradient)
                    paint.drawEllipse(drawX,drawY,self.circleRadius,self.circleRadius)
                    countPointFlag += 1
                elif self.paintFlagArray[i][j]==CodeState.ERROR_WEEKNUM_CODE_POINT:
                    paint.setPen(QPen(QtCore.Qt.darkYellow,4,QtCore.Qt.SolidLine))
                    linearGradient = QLinearGradient(0, 0, 400, 400)
                    linearGradient.setColorAt(1.0, Qt.darkYellow)
                    paint.setBrush(linearGradient)
                    paint.drawEllipse(drawX,drawY,self.circleRadius,self.circleRadius)
                    countPointFlag+=1
                elif self.paintFlagArray[i][j]==CodeState.UNTEST_CODE_POINT:
                    paint.setPen(QPen(QtCore.Qt.red,4,QtCore.Qt.SolidLine))
                    linearGradient = QLinearGradient(0, 0, 400, 400)
                    linearGradient.setColorAt(1.0, Qt.red)
                    paint.setBrush(linearGradient)
                    paint.drawEllipse(drawX,drawY,self.circleRadius,self.circleRadius)
                    countPointFlag+=1
                elif self.paintFlagArray[i][j]==CodeState.ERROR_FIXED_CODE_POINT:
                    paint.setPen(QPen(QtCore.Qt.black,4,QtCore.Qt.SolidLine))
                    linearGradient = QLinearGradient(0, 0, 400, 400)
                    linearGradient.setColorAt(1.0, Qt.black)
                    paint.setBrush(linearGradient)
                    paint.drawEllipse(drawX,drawY,self.circleRadius,self.circleRadius)
                    countPointFlag+=1
                elif self.paintFlagArray[i][j]==CodeState.ERROR_CODE_LENGTH:
                    paint.setPen(QPen(QtCore.Qt.darkBlue,4,QtCore.Qt.SolidLine))
                    linearGradient = QLinearGradient(0, 0, 400, 400)
                    linearGradient.setColorAt(1.0, Qt.darkBlue)
                    paint.setBrush(linearGradient)
                    paint.drawEllipse(drawX,drawY,self.circleRadius,self.circleRadius)
                    countPointFlag += 1
                elif self.paintFlagArray[i][j] == CodeState.SAVE_ERROR_POINT:
                    paint.setPen(QPen(QtCore.Qt.darkRed,4,QtCore.Qt.SolidLine))
                    linearGradient = QLinearGradient(0, 0, 400, 400)
                    linearGradient.setColorAt(1.0, Qt.darkRed)
                    paint.setBrush(linearGradient)
                    paint.drawEllipse(drawX,drawY,self.circleRadius,self.circleRadius)
                    countPointFlag+=1
                if countPointFlag == self.data['adapterNumEachPoint']\
                        and self.data['maxPackNum'] != 0\
                        and self.data['adapterNumEachPoint'] != 1:
                    paint.setPen(QPen(QtCore.Qt.blue, 4, QtCore.Qt.SolidLine))
                    linearGradient = QLinearGradient(0, 0, 400, 400)
                    linearGradient.setColorAt(1.0, Qt.blue)
                    paint.setBrush(linearGradient)
                    paint.drawLine(QPoint(drawX+self.circleRadius+(self.gapBetweenCircle/2),drawY),
                                QPoint(drawX+self.circleRadius+(self.gapBetweenCircle/2),drawY+self.circleRadius))
                    countPointFlag = 0
        # paint.end()

    def getInputData(self):
        if not self.checkTool.mysqlConnectState():
            return

        self.data['fixCode'] = self.lineEdit_16.text()

        if self.lineEdit_17.text() == '':
            self.data['codeLength'] = 0
        else:
            self.data['codeLength'] = int(self.lineEdit_17.text())

        if self.lineEdit_18.text() == '':
            self.data['boxNumberLength'] = 0
        else:
            self.data['boxNumberLength'] = int(self.lineEdit_18.text())

        if not self.data["isCommonPackMode"]:
            self.data['codeRange'] = self.codeRangeLineedit.text()

        self.data['model'] = self.lineEdit_2.text()

        self.data['boxNumber'] = self.lineEdit.text()
        if self.lineEdit_3.text() == '':
            self.data['weekNum'] = ''
        else:
            self.data['weekNum'] = self.lineEdit_3.text()

        if self.lineEdit_4.text() == '':
            self.data['weekNumPosition']=0
        else:
            self.data['weekNumPosition'] = int(self.lineEdit_4.text())

        if self.lineEdit_10.text() == '':
            self.data['lineNumEachLayer']=0
        else:
            self.data['lineNumEachLayer'] = int(self.lineEdit_10.text())

        if self.lineEdit_9.text() == '':
            self.data['layerNumEachBox']=0
        else:
            self.data['layerNumEachBox'] = int(self.lineEdit_9.text())

        if self.lineEdit_15.text() == '':
            self.data['adapterNumEachPoint']=0
        else:
            self.data['adapterNumEachPoint'] = int(self.lineEdit_15.text())

        if self.lineEdit_11.text() == '':
            self.data['pointNumEachLine']=0
        else:
            self.data['pointNumEachLine'] = int(self.lineEdit_11.text())

        self.data['numAdapterEachLine'] = self.data['pointNumEachLine']\
                                          * self.data['adapterNumEachPoint']

        self.data['adapterNumEachLayer'] = self.data['lineNumEachLayer']\
                                          * self.data['pointNumEachLine']\
                                          * self.data['adapterNumEachPoint']

        self.data['packedNum'] = 0

        if self.data["isCommonPackMode"]:
            self.data['maxPackNum'] = self.data['layerNumEachBox'] \
                                      * self.data['lineNumEachLayer'] \
                                      * self.data['pointNumEachLine'] \
                                      * self.data['adapterNumEachPoint']
        elif self.lineEdit_9.text()!='':
            self.data["maxPackNum"] = int(self.lineEdit_9.text())
        pass

    def preScanCodeOnBox(self):
        if self.data['code'] in self.preScanCodeArray:
            self.hintLabel.setStyleSheet("color:red")
            self.hintLabel.setText("条码已经扫入该箱！")
            return

        self.data['isCheckUntest'] = False
        checkResult = self.checkTool.checkCodeValidity(self.data)

        self.hintLabel.setStyleSheet("color:red")
        if checkResult == CodeState.ERROR_CODE_LENGTH:
            self.hintLabel.setText("条码长度错误！")
            return
        elif checkResult == CodeState.ERROR_WEEKNUM_CODE_POINT:
            self.hintLabel.setText("条码周期错误！")
            return
        elif checkResult == CodeState.ERROR_FIXED_CODE_POINT:
            self.hintLabel.setText("条码不包含固定码！")
            return
        elif checkResult == CodeState.DUPLICATE_CODE_POINT:
            self.hintLabel.setText("条码重复！")
            return

        self.checkTool.updateCodeBoxNumber(self.data)

        self.hintLabel.clear()
        self.preScanCodeArray.append(self.data['code'])
        self.isScanCodeTwiceTime.append(False)
        self.codeLabelArray[len(self.preScanCodeArray) - 1].setText(self.data['code'])
        if len(self.preScanCodeArray) == self.data["maxPackNum"]:
            self.isScanedCodesOnBox = True
            self.hintLabel.setText("开始扫描电源条码!")
        return

    def checkAndSaveCode(self):
        ####yuanminmin###########################
        self.data['isCheckUntest'] = True
        self.data['isCheckDuplicate'] = True

        checkResult = self.checkTool.checkCodeValidity(self.data)
        if not self.data["isCommonPackMode"]:
            _codeIndex = -1
            self.hintLabel.clear()
            for i in range(0, len(self.preScanCodeArray), 1):
                if self.preScanCodeArray[i] == self.data['code']:
                    _codeIndex = i
                    break

            self.hintLabel.setStyleSheet("color:red")
            if _codeIndex == -1:
                self.hintLabel.setText("条码不属于该箱！")
                return
            else:
                if self.data['code'] in self.boxCodesArray:
                    self.hintLabel.setText("该条码已装箱！")
                    return
            if checkResult == CodeState.PACKED_POINT:
                if self.isScanCodeTwiceTime[_codeIndex]:
                    self.boxCodesArray.append(self.data['code'])
                    self.codeLabelArray[_codeIndex].setStyleSheet("background:green")
                else:
                    self.isScanCodeTwiceTime[_codeIndex] = True
                    self.codeLabelArray[_codeIndex].setStyleSheet("background:yellow")
                    return
            if checkResult == CodeState.UNTEST_CODE_POINT:
                self.codeLabelArray[_codeIndex].setStyleSheet("background:red")
        # else:
        #     #######将检测检测赋给显示界面#####################
        #     self.paintFlagArray[self.validCoordinate[self.data['packedNum']].x][
        #         self.validCoordinate[self.data['packedNum']].y] = checkResult

        if checkResult == CodeState.PACKED_POINT:
            self.data['dayPackedAdapterNum'] += 1
            self.data['packedNum'] += 1

            if (not self.data['isCommonPackMode']) and self.data['code'] in self.boxCodesArray:
                self.saveUnCommonPackData()
        elif checkResult == CodeState.ERROR_CODE_LENGTH:
            self.lineEdit_12.setText('长度错误 '+self.data['code'])
            self.hintLabel.setText("条码长度错误！")
            self.data['dayErrorCodeNum'] += 1
        elif checkResult == CodeState.ERROR_FIXED_CODE_POINT:
            self.lineEdit_12.setText('无固定码 '+self.data['code'])
            self.hintLabel.setText("条码不包含固定码！")
            self.data['dayErrorCodeNum'] += 1
        elif checkResult == CodeState.UNTEST_CODE_POINT:
            self.lineEdit_12.setText('未测试 '+self.data['code'])
            self.hintLabel.setText("条码未测试！")
            self.data['dayUntestCodeNum'] += 1
        elif checkResult == CodeState.DUPLICATE_CODE_POINT:
            self.lineEdit_12.setText('重复 '+self.data['code'])
            self.hintLabel.setText("条码重复！")
            self.data['dayDuplicateCodeNum'] += 1
        elif checkResult == CodeState.ERROR_WEEKNUM_CODE_POINT:
            self.lineEdit_12.setText('周期错误 '+self.data['code'])
            self.hintLabel.setText("条码周期错误！")
            self.data['dayErrorCodeNum'] += 1

        ###############保存条码错误的时候，报错并回滚################
        _checkResult=checkResult
        if not self.checkTool.savePackedDataToServer(self.data,checkResult):
            checkResult=CodeState.SAVE_ERROR_POINT
            self.lineEdit_12.setText('保存错误 '+self.data['code'])
            self.data['dayErrorCodeNum'] += 1
            if _checkResult==CodeState.PACKED_POINT:
                self.data['dayPackedAdapterNum'] -= 1
                self.data['packedNum'] -= 1

        self.paintFlagArray[self.validCoordinate[self.data['packedNum']].x][self.validCoordinate[self.data['packedNum']].y] = checkResult
        self.repaint()
        self.checkTool.saveDataToLocal(self.data)

        if self.data['packedNum'] == self.data['maxPackNum']:
            self.packNextBox()
        pass

    def onCodeInputEnd(self):
        if not self.checkTool.mysqlConnectState():
            return

        if self.data['maxPackNum']==0 or self.data['packedNum']>=self.data['maxPackNum']:
            return

        self.data['code'], isOk = self.checkTool.preProcessCode(self.lineEdit_8.text())
        if not isOk:
            return

        self.lineEdit_8.clear()
        self.lineEdit_12.setText(self.data['code'])

        if (not self.isScanedCodesOnBox) and (not self.data["isCommonPackMode"]):
            self.preScanCodeOnBox()
            return
        self.checkAndSaveCode()

    def saveUnCommonPackData(self):
        self._packData={}
        self._packData["packedNum"]=self.data["packedNum"]
        self._packData["maxPackNum"]=self.data["maxPackNum"]
        self._packData["weekNum"]=self.data["weekNum"]
        self._packData["boxNumber"]=self.data["boxNumber"]
        self._packData["model"]=self.data["model"]
        self._packData["codes"] = {}
        self._packData["codesState"] = {}
        for i in range(0,len(self.preScanCodeArray),1):
            self._packData["codes"]["code"+str(i)]=self.preScanCodeArray[i]
            self._packData["codesState"]["code"+str(i)]=self.isScanCodeTwiceTime[i]
        self.yamlTool.saveParam("packData.yaml",self._packData)
        pass

    def onBoxNumberLengthCheckBoxClicked(self):
        if not self.checkTool.mysqlConnectState():
            return
        if self.lineEdit_18.text() == '':
            self.checkBox_2.setChecked(False)
            QMessageBox.warning(self,"Warning","请输入有效数据！")
            return
        self.data['isCheckBoxNumberLength']=self.checkBox_2.isChecked()

        if self.data['isCheckBoxNumberLength']:
            self.lineEdit_18.setEnabled(False)
        else:
            self.lineEdit_18.setEnabled(True)
        self.data['boxNumberLength']=int(self.lineEdit_18.text())
        self.checkTool.saveDataToLocal(self.data)
        pass

    def onCodeLengthCheckBoxClicked(self):
        if not self.checkTool.mysqlConnectState():
            return
        if self.lineEdit_17.text() == '':
            self.checkBox_3.setChecked(False)
            QMessageBox.warning(self,"Warning","请输入有效数据！")
            return

        self.data['isCheckCodeLength']=self.checkBox_3.isChecked()
        if self.data['isCheckCodeLength']:
            self.lineEdit_17.setEnabled(False)
        else:
            self.lineEdit_17.setEnabled(True)
        self.data['codeLength']=int(self.lineEdit_17.text())
        self.checkTool.saveDataToLocal(self.data)
        pass

    def onFixCodeCheckBoxClicked(self):
        if not self.checkTool.mysqlConnectState():
            return
        if self.lineEdit_16.text() == '':
            self.checkBox_4.setChecked(False)
            QMessageBox.warning(self,"Warning","请输入有效数据！")
            return
        self.data['isCheckFixCode']=self.checkBox_4.isChecked()
        if self.data['isCheckFixCode']:
            self.lineEdit_16.setEnabled(False)
        else:
            self.lineEdit_16.setEnabled(True)
        self.data['fixCode']=self.lineEdit_16.text()
        self.checkTool.saveDataToLocal(self.data)
        pass

    def packNextBox(self):
        if not self.data["isCommonPackMode"]:
            self.boxCodesArray.clear()
            self.preScanCodeArray.clear()
            self.isScanCodeTwiceTime.clear()
            self.isScanedCodesOnBox=False

        if not self.checkTool.mysqlConnectState():
            return
        boxNumber,isOK=QInputDialog.getText(self,'装下一箱？','箱号', QLineEdit.Normal)
        if isOK:
            if boxNumber == "":
                QMessageBox.warning(self,"Warning","箱号不能为空！")
            self.data['packedNum'] = 0
            self.lineEdit.setText(boxNumber)
            self.confirmButtonClicked()

        self.data=self.checkTool.loadDayPackedData(self.data)
        self.repaint()
        pass

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        choose = QMessageBox.question(self, 'Question', '确认关闭程序？', QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.Yes)
        if choose == QMessageBox.No:
            a0.ignore()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    runGui=GUI()
    # runGui.showFullScreen()
    runGui.show()
    sys.exit(app.exec_())

