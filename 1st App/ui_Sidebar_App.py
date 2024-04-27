# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sidebar_App.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# Import the generated resource module
import ui_Resources_rc

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import ui_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1338, 856)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Icon_Widget = QWidget(self.centralwidget)
        self.Icon_Widget.setObjectName(u"Icon_Widget")
        self.Icon_Widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 156, 233);\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	height:50px;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color:#f5fafe;\n"
"	color:#1f95ef;\n"
"	font-weight:bold;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.Icon_Widget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.Icon_Widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 60))
        self.label.setMaximumSize(QSize(65, 80))
        self.label.setPixmap(QPixmap("F:/Users/Strix/Desktop/SideMenu/images/profile 2white.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(13)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Dashboard_S = QPushButton(self.Icon_Widget)
        self.Dashboard_S.setObjectName(u"Dashboard_S")
        icon = QIcon()
        icon.addFile(u":/images/dashboard white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/dashboard Blue.png", QSize(), QIcon.Normal, QIcon.On)
        self.Dashboard_S.setIcon(icon)
        self.Dashboard_S.setCheckable(True)
        self.Dashboard_S.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Dashboard_S)

        self.Profile_S = QPushButton(self.Icon_Widget)
        self.Profile_S.setObjectName(u"Profile_S")
        icon1 = QIcon()
        icon1.addFile(u":/images/user (white).png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/user (blue).png", QSize(), QIcon.Normal, QIcon.On)
        self.Profile_S.setIcon(icon1)
        self.Profile_S.setCheckable(True)
        self.Profile_S.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Profile_S)

        self.Messages_S = QPushButton(self.Icon_Widget)
        self.Messages_S.setObjectName(u"Messages_S")
        icon2 = QIcon()
        icon2.addFile(u":/images/comments white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/comments.png", QSize(), QIcon.Normal, QIcon.On)
        self.Messages_S.setIcon(icon2)
        self.Messages_S.setCheckable(True)
        self.Messages_S.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Messages_S)

        self.Notifications_S = QPushButton(self.Icon_Widget)
        self.Notifications_S.setObjectName(u"Notifications_S")
        icon3 = QIcon()
        icon3.addFile(u":/images/Notification white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/Notification Blue.png", QSize(), QIcon.Normal, QIcon.On)
        self.Notifications_S.setIcon(icon3)
        self.Notifications_S.setCheckable(True)
        self.Notifications_S.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Notifications_S)

        self.Settings_S = QPushButton(self.Icon_Widget)
        self.Settings_S.setObjectName(u"Settings_S")
        icon4 = QIcon()
        icon4.addFile(u":/images/Setting white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/Setting Blue.png", QSize(), QIcon.Normal, QIcon.On)
        self.Settings_S.setIcon(icon4)
        self.Settings_S.setCheckable(True)
        self.Settings_S.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Settings_S)

        self.verticalSpacer = QSpacerItem(20, 548, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.SignOut_S = QPushButton(self.Icon_Widget)
        self.SignOut_S.setObjectName(u"SignOut_S")
        icon5 = QIcon()
        icon5.addFile(u":/images/power white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SignOut_S.setIcon(icon5)
        self.SignOut_S.setCheckable(True)

        self.verticalLayout_2.addWidget(self.SignOut_S)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.Icon_Widget, 0, 0, 1, 1)

        self.Icon_Name_Widget = QWidget(self.centralwidget)
        self.Icon_Name_Widget.setObjectName(u"Icon_Name_Widget")
        self.Icon_Name_Widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 156, 233);\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:None;\n"
