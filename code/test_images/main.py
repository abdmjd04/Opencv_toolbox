# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy
import PIL
from PIL import *
import numpy as np
import easygui
import glob
import cv2
from PIL import Image, ImageTk
from tkinter import filedialog
from matplotlib import pyplot as plt
#from tkinter import messagebox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import glob
import os
import face_recognition
import pickle
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1244, 864)
        font = QtGui.QFont()
        font.setFamily("Hobo Std")
        font.setPointSize(24)
        Form.setFont(font)
        Form.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(190, 191, 200);\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(440, 30, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Cooper Std Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 190, 331, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(620, 190, 331, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 670, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 670, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(960, 150, 241, 161))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 40, 141, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 90, 171, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(960, 320, 251, 191))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 40, 141, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 80, 81, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 120, 81, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 360, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 450, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 540, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(980, 530, 241, 301))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 221, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 10, 121, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 50, 81, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 90, 121, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.checkBox_9 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 20, 161, 22))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_10.setGeometry(QtCore.QRect(10, 60, 141, 22))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_11.setGeometry(QtCore.QRect(10, 100, 97, 22))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_12.setGeometry(QtCore.QRect(10, 140, 121, 22))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_13.setGeometry(QtCore.QRect(10, 180, 121, 22))
        self.checkBox_13.setObjectName("checkBox_13")
        self.tabWidget.addTab(self.tab_2, "")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(743, 530, 201, 101))
        self.textEdit.setObjectName("textEdit")
        self.comboBox_7 = QtWidgets.QComboBox(Form)
        self.comboBox_7.setGeometry(QtCore.QRect(30, 580, 161, 22))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")

        self.comboBox_6 = QtWidgets.QComboBox(Form)
        self.comboBox_6.setGeometry(QtCore.QRect(30, 490, 161, 22))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(30, 400, 161, 22))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(30, 310, 161, 22))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(30, 220, 161, 22))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 130, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(360, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(750, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OpenCV Tool Box"))
        self.label.setText(_translate("Form", "OpenCV Tool Box"))
        self.pushButton_2.setText(_translate("Form", "Load Image"))
        self.pushButton_3.setText(_translate("Form", "Process"))
        self.groupBox.setTitle(_translate("Form", "Detect Faces"))
        self.checkBox.setText(_translate("Form", "Deep Learning"))
        self.checkBox_2.setText(_translate("Form", "Cascading classifiers"))
        self.groupBox_2.setTitle(_translate("Form", "Recognize Detected Faces"))
        self.checkBox_3.setText(_translate("Form", "Deep Learning"))
        self.checkBox_4.setText(_translate("Form", "LBP"))
        self.checkBox_5.setText(_translate("Form", "PCA"))
        self.label_4.setText(_translate("Form", "Basic Operations"))
        self.label_5.setText(_translate("Form", "Morphological Operations"))
        self.label_6.setText(_translate("Form", "Filters"))
        self.label_7.setText(_translate("Form", "Lines & Contours"))
        self.label_8.setText(_translate("Form", "Feature Points"))
        self.label_9.setText(_translate("Form", "Camera Calibration & Other "))
        self.groupBox_3.setTitle(_translate("Form", "Extra Tasks"))
        self.checkBox_6.setText(_translate("Form", "AgeGender"))
        self.checkBox_7.setText(_translate("Form", "YOLO"))
        self.checkBox_8.setText(_translate("Form", "Colorization"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Deep Learning"))
        self.checkBox_9.setText(_translate("Form", "Red Eye Remover"))
        self.checkBox_10.setText(_translate("Form", "Eye Detector"))
        self.checkBox_11.setText(_translate("Form", "Head Pose"))
        self.checkBox_12.setText(_translate("Form", "Eigen Faces"))
        self.checkBox_13.setText(_translate("Form", "Pencil Sketch"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Image Processing"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Hobo Std\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">Output</span></p></body></html>"))
        self.comboBox_7.setItemText(0, _translate("Form", "Select any"))
        self.comboBox_7.setItemText(1, _translate("Form", "Calibrate"))
        self.comboBox_7.setItemText(2, _translate("Form", "7 POINT"))
        self.comboBox_7.setItemText(3, _translate("Form", "8 POINT"))
        self.comboBox_7.setItemText(4, _translate("Form", "RANSAC"))
        self.comboBox_7.setItemText(5, _translate("Form", "Epipolar Lines"))
        self.comboBox_7.setItemText(6, _translate("Form", "Compute Homography"))
        self.comboBox_7.setItemText(7, _translate("Form", "Mosaic"))
        self.comboBox_7.setItemText(8, _translate("Form", "Stitch"))
        self.comboBox_6.setItemText(0, _translate("Form", "Select Any"))
        self.comboBox_6.setItemText(1, _translate("Form", "Harris Corner"))
        self.comboBox_6.setItemText(2, _translate("Form", "FAST"))
        self.comboBox_6.setItemText(3, _translate("Form", "SURF"))
        self.comboBox_6.setItemText(4, _translate("Form", "SIFT"))
        self.comboBox_6.setItemText(5, _translate("Form", "Feature matching"))
        self.comboBox_5.setItemText(0, _translate("Form", "Select any"))
        self.comboBox_5.setItemText(1, _translate("Form", "Extract Lines"))
        self.comboBox_5.setItemText(2, _translate("Form", "Extract Circles"))
        self.comboBox_5.setItemText(3, _translate("Form", "Contours"))
        self.comboBox_5.setItemText(4, _translate("Form", "Bounding box"))
        self.comboBox_5.setItemText(5, _translate("Form", "Enclosing circle"))
        self.comboBox_4.setItemText(0, _translate("Form", "Select any"))
        self.comboBox_4.setItemText(1, _translate("Form", "Median Blur "))
        self.comboBox_4.setItemText(2, _translate("Form", "Average Blur"))
        self.comboBox_4.setItemText(3, _translate("Form", "Gaussian blur"))
        self.comboBox_4.setItemText(4, _translate("Form", "Bilteral filter blur"))
        self.comboBox_4.setItemText(5, _translate("Form", "Sobel Operator"))
        self.comboBox_4.setItemText(6, _translate("Form", "Laplace Operator"))
        self.comboBox_4.setItemText(7, _translate("Form", "Canny Edge"))
        self.comboBox_3.setItemText(0, _translate("Form", "Select any"))
        self.comboBox_3.setItemText(1, _translate("Form", "Dilate"))
        self.comboBox_3.setItemText(2, _translate("Form", "Erode"))
        self.comboBox_3.setItemText(3, _translate("Form", "Close"))
        self.comboBox_3.setItemText(4, _translate("Form", "Open"))
        self.comboBox_2.setItemText(0, _translate("Form", "Select any"))
        self.comboBox_2.setItemText(1, _translate("Form", "Add Salt"))
        self.comboBox_2.setItemText(2, _translate("Form", "Add Pepper Noise"))
        self.comboBox_2.setItemText(3, _translate("Form", "Add Logo"))
        self.comboBox_2.setItemText(4, _translate("Form", "BGR2RGB"))
        self.comboBox_2.setItemText(5, _translate("Form", "BGR2YCrCB"))
        self.comboBox_2.setItemText(6, _translate("Form", "BGR2Lab"))
        self.comboBox_2.setItemText(7, _translate("Form", "BGR2HSV"))
        self.comboBox_2.setItemText(8, _translate("Form", "Compute Histogram"))
        self.comboBox_2.setItemText(9, _translate("Form", "Histogram Equalization"))
        self.label_10.setText(_translate("Form", "   Input"))
        self.label_11.setText(_translate("Form", "  Output"))
        self.pushButton_2.clicked.connect(self.load_image)
        self.pushButton_3.clicked.connect(self.process)

    def load_image(self):
            global img
            global a
            global qImg
            path = easygui.fileopenbox()
            img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (331, 281))
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_2.setPixmap(pixmap)
            self.label_3.clear()
            a = img

    def salt(self):
            row, col, ch = a.shape
            #sNp = 2.0
            sNp = 0.5
            amount = 0.05
            out = np.copy(a)

            # Salt mode
            num_salt = np.ceil(amount * a.size * sNp)
            coords = [np.random.randint(0, i - 1, int(num_salt))
                      for i in a.shape]
            out[coords] = 1
            height, width, channel = out.shape
            bytesPerLine = 3 * width
            qImg = QImage(out.data, width, height, bytesPerLine, QImage.Format_RGB888)

            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)

    def pepper(self):
            row, col, ch = a.shape
            sNp = 0.5
            amount = 0.05
            out = np.copy(a)

            num_pepper = np.ceil(amount * a.size * (1. - sNp))
            coords = [np.random.randint(0, i - 1, int(num_pepper))
                      for i in a.shape]
            out[coords] = 0
            height, width, channel = out.shape
            bytesPerLine = 3 * width
            qImg = QImage(out.data, width, height, bytesPerLine, QImage.Format_RGB888)

            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)

    def addlogo(self):
            path = easygui.fileopenbox()
            # Load two images
            img1 = a
            img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
            #img1 = cv2.imread(path)
            #path = easygui.fileopenbox()
            img2 = cv2.imread(path)
            img2 = cv2.resize(img2, (75, 75))
            # I want to put logo on top-left corner, So I create a ROI
            rows, cols, channels = img2.shape
            roi = img1[0:rows, 0:cols]
            # Now create a mask of logo and create its inverse mask also
            img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            # Now black-out the area of logo in ROI
            img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
            # Take only region of logo from logo image.
            img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
            # Put logo in ROI and modify the main image
            dst = cv2.add(img1_bg, img2_fg)
            img1[0:rows, 0:cols] = dst
            # cv2.imshow('res',img1)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            img1 = cv2.resize(img1, (331, 281))
            height, width, channel = img1.shape
            bytesPerLine = 3 * width
            qImg = QImage(img1.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)

    def bgr2rgb(self):
            bgrtorgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, channel = bgrtorgb.shape
            bytesPerLine = 3 * width
            qImg = QImage(bgrtorgb.data, width, height, bytesPerLine, QImage.Format_RGB888)

            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)

    def bgr2Ycrcb(self):
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
            height, width, channel = img1.shape
            bytesPerLine = 3 * width
            qImg = QImage(img1.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)
    def bgr2lab(self):
            bgrtolab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            height, width, channel = bgrtolab.shape
            bytesPerLine = 3 * width
            qImg = QImage(bgrtolab.data, width, height, bytesPerLine, QImage.Format_RGB888)

            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)

    def bgr2lab(self):
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            height, width, channel = img1.shape
            bytesPerLine = 3 * width
            qImg = QImage(img1.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)
    def bgr2gray(self):
            bgrtogray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            height, width, channel = bgrtogray.shape
            bytesPerLine = 3 * width
            qImg = QImage(bgrtogray.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)

    def bgr2hsv(self):
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            height, width, channel = img1.shape
            bytesPerLine = 3 * width
            qImg = QImage(img1.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)

    def histogram(self):
            hist, bins = np.histogram(img.ravel(), 256, [0, 256])
            color = ('b', 'g', 'r')
            for i, col in enumerate(color):
                    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
                    plt.plot(histr, color=col)
                    plt.xlim([0, 256])
            plt.show()
            self.comboBox_2.setCurrentIndex(0)
    def equalizehist(self):
            img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

            # equalize the histogram of the Y channel
            img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

            # convert the YUV image back to RGB format
            img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
            output = cv2.cvtColor(img_output, cv2.COLOR_BGR2RGB)
            height, width, channel = output.shape
            bytesPerLine = 3 * width
            qImg = QImage(output.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_2.setCurrentIndex(0)

    def dilation(self):
            kernel = np.ones((5, 5), np.uint8)
            erosion = cv2.dilate(img, kernel, iterations=1)
            height, width, channel = erosion.shape
            bytesPerLine = 3 * width
            qImg = QImage(erosion.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_3.setCurrentIndex(0)

    def open(self):
            kernel = np.ones((5, 5), np.uint8)
            erosion = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            height, width, channel = erosion.shape
            bytesPerLine = 3 * width
            qImg = QImage(erosion.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_3.setCurrentIndex(0)

    def close(self):
            kernel = np.ones((5, 5), np.uint8)
            erosion = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
            height, width, channel = erosion.shape
            bytesPerLine = 3 * width
            qImg = QImage(erosion.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_3.setCurrentIndex(0)
    def erode(self):
            kernel = np.ones((5, 5), np.uint8)
            erosion = cv2.erode(img, kernel, iterations=1)
            height, width, channel = erosion.shape
            bytesPerLine = 3 * width
            qImg = QImage(erosion.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_3.setCurrentIndex(0)

    def medianblur(self):
            blur = cv2.medianBlur(img, 3)
            # img = cv2.resize(blur,(250,250))
            height, width, channel = blur.shape
            bytesPerLine = 3 * width
            qImg = QImage(blur.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_4.setCurrentIndex(0)
    def averageblur(self):
            blur = cv2.blur(img, (5, 5))
            height, width, channel = blur.shape
            bytesPerLine = 3 * width
            qImg = QImage(blur.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_4.setCurrentIndex(0)
    def gaussianblur(self):
            blur = cv2.GaussianBlur(img, (5, 5), 0)
            height, width, channel = blur.shape
            bytesPerLine = 3 * width
            qImg = QImage(blur.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_4.setCurrentIndex(0)

    def bilateralfilterblur(self):
            blur = cv2.bilateralFilter(img, 9, 75, 75)
            height, width, channel = blur.shape
            bytesPerLine = 3 * width
            qImg = QImage(blur.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_4.setCurrentIndex(0)
    def sobel(self):

            sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
            plt.subplot(1, 2, 1), plt.imshow(sobelx, cmap='gray')
            plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
            plt.subplot(1, 2, 2), plt.imshow(sobely, cmap='gray')
            plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

            plt.show()
            self.comboBox_4.setCurrentIndex(0)
    def laplace(self):
            laplace = cv2.Laplacian(img, cv2.CV_64F)

            height, width, channel = laplace.shape
            bytesPerLine = 3 * width
            qImg = QImage(laplace.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_4.setCurrentIndex(0)
    def cannyedge(self):
            edges = cv2.Canny(img, 100, 200)
            plt.subplot(121), plt.imshow(img, cmap='gray')
            plt.title('Original Image'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(edges, cmap='gray')
            plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

            plt.show()
            self.comboBox_4.setCurrentIndex(0)
    def houghline(self):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # img = cv2.imread("lines.png")
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 75, 150)
            lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, maxLineGap=250)
            for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_5.setCurrentIndex(0)
    def houghcircle(self):
            output = img.copy()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # detect circles in the image
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

            # ensure at least some circles were found
            if circles is not None:
                    # convert the (x, y) coordinates and radius of the circles to integers
                    circles = np.round(circles[0, :]).astype("int")

                    # loop over the (x, y) coordinates and radius of the circles
                    for (x, y, r) in circles:
                            # draw the circle in the output image, then draw a rectangle
                            # corresponding to the center of the circle
                            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

                    height, width, channel = output.shape
                    bytesPerLine = 3 * width
                    qImg = QImage(output.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    pixmap = QPixmap(qImg)
                    self.label_3.setPixmap(pixmap)
                    self.comboBox_5.setCurrentIndex(0)

    def contours(self):
            img = cv2.pyrDown(cv2.imread("building.jpg", cv2.IMREAD_UNCHANGED))
            img = cv2.resize(img, (331, 281))

            ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
            image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in contours:
                    # find bounding box coordinates
                    x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # find minimum area
            rect = cv2.minAreaRect(c)
            # calculate coordinates of the minimum area rectangle
            box = cv2.boxPoints(rect)
            # normalize coordinates to integers
            box = np.int0(box)
            # draw contours
            cv2.drawContours(img, [box], 0, (0, 0, 255), 3)
            # calculate center and radius of minimum enclosing circle
            (x, y), radius = cv2.minEnclosingCircle(c)
            # cast to integers
            center = (int(x), int(y))
            radius = int(radius)
            # draw the circle
            img = cv2.circle(img, center, radius, (0, 255, 0), 2)

            cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_5.setCurrentIndex(0)


    def boundingbox(self):
            # read and scale down image
            # wget https://bigsnarf.files.wordpress.com/2017/05/hammer.png
            #path = easygui.fileopenbox()
            #img = cv2.pyrDown(cv2.imread(path, cv2.IMREAD_UNCHANGED))
            #img = cv2.resize(img, (331, 281))
            # threshold image
            ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                                              127, 255, cv2.THRESH_BINARY)
            # find contours and get the external one
            image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE,
                                                     cv2.CHAIN_APPROX_SIMPLE)

            # with each contour, draw boundingRect in green
            # a minAreaRect in red and
            # a minEnclosingCircle in blue
            for c in contours:
                    # get the bounding rect
                    x, y, w, h = cv2.boundingRect(c)
                    # draw a green rectangle to visualize the bounding rect
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    # get the min area rect
                    rect = cv2.minAreaRect(c)
                    box = cv2.boxPoints(rect)
                    # convert all coordinates floating point values to int
                    box = np.int0(box)
                    # draw a red 'nghien' rectangle
                    cv2.drawContours(img, [box], 0, (0, 0, 255))
            cv2.drawContours(img, contours, -1, (255, 255, 0), 1)

            #cv2.imshow("contours", img)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_5.setCurrentIndex(0)

    def enclosecircle(self):
            # read and scale down image
            # wget https://bigsnarf.files.wordpress.com/2017/05/hammer.png
            #path = easygui.fileopenbox()
            #img = cv2.pyrDown(cv2.imread(path, cv2.IMREAD_UNCHANGED))
            #img = cv2.resize(img, (331, 281))
            # threshold image
            img =a
            ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                                              127, 255, cv2.THRESH_BINARY)
            # find contours and get the external one
            image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE,
                                                     cv2.CHAIN_APPROX_SIMPLE)

            # with each contour, draw boundingRect in green
            # a minAreaRect in red and
            # a minEnclosingCircle in blue
            for c in contours:
                      #finally, get the min enclosing circle
                     (x, y), radius = cv2.minEnclosingCircle(c)
                     #convert all values to int
                     center = (int(x), int(y))
                     radius = int(radius)
                    # and draw the circle in blue
                     img = cv2.circle(img, center, radius, (255, 0, 0), 2)

            # print(len(contours))
            cv2.drawContours(img, contours, -1, (255, 255, 0), 1)

            # cv2.imshow("contours", img)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_5.setCurrentIndex(0)

    def harris(self):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            gray = np.float32(gray)
            dst = cv2.cornerHarris(gray, 2, 3, 0.04)

            # result is dilated for marking the corners, not important
            dst = cv2.dilate(dst, None)

            # Threshold for an optimal value, it may vary depending on the image.
            img[dst > 0.01 * dst.max()] = [0, 0, 255]
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_6.setCurrentIndex(0)

    def fast(self):
            fast = cv2.FastFeatureDetector_create()
            # find and draw the keypoints
            kp = fast.detect(img, None)
            img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
            # Print all default params
            #print("Threshold: {}".format(fast.getThreshold()))
            #print("nonmaxSuppression:{}".format(fast.getNonmaxSuppression()))
            #print("neighborhood: {}".format(fast.getType()))
            #print("Total Keypoints with nonmaxSuppression: {}".format(len(kp)))
            # cv.imwrite('fast_true.png',img2)
            # Disable nonmaxSuppression
            fast.setNonmaxSuppression(0)
            kp = fast.detect(img, None)
            #print("Total Keypoints without nonmaxSuppression: {}".format(len(kp)))
            img3 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
            # cv.imwrite('fast_false.png',img3)
            height, width, channel = img2.shape
            bytesPerLine = 3 * width
            qImg = QImage(img2.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_6.setCurrentIndex(0)

    def surf(self):

            # Create SURF object. You can specify params here or later.
            # Here I set Hessian Threshold to 400
            surf = cv2.xfeatures2d.SURF_create(400)
            # Find keypoints and descriptors directly
            # kp, des = surf.detectAndCompute(img,None)
            # len(kp)
            surf.setHessianThreshold(50000)
            # Again compute keypoints and check its number.
            kp, des = surf.detectAndCompute(img, None)
            img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)

            height, width, channel = img2.shape
            bytesPerLine = 3 * width
            qImg = QImage(img2.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_6.setCurrentIndex(0)

    def sift(self):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            sift = cv2.xfeatures2d.SIFT_create()
            kp = sift.detect(gray, None)
            img1 = cv2.drawKeypoints(gray, kp, img)

            height, width, channel = img1.shape
            bytesPerLine = 3 * width
            qImg = QImage(img1.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_6.setCurrentIndex(0)

    def stitching(self):
            path = easygui.fileopenbox()
            img_ = cv2.imread(path)
            img1 = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)

            path = easygui.fileopenbox()
            img = cv2.imread(path)
            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            sift = cv2.xfeatures2d.SIFT_create()
            # find the keypoints and descriptors with SIFT
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)
            # BFMatcher with default params
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1, des2, k=2)

            # print matches
            # Apply ratio test
            good = []

            for m in matches:
                    if m[0].distance < 0.5 * m[1].distance:
                            good.append(m)
            matches = np.asarray(good)

            if len(matches[:, 0]) >= 4:
                    src = np.float32([kp1[m.queryIdx].pt for m in matches[:, 0]]).reshape(-1, 1, 2)
                    dst = np.float32([kp2[m.trainIdx].pt for m in matches[:, 0]]).reshape(-1, 1, 2)

                    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
                    print(H)
            else:
                    raise AssertionError("Can't find enough keypoints.")

            dst = cv2.warpPerspective(img_, H, (img.shape[1] + img_.shape[1], img.shape[0]))
            plt.subplot(122), plt.imshow(dst), plt.title('Warped Image')
            plt.show()
            plt.figure()
            dst[0:img.shape[0], 0:img.shape[1]] = img
            #cv2.imwrite('Saved/resultant_stitched_panorama.jpg', dst)
            #plt.imshow(dst)
            #plt.show()
            #cv2.imwrite('Saved/result.jpg', dst)
            dst = cv2.resize(dst,(331, 281))
            height, width, channel = dst.shape
            bytesPerLine = 3 * width
            qImg = QImage(dst.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_7.setCurrentIndex(0)
    def featurematch(self):
            path = easygui.fileopenbox()
            # img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            # img1 = cv2.imread('',cv2.IMREAD_GRAYSCALE)          # queryImage
            img1 = a
            img2 = cv2.imread(path)  # trainImage
            img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
            # Initiate SIFT detector
            sift = cv2.xfeatures2d.SIFT_create()
            # find the keypoints and descriptors with SIFT
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)
            # FLANN parameters
            FLANN_INDEX_KDTREE = 1
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)  # or pass empty dictionary
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1, des2, k=2)
            # Need to draw only good matches, so create a mask
            matchesMask = [[0, 0] for i in range(len(matches))]
            # ratio test as per Lowe's paper
            for i, (m, n) in enumerate(matches):
                    if m.distance < 0.7 * n.distance:
                            matchesMask[i] = [1, 0]
            draw_params = dict(matchColor=(0, 255, 0),
                               singlePointColor=(255, 0, 0),
                               matchesMask=matchesMask,
                               flags=cv2.DrawMatchesFlags_DEFAULT)
            img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
            img3 = cv2.resize(img3, (331, 281))
            #cv2.imshow("ww",img3)

            height, width, channel = img3.shape
            bytesPerLine = 3 * width
            qImg = QImage(img3.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_7.setCurrentIndex(0)

    def calibration(self):

            # termination criteria
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

            # termination criteria
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

            # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
            objp = np.zeros((6 * 7, 3), np.float32)
            objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

            # Arrays to store object points and image points from all the images.
            objpoints = []  # 3d point in real world space
            imgpoints = []  # 2d points in image plane.

            images = glob.glob('calib_images/*.jpg')

            for fname in images:
                    img = cv2.imread(fname)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    # Find the chess board corners
                    ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

                    # If found, add object points, image points (after refining them)
                    if ret == True:
                            objpoints.append(objp)

                            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                            imgpoints.append(corners2)

                            # Draw and display the corners
                            img = cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
                            cv2.imshow('img', img)
                            cv2.waitKey(500)

            cv2.destroyAllWindows()
            self.comboBox_7.setCurrentIndex(0)

    def epipolar(self):
            global F
            path = easygui.fileopenbox()
            img1 = cv2.imread(path,0)# queryimage # left image
            path = easygui.fileopenbox()
            img2 = cv2.imread(path,0)  # trainimage # right image

            # sift = cv2.SIFT()
            sift = cv2.xfeatures2d.SIFT_create()

            # find the keypoints and descriptors with SIFT
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)

            # FLANN parameters
            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)

            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1, des2, k=2)

            good = []
            pts1 = []
            pts2 = []

            # ratio test as per Lowe's paper
            for i, (m, n) in enumerate(matches):
                    if m.distance < 0.8 * n.distance:
                            good.append(m)
                            pts2.append(kp2[m.trainIdx].pt)
                            pts1.append(kp1[m.queryIdx].pt)
            pts1 = np.int32(pts1)
            pts2 = np.int32(pts2)
            F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_LMEDS)

            # We select only inlier points
            pts1 = pts1[mask.ravel() == 1]
            pts2 = pts2[mask.ravel() == 1]

            def drawlines(img1, img2, lines, pts1, pts2):
                    ''' img1 - image on which we draw the epilines for the points in img2
                        lines - corresponding epilines '''
                    r, c = img1.shape
                    img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
                    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
                    for r, pt1, pt2 in zip(lines, pts1, pts2):
                            color = tuple(np.random.randint(0, 255, 3).tolist())
                            x0, y0 = map(int, [0, -r[2] / r[1]])
                            x1, y1 = map(int, [c, -(r[2] + r[0] * c) / r[1]])
                            img1 = cv2.line(img1, (x0, y0), (x1, y1), color, 1)
                            img1 = cv2.circle(img1, tuple(pt1), 5, color, -1)
                            img2 = cv2.circle(img2, tuple(pt2), 5, color, -1)
                    return img1, img2

            # Find epilines corresponding to points in right image (second image) and
            # drawing its lines on left image
            lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1, 1, 2), 2, F)
            lines1 = lines1.reshape(-1, 3)
            img5, img6 = drawlines(img1, img2, lines1, pts1, pts2)

            # Find epilines corresponding to points in left image (first image) and
            # drawing its lines on right image
            lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1, 1, 2), 1, F)
            lines2 = lines2.reshape(-1, 3)
            img3, img4 = drawlines(img2, img1, lines2, pts2, pts1)
            np.savetxt('fundamental_matrix/Funmat.txt', F, delimiter='    ')
            #f = open('Funndamental_matrix.txt', "a+")
            #f.write("Fundamental matrix using FM_LMEDS\n" )
            #f.close()
            # w = np.loadtxt(q)
            with open('fundamental_matrix/Funmat.txt', 'a') as file:
                    file.write("\n The above values are of Fundamental matrix obtained using Least Median of Squares")
             #       data = file.read().replace(',', '   ')
            #self.textEdit.setText(data)
            os.startfile('fundamental_matrix/Funmat.txt')
            img5 = cv2.resize(img5,(331, 281))
            height, width, channel = img5.shape
            bytesPerLine = 3 * width
            qImg = QImage(img5.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            img3 = cv2.resize(img3, (331, 281))
            height, width, channel = img5.shape
            bytesPerLine = 3 * width
            qImg = QImage(img3.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_2.setPixmap(pixmap)
            self.comboBox_7.setCurrentIndex(0)
            #plt.subplot(121), plt.imshow(img5)
            #plt.subplot(122), plt.imshow(img3)
            #plt.show()
    def sevenpoint(self):
            path = easygui.fileopenbox()
            img1 = cv2.imread(path, 0)  # queryimage # left image
            path = easygui.fileopenbox()
            img2 = cv2.imread(path, 0)  # trainimage # right image

            # sift = cv2.SIFT()
            sift = cv2.xfeatures2d.SIFT_create()

            # find the keypoints and descriptors with SIFT
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)

            # FLANN parameters
            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)

            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1, des2, k=2)

            good = []
            pts1 = []
            pts2 = []

            # ratio test as per Lowe's paper
            for i, (m, n) in enumerate(matches):
                    if m.distance < 0.8 * n.distance:
                            good.append(m)
                            pts2.append(kp2[m.trainIdx].pt)
                            pts1.append(kp1[m.queryIdx].pt)
            pts1 = np.int32(pts1)
            pts2 = np.int32(pts2)
            F2, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_7POINT)
            np.savetxt('fundamental_matrix/7POINT_Funmat.txt', F2, delimiter='    ')
            with open('fundamental_matrix/7POINT_Funmat.txt', 'a') as file:
                    file.write("\n The above values are of Fundamental matrix obtained using 7POINT Algorithm")
            os.startfile('fundamental_matrix/7POINT_Funmat.txt')
            self.comboBox_7.setCurrentIndex(0)

    def eightpoint(self):
            path = easygui.fileopenbox()
            img1 = cv2.imread(path, 0)  # queryimage # left image
            path = easygui.fileopenbox()
            img2 = cv2.imread(path, 0)  # trainimage # right image

            # sift = cv2.SIFT()
            sift = cv2.xfeatures2d.SIFT_create()

            # find the keypoints and descriptors with SIFT
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)

            # FLANN parameters
            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)

            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1, des2, k=2)

            good = []
            pts1 = []
            pts2 = []

            # ratio test as per Lowe's paper
            for i, (m, n) in enumerate(matches):
                    if m.distance < 0.8 * n.distance:
                            good.append(m)
                            pts2.append(kp2[m.trainIdx].pt)
                            pts1.append(kp1[m.queryIdx].pt)
            pts1 = np.int32(pts1)
            pts2 = np.int32(pts2)
            F2, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_8POINT)
            np.savetxt('fundamental_matrix/8POINT_Funmat.txt', F2, delimiter='    ')
            with open('fundamental_matrix/8POINT_Funmat.txt', 'a') as file:
                    file.write("\n The above values are of Fundamental matrix obtained using 8POINT Algorithm")
            os.startfile('fundamental_matrix/8POINT_Funmat.txt')
            self.comboBox_7.setCurrentIndex(0)

    def ransac(self):
            path = easygui.fileopenbox()
            img1 = cv2.imread(path, 0)  # queryimage # left image
            path = easygui.fileopenbox()
            img2 = cv2.imread(path, 0)  # trainimage # right image

            # sift = cv2.SIFT()
            sift = cv2.xfeatures2d.SIFT_create()

            # find the keypoints and descriptors with SIFT
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)

            # FLANN parameters
            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)

            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1, des2, k=2)

            good = []
            pts1 = []
            pts2 = []

            # ratio test as per Lowe's paper
            for i, (m, n) in enumerate(matches):
                    if m.distance < 0.8 * n.distance:
                            good.append(m)
                            pts2.append(kp2[m.trainIdx].pt)
                            pts1.append(kp1[m.queryIdx].pt)
            pts1 = np.int32(pts1)
            pts2 = np.int32(pts2)
            F2, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_8POINT)
            np.savetxt('fundamental_matrix/RANSAC_Funmat.txt', F2, delimiter='    ')
            with open('fundamental_matrix/RANSAC_Funmat.txt', 'a') as file:
                    file.write("\n The above values are of Fundamental matrix obtained using RANSAC Algorithm")
            os.startfile('fundamental_matrix/RANSAC_Funmat.txt')
            self.comboBox_7.setCurrentIndex(0)

    def homography(self):
            MAX_FEATURES = 500
            GOOD_MATCH_PERCENT = 0.15
           #onvert images to grayscale
            #path = easygui.fileopenbox()
            #img1 = cv2.imread(path)
            im1Gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            path = easygui.fileopenbox()
            img2 = cv2.imread(path)
            im2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            # Detect ORB features and compute descriptors.
            orb = cv2.ORB_create(MAX_FEATURES)
            keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
            keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)
            # Match Features
            matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
            matches = matcher.match(descriptors1, descriptors2, None)
            # Sort matches by score
            matches.sort(key=lambda x: x.distance, reverse=False)
            # Remove not so good matches
            numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
            matches = matches[:numGoodMatches]
            # Extract location of good matches
            points1 = np.zeros((len(matches), 2), dtype=np.float32)
            points2 = np.zeros((len(matches), 2), dtype=np.float32)
            for i, match in enumerate(matches):
                    points1[i, :] = keypoints1[match.queryIdx].pt
                    points2[i, :] = keypoints2[match.trainIdx].pt
            # Find homography
            H, mask = cv2.findHomography(points1, points2, cv2.RANSAC)
            global HM
            HM = H
            np.savetxt('fundamental_matrix/homography.txt', H, delimiter='    ')
            with open('fundamental_matrix/homography.txt', 'a') as file:
                    file.write("\n The above values are of Homography ")
            os.startfile('fundamental_matrix/homography.txt')
            self.comboBox_7.setCurrentIndex(0)
    def mosaic(self):
            path = easygui.fileopenbox()
            img1 = cv2.imread(path)
            path = easygui.fileopenbox()
            img2 = cv2.imread(path)
            height, width, channels = img2.shape
            mos = cv2.warpPerspective(img1,HM, (width, height))
            #cv2.imshow('mosaic',mos)
            #plt.imshow('mosaic',mos)
            mos = cv2.resize(mos,(331, 281))
            height1, width1, channel1 = mos.shape
            bytesPerLine = 3 * width1
            qImg = QImage(mos.data, width1, height1, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)
            self.comboBox_7.setCurrentIndex(0)

    def deepfacedetect(self):
            # Define paths
            base_dir = os.path.dirname(__file__)
            prototxt_path = os.path.join(base_dir + 'model_data/deploy.prototxt')
            caffemodel_path = os.path.join(base_dir + 'model_data/weights.caffemodel')

            # Read the model
            model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

            # Create directory 'faces' if it does not exist
            if not os.path.exists('faces'):
                    print("New directory created")
                    os.makedirs('faces')

            # Loop through all images and strip out faces
            # count = 0
            for file in os.listdir(base_dir + 'model_data/images'):
                    file_name, file_extension = os.path.splitext(file)
                    if (file_extension in ['.png', '.jpg']):
                            # image = cv2.imread(base_dir + 'images/' + file)
                            image = img
                            (h, w) = image.shape[:2]
                            blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300),
                                                         (104.0, 177.0, 123.0))

                            model.setInput(blob)
                            detections = model.forward()

                            # Identify each face
                            for i in range(0, detections.shape[2]):
                                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                                    (startX, startY, endX, endY) = box.astype("int")

                                    confidence = detections[0, 0, i, 2]

                                    # If confidence > 0.5, save it as a separate file
                                    if (confidence > 0.5):
                                            cv2.rectangle(image, (startX, startY), (endX, endY), (255, 255, 255), 2)

                            #cv2.imshow("img", image)
                            image = cv2.resize(image,(331, 281))
                            height1, width1, channel1 = image.shape
                            bytesPerLine = 3 * width1
                            qImg = QImage(image.data, width1, height1, bytesPerLine, QImage.Format_RGB888)
                            pixmap = QPixmap(qImg)
                            self.label_3.setPixmap(pixmap)

    def cascade(self):
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
            #img = img
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_color = img[y:y + h, x:x + w]
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            height1, width1, channel1 = img.shape
            bytesPerLine = 3 * width1
            qImg = QImage(img.data, width1, height1, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)

    def recognize(self):

            # load the known faces and embeddings
            #print("[INFO] loading encodings...")
            data = pickle.loads(open("encodings.pickle", "rb").read())

            # load the input image and convert it from BGR to RGB
            image = img
            #image = cv2.imread("example_01.png")
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes corresponding
            # to each face in the input image, then compute the facial embeddings
            # for each face
            #print("[INFO] recognizing faces...")
            print("Please wait ..........")
            print("Recognizing the face ..........")
            boxes = face_recognition.face_locations(rgb, model='cnn')
            encodings = face_recognition.face_encodings(rgb, boxes)

            # initialize the list of names for each face detected
            names = []

            # loop over the facial embeddings
            for encoding in encodings:
                    # attempt to match each face in the input image to our known
                    # encodings
                    matches = face_recognition.compare_faces(data["encodings"],
                                                             encoding)
                    name = "Unknown"

                    # check to see if we have found a match
                    if True in matches:
                            # find the indexes of all matched faces then initialize a
                            # dictionary to count the total number of times each face
                            # was matched
                            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                            counts = {}

                            # loop over the matched indexes and maintain a count for
                            # each recognized face face
                            for i in matchedIdxs:
                                    name = data["names"][i]
                                    counts[name] = counts.get(name, 0) + 1

                            # determine the recognized face with the largest number of
                            # votes (note: in the event of an unlikely tie Python will
                            # select first entry in the dictionary)
                            name = max(counts, key=counts.get)

                    # update the list of names
                    names.append(name)

            # loop over the recognized faces
            for ((top, right, bottom, left), name) in zip(boxes, names):
                    # draw the predicted face name on the image
                    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                                0.75, (0, 255, 0), 2)

            height1, width1, channel1 = image.shape
            bytesPerLine = 3 * width1
            qImg = QImage(image.data, width1, height1, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)


    def detect_face(self, img):
            global faces
            global labels
            # convert the test image to gray image as opencv face detector expects gray images
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # load OpenCV face detector, I am using LBP which is fast
            # there is also a more accurate but slow Haar classifier
            face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

            # let's detect multiscale (some images may be closer to camera than others) images
            # result is a list of faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

            # if no faces are detected then return original img
            if (len(faces) == 0):
                    return None, None

            # under the assumption that there will be only one face,
            # extract the face area
            (x, y, w, h) = faces[0]

            # return only the face part of the image
            return gray[y:y + w, x:x + h], faces[0]

    def prepare_training_data(self, data_folder_path):

            # ------STEP-1--------
            # get the directories (one directory for each subject) in data folder
            dirs = os.listdir(data_folder_path)

            # list to hold all subject faces
            faces = []
            # list to hold labels for all subjects
            labels = []

            # let's go through each directory and read images within it
            for dir_name in dirs:

                    if not dir_name.startswith("s"):
                            continue;

                    # ------STEP-2--------
                    # extract label number of subject from dir_name
                    # format of dir name = slabel
                    # , so removing letter 's' from dir_name will give us label
                    label = int(dir_name.replace("sample", ""))

                    # build path of directory containin images for current subject subject
                    # sample subject_dir_path = "training-data/s1"
                    subject_dir_path = data_folder_path + "/" + dir_name

                    # get the images names that are inside the given subject directory
                    subject_images_names = os.listdir(subject_dir_path)

                    # ------STEP-3--------
                    # go through each image name, read image,
                    # detect face and add face to list of faces
                    for image_name in subject_images_names:

                            # ignore system files like .DS_Store
                            if image_name.startswith("."):
                                    continue;

                            # build image path
                            # sample image path = training-data/s1/1.pgm
                            image_path = subject_dir_path + "/" + image_name

                            # read image
                            image = cv2.imread(image_path)
                            image = cv2.resize(image, (512, 512), interpolation=cv2.INTER_AREA)

                            # display an image window to show the image
                            cv2.imshow("Training in progress", image)
                            cv2.waitKey(100)

                            # detect face
                            face, rect = self.detect_face(image)

                            # ------STEP-4--------
                            # for the purpose of this tutorial
                            # we will ignore faces that are not detected
                            if face is not None:
                                    face = cv2.resize(face, (120, 120), interpolation=cv2.INTER_AREA)
                                    # add face to list of faces
                                    faces.append(face)
                                    # add label for this face
                                    labels.append(label)

            cv2.destroyAllWindows()
            cv2.waitKey(1)
            cv2.destroyAllWindows()

            return faces, labels

    def draw_rectangle(self, img, rect):
            (x, y, w, h) = rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    def draw_text(self, img, text, x, y):
            cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


    def predict(self, test_img):

            # make a copy of the image as we don't want to chang original image
            img = test_img.copy()
            # detect face from the image
            face, rect = self.detect_face(img)
            face = cv2.resize(face, (120, 120), interpolation=cv2.INTER_AREA)

            label = face_recognizer.predict(face)
            #print("Label")
            print(label)
            # get name of respective label returned by face recognizer
            label_text = subjects[label[0]]

            # draw a rectangle around face detected
            self.draw_rectangle(img, rect)
            # draw name of predicted person
            self.draw_text(img, label_text, rect[0], rect[1] - 5)

            return img

    def lbph(self):
            global subjects
            global face_recognizer
            subjects = ["", "Barack_Obama", "Tom_cruise","Sundar_pichai"]
            faces, labels = self.prepare_training_data("training-data")



            # create our LBPH face recognizer
            face_recognizer = cv2.face.LBPHFaceRecognizer_create()

            # train our face recognizer of our training faces
            face_recognizer.train(faces, np.array(labels))
            # load test images
            test_img1 = img

            # perform a prediction
            predicted_img1 = self.predict(test_img1)


            height1, width1, channel1 = predicted_img1.shape
            bytesPerLine = 3 * width1
            qImg = QImage(predicted_img1.data, width1, height1, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)


    def pca(self):
            global subjects
            global face_recognizer
            subjects = ["", "Barack_Obama", "Tom_cruise", "Sundar_pichai"]
            faces, labels = self.prepare_training_data("training-data")

            # create our LBPH face recognizer
            face_recognizer = cv2.face.EigenFaceRecognizer_create()

            # train our face recognizer of our training faces
            face_recognizer.train(faces, np.array(labels))

            # load test images
            test_img1 = img

            # perform a prediction
            predicted_img1 = self.predict(test_img1)
            height1, width1, channel1 = predicted_img1.shape
            bytesPerLine = 3 * width1
            qImg = QImage(predicted_img1.data, width1, height1, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_3.setPixmap(pixmap)


    def process(self,i):

            basic = (self.comboBox_2.currentIndex())
            morphology = (self.comboBox_3.currentIndex())
            filters  =  (self.comboBox_4.currentIndex())
            lines =  (self.comboBox_5.currentIndex())
            feature =  (self.comboBox_6.currentIndex())
            camera =  (self.comboBox_7.currentIndex())
            if basic == 1:
                    self.salt()
            elif basic == 2:
                    self.pepper()
            elif basic == 3:
                    self.addlogo()
            elif basic == 4:
                    self.bgr2rgb()
            elif basic == 5:
                    self.bgr2Ycrcb()
            elif basic == 6:
                    self.bgr2lab()
            elif basic == 7:
                    self.bgr2hsv()
            elif basic == 8 :
                    self.histogram()
            elif basic == 9:
                    self.equalizehist()
            elif morphology == 1:
                    self.dilation()
            elif morphology == 2:
                    self.erode()
            elif morphology == 3:
                    self.close()
            elif morphology == 4:
                    self.open()
            elif filters == 1:
                    self.medianblur()
            elif filters == 2:
                    self.averageblur()
            elif filters == 3:
                    self.gaussianblur()
            elif filters == 4:
                    self.bilateralfilterblur()
            elif filters == 5:
                    self.sobel()
            elif filters == 6:
                    self.laplace()
            elif filters == 7:
                    self.cannyedge()
            elif lines == 1:
                    self.houghline()

            elif lines == 2:
                    self.houghcircle()

            elif lines == 3:
                    self.contours()
            elif lines == 4:
                    self.boundingbox()
            elif lines == 5:
                    self.enclosecircle()

            elif camera == 1:
                    self.calibration()
            elif camera == 2:
                    self.sevenpoint()
            elif camera  ==3:
                    self.eightpoint()
            elif camera == 4:
                    self.ransac()

            elif camera ==5:
                    self.epipolar()
            elif camera == 6:
                    self.homography()
            elif camera == 7:
                    self.mosaic()
            elif camera == 8:
                    self.stitching()
            elif feature == 1:
                    self.harris()
            elif feature == 2:
                    self.fast()
            elif feature == 3:
                    self.surf()
            elif feature == 4:
                    self.sift()
            elif feature ==5:
                    self.featurematch()
            else:
                    pass

            if self.checkBox.isChecked() == True:
                    self.deepfacedetect()
            elif self.checkBox_2.isChecked() ==True:
                    self.cascade()
            elif self.checkBox_3.isChecked()==True:
                    self.recognize()
            elif self.checkBox_4.isChecked()== True:
                    self.lbph()
            elif self.checkBox_5.isChecked() == True:
                    self.pca()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
