# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 764)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 764))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setMinimumSize(QtCore.QSize(960, 122))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.plateDecodedFrame = QtWidgets.QFrame(self.frame_5)
        self.plateDecodedFrame.setMinimumSize(QtCore.QSize(260, 56))
        self.plateDecodedFrame.setSizeIncrement(QtCore.QSize(16, 9))
        self.plateDecodedFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plateDecodedFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plateDecodedFrame.setObjectName("plateDecodedFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.plateDecodedFrame)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.plateDecodedLabel = QtWidgets.QLabel(self.plateDecodedFrame)
        self.plateDecodedLabel.setObjectName("plateDecodedLabel")
        self.gridLayout_5.addWidget(self.plateDecodedLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.plateDecodedFrame, 1, 0, 1, 1)
        self.plateFrame = QtWidgets.QFrame(self.frame_5)
        self.plateFrame.setMinimumSize(QtCore.QSize(260, 56))
        self.plateFrame.setSizeIncrement(QtCore.QSize(16, 9))
        self.plateFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plateFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plateFrame.setObjectName("plateFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.plateFrame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plateView = QtWidgets.QLabel(self.plateFrame)
        self.plateView.setObjectName("plateView")
        self.gridLayout_4.addWidget(self.plateView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.plateFrame, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setMinimumSize(QtCore.QSize(690, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 2, 2, 1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 0, 1, 2, 1)
        self.gridLayout_2.addWidget(self.frame_5, 3, 0, 1, 1)
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setMinimumSize(QtCore.QSize(960, 520))
        self.mainFrame.setSizeIncrement(QtCore.QSize(16, 9))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.mainFrame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mainView = QtWidgets.QLabel(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainView.sizePolicy().hasHeightForWidth())
        self.mainView.setSizePolicy(sizePolicy)
        self.mainView.setSizeIncrement(QtCore.QSize(16, 9))
        self.mainView.setAlignment(QtCore.Qt.AlignCenter)
        self.mainView.setObjectName("mainView")
        self.gridLayout_3.addWidget(self.mainView, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.mainFrame, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setMinimumSize(QtCore.QSize(960, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout_2.addWidget(self.frame_6, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 6, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuSettings.addAction(self.actionOpen)
        self.menuSettings.addAction(self.actionSettings)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plateDecodedLabel.setText(_translate("MainWindow", "TextLabel"))
        self.plateView.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Classification model: YOLO8n-200e"))
        self.label_2.setText(_translate("MainWindow", "Detection model: YOLO8s-100e"))
        self.label_5.setText(_translate("MainWindow", "Classifiation accuracy:\n"
"O - 70%\n"
"7 - 66%\n"
"6 - 52%\n"
"9 - 97%\n"
"D - 84%\n"
"T - 90%"))
        self.label.setText(_translate("MainWindow", "Elapsed time: 10ms"))
        self.label_4.setText(_translate("MainWindow", "Detection accuracy: 80%"))
        self.mainView.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.menuSettings.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))