"	padding:8px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:Checked{\n"
"	background-color:#f5fafe;\n"
"	color:#1f95ef;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.Icon_Name_Widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.Icon_Name_Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(75, 75))
        self.label_2.setMaximumSize(QSize(75, 75))
        self.label_2.setPixmap(QPixmap(u":/images/profile 2white.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(2)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.Icon_Name_Widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold Condensed"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:White")
        self.label_3.setMargin(4)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Dashboard_B = QPushButton(self.Icon_Name_Widget)
        self.Dashboard_B.setObjectName(u"Dashboard_B")
        self.Dashboard_B.setIcon(icon)
        self.Dashboard_B.setCheckable(True)
        self.Dashboard_B.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Dashboard_B)

        self.Profile_B = QPushButton(self.Icon_Name_Widget)
        self.Profile_B.setObjectName(u"Profile_B")
        self.Profile_B.setIcon(icon1)
        self.Profile_B.setCheckable(True)
        self.Profile_B.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Profile_B)

        self.Messages_B = QPushButton(self.Icon_Name_Widget)
        self.Messages_B.setObjectName(u"Messages_B")
        self.Messages_B.setIcon(icon2)
        self.Messages_B.setCheckable(True)
        self.Messages_B.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Messages_B)

        self.Notifications_B = QPushButton(self.Icon_Name_Widget)
        self.Notifications_B.setObjectName(u"Notifications_B")
        self.Notifications_B.setIcon(icon3)
        self.Notifications_B.setCheckable(True)
        self.Notifications_B.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Notifications_B)

        self.Settings_B = QPushButton(self.Icon_Name_Widget)
        self.Settings_B.setObjectName(u"Settings_B")
        self.Settings_B.setIcon(icon4)
        self.Settings_B.setCheckable(True)
        self.Settings_B.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Settings_B)

        self.verticalSpacer_2 = QSpacerItem(20, 548, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.SignOut_B = QPushButton(self.Icon_Name_Widget)
        self.SignOut_B.setObjectName(u"SignOut_B")
        icon6 = QIcon()
        icon6.addFile(u":/images/power white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/images/power blue.png", QSize(), QIcon.Normal, QIcon.On)
        self.SignOut_B.setIcon(icon6)
        self.SignOut_B.setCheckable(True)

        self.verticalLayout.addWidget(self.SignOut_B)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.Icon_Name_Widget, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Header = QWidget(self.widget_3)
        self.Header.setObjectName(u"Header")
        self.horizontalLayout_5 = QHBoxLayout(self.Header)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Menu = QPushButton(self.Header)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/images/menu-bar blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon7)
        self.Menu.setIconSize(QSize(30, 30))
        self.Menu.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.Menu)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.lineEdit = QLineEdit(self.Header)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Search = QPushButton(self.Header)
        self.Search.setObjectName(u"Search")
        self.Search.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/images/Search Icon Blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Search.setIcon(icon8)
        self.Search.setIconSize(QSize(100, 20))

        self.horizontalLayout.addWidget(self.Search)

        self.Profile = QPushButton(self.Header)
        self.Profile.setObjectName(u"Profile")
        self.Profile.setStyleSheet(u"border:none;")
        icon9 = QIcon()
        icon9.addFile(u":/images/user (blue).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile.setIcon(icon9)
        self.Profile.setIconSize(QSize(30, 20))

        self.horizontalLayout.addWidget(self.Profile)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.Header)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.Dashboard_Page = QWidget()
        self.Dashboard_Page.setObjectName(u"Dashboard_Page")
        self.Dashboard_Page.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.Dashboard_Page)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.Dashboard_Page)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.Dashboard_Page)
        self.Profile_Page = QWidget()
        self.Profile_Page.setObjectName(u"Profile_Page")
        self.horizontalLayout_8 = QHBoxLayout(self.Profile_Page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.Profile_Page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.Profile_Page)
        self.Messages_Page = QWidget()
        self.Messages_Page.setObjectName(u"Messages_Page")
        self.horizontalLayout_9 = QHBoxLayout(self.Messages_Page)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.Messages_Page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.Messages_Page)
        self.Notifications_Page = QWidget()
        self.Notifications_Page.setObjectName(u"Notifications_Page")
        self.verticalLayout_6 = QVBoxLayout(self.Notifications_Page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.Notifications_Page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.verticalLayout_6.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.Notifications_Page)
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.horizontalLayout_6 = QHBoxLayout(self.Settings_Page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.Settings_Page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.stackedWidget.addWidget(self.Settings_Page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Menu.toggled.connect(self.Icon_Widget.setHidden)
        self.Menu.toggled.connect(self.Icon_Name_Widget.setVisible)
        self.Settings_S.toggled.connect(self.Settings_B.setChecked)
        self.Notifications_S.toggled.connect(self.Notifications_B.setChecked)
        self.Messages_S.toggled.connect(self.Messages_B.setChecked)
        self.Profile_S.toggled.connect(self.Profile_B.setChecked)
        self.Dashboard_S.toggled.connect(self.Dashboard_B.setChecked)
        self.SignOut_S.toggled.connect(self.SignOut_B.setChecked)
        self.Dashboard_B.toggled.connect(self.Dashboard_S.setChecked)
        self.Profile_B.toggled.connect(self.Profile_S.setChecked)
        self.Messages_B.toggled.connect(self.Messages_S.setChecked)
        self.Notifications_B.toggled.connect(self.Notifications_S.setChecked)
        self.Settings_B.toggled.connect(self.Settings_S.setChecked)
        self.SignOut_B.toggled.connect(self.SignOut_S.setChecked)
        self.SignOut_B.toggled.connect(MainWindow.close)
        self.SignOut_S.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.Dashboard_S.setText("")
        self.Profile_S.setText("")
        self.Messages_S.setText("")
        self.Notifications_S.setText("")
        self.Settings_S.setText("")
        self.SignOut_S.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Side Bar", None))
        self.Dashboard_B.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.Profile_B.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.Messages_B.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.Notifications_B.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.Settings_B.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.SignOut_B.setText(QCoreApplication.translate("MainWindow", u"SignOut", None))
        self.Menu.setText("")
        self.Search.setText("")
        self.Profile.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    retranslateUi

