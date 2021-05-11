# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(297, 387)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0); \n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_content)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame_content)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBox_filetype = QComboBox(self.frame_content)
        self.comboBox_filetype.addItem("")
        self.comboBox_filetype.addItem("")
        self.comboBox_filetype.setObjectName(u"comboBox_filetype")
        self.comboBox_filetype.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_filetype)

        self.label_3 = QLabel(self.frame_content)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.comboBox_delimiter = QComboBox(self.frame_content)
        self.comboBox_delimiter.addItem("")
        self.comboBox_delimiter.addItem("")
        self.comboBox_delimiter.addItem("")
        self.comboBox_delimiter.addItem("")
        self.comboBox_delimiter.setObjectName(u"comboBox_delimiter")
        self.comboBox_delimiter.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_delimiter)

        self.pushButton_convertFiles = QPushButton(self.frame_content)
        self.pushButton_convertFiles.setObjectName(u"pushButton_convertFiles")
        self.pushButton_convertFiles.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_convertFiles.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.pushButton_convertFiles)

        self.label_errors = QLabel(self.frame_content)
        self.label_errors.setObjectName(u"label_errors")
        self.label_errors.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_errors.setAlignment(Qt.AlignCenter)
        self.label_errors.setWordWrap(False)
        self.label_errors.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_errors)

        self.label_results = QLabel(self.frame_content)
        self.label_results.setObjectName(u"label_results")
        self.label_results.setWordWrap(False)
        self.label_results.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_results)


        self.verticalLayout.addWidget(self.frame_content)

        self.progressBar_mainProgress = QProgressBar(self.centralwidget)
        self.progressBar_mainProgress.setObjectName(u"progressBar_mainProgress")
        self.progressBar_mainProgress.setValue(0)
        self.progressBar_mainProgress.setOrientation(Qt.Horizontal)
        self.progressBar_mainProgress.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar_mainProgress)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 297, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"File Converter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Filetype", None))
        self.comboBox_filetype.setItemText(0, QCoreApplication.translate("MainWindow", u"csv", None))
        self.comboBox_filetype.setItemText(1, QCoreApplication.translate("MainWindow", u"txt", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Delimiter", None))
        self.comboBox_delimiter.setItemText(0, QCoreApplication.translate("MainWindow", u",", None))
        self.comboBox_delimiter.setItemText(1, QCoreApplication.translate("MainWindow", u";", None))
        self.comboBox_delimiter.setItemText(2, QCoreApplication.translate("MainWindow", u"Tabulator", None))
        self.comboBox_delimiter.setItemText(3, QCoreApplication.translate("MainWindow", u"Leerzeichen", None))

        self.pushButton_convertFiles.setText(QCoreApplication.translate("MainWindow", u"convert Files to XLSX", None))
        self.label_errors.setText("")
        self.label_results.setText("")
    # retranslateUi

