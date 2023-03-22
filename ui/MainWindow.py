# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
        MainWindow.resize(819, 576)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_Main = QTabWidget(self.centralwidget)
        self.tabWidget_Main.setObjectName(u"tabWidget_Main")
        self.tab_local = QWidget()
        self.tab_local.setObjectName(u"tab_local")
        self.horizontalLayout = QHBoxLayout(self.tab_local)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_local = QLabel(self.tab_local)
        self.label_local.setObjectName(u"label_local")

        self.verticalLayout_3.addWidget(self.label_local)

        self.listView_loacl = QListView(self.tab_local)
        self.listView_loacl.setObjectName(u"listView_loacl")
        self.listView_loacl.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.listView_loacl)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_R = QPushButton(self.tab_local)
        self.pushButton_R.setObjectName(u"pushButton_R")

        self.verticalLayout_2.addWidget(self.pushButton_R)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_loaded = QLabel(self.tab_local)
        self.label_loaded.setObjectName(u"label_loaded")

        self.verticalLayout_11.addWidget(self.label_loaded)

        self.listView_loaded = QListView(self.tab_local)
        self.listView_loaded.setObjectName(u"listView_loaded")
        self.listView_loaded.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_11.addWidget(self.listView_loaded)


        self.horizontalLayout.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_up = QPushButton(self.tab_local)
        self.pushButton_up.setObjectName(u"pushButton_up")

        self.verticalLayout_12.addWidget(self.pushButton_up)

        self.pushButton_down = QPushButton(self.tab_local)
        self.pushButton_down.setObjectName(u"pushButton_down")

        self.verticalLayout_12.addWidget(self.pushButton_down)

        self.pushButton_add = QPushButton(self.tab_local)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.verticalLayout_12.addWidget(self.pushButton_add)

        self.pushButton_L = QPushButton(self.tab_local)
        self.pushButton_L.setObjectName(u"pushButton_L")

        self.verticalLayout_12.addWidget(self.pushButton_L)


        self.horizontalLayout.addLayout(self.verticalLayout_12)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_nowpath = QLabel(self.tab_local)
        self.label_nowpath.setObjectName(u"label_nowpath")

        self.horizontalLayout_6.addWidget(self.label_nowpath)

        self.lineEdit_nowpath = QLineEdit(self.tab_local)
        self.lineEdit_nowpath.setObjectName(u"lineEdit_nowpath")
        self.lineEdit_nowpath.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_nowpath)

        self.pushButton_nowpath = QPushButton(self.tab_local)
        self.pushButton_nowpath.setObjectName(u"pushButton_nowpath")

        self.horizontalLayout_6.addWidget(self.pushButton_nowpath)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.comboBox_mods = QComboBox(self.tab_local)
        self.comboBox_mods.setObjectName(u"comboBox_mods")

        self.verticalLayout_4.addWidget(self.comboBox_mods)

        self.label_nowdir = QLabel(self.tab_local)
        self.label_nowdir.setObjectName(u"label_nowdir")

        self.verticalLayout_4.addWidget(self.label_nowdir)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_save = QPushButton(self.tab_local)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.verticalLayout_4.addWidget(self.pushButton_save)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.tabWidget_Main.addTab(self.tab_local, "")
        self.tab_Network = QWidget()
        self.tab_Network.setObjectName(u"tab_Network")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_Network)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listView_Network = QListView(self.tab_Network)
        self.listView_Network.setObjectName(u"listView_Network")
        self.listView_Network.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalLayout_2.addWidget(self.listView_Network)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.pushButton_refresh = QPushButton(self.tab_Network)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.verticalLayout_7.addWidget(self.pushButton_refresh)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_name = QLabel(self.tab_Network)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout_6.addWidget(self.label_name)

        self.label_author = QLabel(self.tab_Network)
        self.label_author.setObjectName(u"label_author")

        self.verticalLayout_6.addWidget(self.label_author)

        self.label_version = QLabel(self.tab_Network)
        self.label_version.setObjectName(u"label_version")

        self.verticalLayout_6.addWidget(self.label_version)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_introduce = QLabel(self.tab_Network)
        self.label_introduce.setObjectName(u"label_introduce")

        self.horizontalLayout_3.addWidget(self.label_introduce)

        self.plainTextEdit_introduce = QPlainTextEdit(self.tab_Network)
        self.plainTextEdit_introduce.setObjectName(u"plainTextEdit_introduce")
        self.plainTextEdit_introduce.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.horizontalLayout_3.addWidget(self.plainTextEdit_introduce)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.line = QFrame(self.tab_Network)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_savedir = QLabel(self.tab_Network)
        self.label_savedir.setObjectName(u"label_savedir")

        self.horizontalLayout_4.addWidget(self.label_savedir)

        self.lineEdit_savedir = QLineEdit(self.tab_Network)
        self.lineEdit_savedir.setObjectName(u"lineEdit_savedir")
        self.lineEdit_savedir.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_savedir)

        self.pushButton_savedir = QPushButton(self.tab_Network)
        self.pushButton_savedir.setObjectName(u"pushButton_savedir")

        self.horizontalLayout_4.addWidget(self.pushButton_savedir)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_source = QLabel(self.tab_Network)
        self.label_source.setObjectName(u"label_source")

        self.horizontalLayout_7.addWidget(self.label_source)

        self.comboBox_download = QComboBox(self.tab_Network)
        self.comboBox_download.setObjectName(u"comboBox_download")

        self.horizontalLayout_7.addWidget(self.comboBox_download)

        self.horizontalLayout_7.setStretch(1, 10)

        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.progressBar_Download = QProgressBar(self.tab_Network)
        self.progressBar_Download.setObjectName(u"progressBar_Download")
        self.progressBar_Download.setValue(0)

        self.verticalLayout_8.addWidget(self.progressBar_Download)

        self.pushButton_Download = QPushButton(self.tab_Network)
        self.pushButton_Download.setObjectName(u"pushButton_Download")

        self.verticalLayout_8.addWidget(self.pushButton_Download)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.tabWidget_Main.addTab(self.tab_Network, "")
        self.tab_about = QWidget()
        self.tab_about.setObjectName(u"tab_about")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_about)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_about_author = QLabel(self.tab_about)
        self.label_about_author.setObjectName(u"label_about_author")

        self.verticalLayout_9.addWidget(self.label_about_author)

        self.label_about_contact = QLabel(self.tab_about)
        self.label_about_contact.setObjectName(u"label_about_contact")

        self.verticalLayout_9.addWidget(self.label_about_contact)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)

        self.line_2 = QFrame(self.tab_about)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_about_verison = QLabel(self.tab_about)
        self.label_about_verison.setObjectName(u"label_about_verison")

        self.verticalLayout_10.addWidget(self.label_about_verison)

        self.label_about_newverison = QLabel(self.tab_about)
        self.label_about_newverison.setObjectName(u"label_about_newverison")

        self.verticalLayout_10.addWidget(self.label_about_newverison)

        self.pushButton_release = QPushButton(self.tab_about)
        self.pushButton_release.setObjectName(u"pushButton_release")

        self.verticalLayout_10.addWidget(self.pushButton_release)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.tabWidget_Main.addTab(self.tab_about, "")

        self.verticalLayout.addWidget(self.tabWidget_Main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget_Main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RA3\u9644\u5c5emod\u4e0b\u8f7d\u5668", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_local.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6587\u4ef6\u5939\u4e0b\u7684big\u6587\u4ef6", None))
        self.pushButton_R.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.label_loaded.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u52a0\u8f7d\u7684\u6587\u4ef6", None))
        self.pushButton_up.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.pushButton_down.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_nowpath.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u76ee\u5f55:", None))
        self.pushButton_nowpath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_nowdir.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6587\u4ef6\u5939:", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab_local), QCoreApplication.translate("MainWindow", u"\u672c\u5730", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0:", None))
        self.label_author.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005:", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c:", None))
        self.label_introduce.setText(QCoreApplication.translate("MainWindow", u"\u4ecb\u7ecd:", None))
        self.label_savedir.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5230:", None))
        self.pushButton_savedir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_source.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6e90:", None))
        self.pushButton_Download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab_Network), QCoreApplication.translate("MainWindow", u"\u7f51\u7edc", None))
        self.label_about_author.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005:\u7530\u9f20-Hatanezumi", None))
        self.label_about_contact.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb:Hatanezumi@chunshengserver.cn", None))
        self.label_about_verison.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7248\u672c:", None))
        self.label_about_newverison.setText(QCoreApplication.translate("MainWindow", u"\u6700\u65b0\u7248\u672c:", None))
        self.pushButton_release.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u5e03\u9875", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab_about), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#if QT_CONFIG(statustip)
        self.statusBar.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.statusBar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.statusBar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

