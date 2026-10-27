# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'boardTestApplicationbrbBBB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1824, 1118)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: black;  /* Text color set to white for contrast */\n"
"}\n"
"\n"
"QComboBox{\n"
"    color: white;  /* Text color set to white */\n"
"    background-color: black;  /* Black background */\n"
"}\n"
"\n"
"QComboBox::item{\n"
"    color: white;  /* White text for dropdown items */\n"
"    background-color: black;  /* Black background for items */\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: black;  /* Black text on buttons */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;  /* Optional: a lighter gray on hover */\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.heade_frame = QFrame(self.centralwidget)
        self.heade_frame.setObjectName(u"heade_frame")
        self.heade_frame.setEnabled(True)
        self.heade_frame.setStyleSheet(u"background-color: rgb(255, 150, 0);")
        self.heade_frame.setFrameShape(QFrame.NoFrame)
        self.heade_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.heade_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.heade_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.header_left_frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.open_close_side_bar_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/bootstrap_icons/menu-button-wide-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame)

        self.header_center_frame = QFrame(self.heade_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.header_center_frame)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/bootstrap_icons/display.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.pushButton, 0, Qt.AlignRight)

        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.heade_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.min_window_button = QPushButton(self.header_right_frame)
        self.min_window_button.setObjectName(u"min_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/bootstrap_icons/dash-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min_window_button.setIcon(icon2)
        self.min_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.min_window_button)

        self.max_window_button = QPushButton(self.header_right_frame)
        self.max_window_button.setObjectName(u"max_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/bootstrap_icons/arrows-fullscreen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.max_window_button.setIcon(icon3)
        self.max_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.max_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/bootstrap_icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon4)
        self.close_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.heade_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.left_menu_frame = QFrame(self.main_body_frame)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setMinimumSize(QSize(50, 0))
        self.left_menu_frame.setMaximumSize(QSize(50, 16777215))
        self.left_menu_frame.setStyleSheet(u"background-color: rgb(255, 150, 0);")
        self.left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.menu_frame = QFrame(self.left_menu_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(0, 10, 200, 461))
        self.menu_frame.setMinimumSize(QSize(200, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.encoder_bnt = QPushButton(self.menu_frame)
        self.encoder_bnt.setObjectName(u"encoder_bnt")
        self.encoder_bnt.setGeometry(QRect(0, 0, 36, 32))
        icon5 = QIcon()
        icon5.addFile(u":/icons/bootstrap_icons/music-note-list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.encoder_bnt.setIcon(icon5)
        self.encoder_bnt.setIconSize(QSize(32, 32))
        self.label_3 = QLabel(self.menu_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(67, 0, 91, 32))
        self.label_3.setFont(font)
        self.label_3.setMargin(5)
        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(63, 80, 81, 41))
        self.label_4.setFont(font)
        self.label_4.setMargin(5)
        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(87, 100, 70, 30))
        self.label_5.setMargin(5)
        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(87, 150, 62, 30))
        self.label_7.setMargin(5)
        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(87, 250, 113, 30))
        self.label_9.setMargin(5)
        self.label_32 = QLabel(self.menu_frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(87, 200, 63, 20))
        self.sys_btn = QPushButton(self.menu_frame)
        self.sys_btn.setObjectName(u"sys_btn")
        self.sys_btn.setGeometry(QRect(0, 80, 36, 32))
        icon6 = QIcon()
        icon6.addFile(u":/icons/bootstrap_icons/gear-wide-connected.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sys_btn.setIcon(icon6)
        self.sys_btn.setIconSize(QSize(32, 32))
        self.label_40 = QLabel(self.menu_frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(87, 300, 113, 30))
        self.label_40.setMargin(5)
        self.label_2 = QLabel(self.left_menu_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(8, 830, 41, 31))

        self.horizontalLayout_8.addWidget(self.left_menu_frame)

        self.centre_menu_frame = QFrame(self.main_body_frame)
        self.centre_menu_frame.setObjectName(u"centre_menu_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centre_menu_frame.sizePolicy().hasHeightForWidth())
        self.centre_menu_frame.setSizePolicy(sizePolicy1)
        self.centre_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.centre_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.centre_menu_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centre_menu_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setWeight(50)
        self.stackedWidget.setFont(font2)
        self.cmemory = QWidget()
        self.cmemory.setObjectName(u"cmemory")
        self.lineEdit_mintresh = QLineEdit(self.cmemory)
        self.lineEdit_mintresh.setObjectName(u"lineEdit_mintresh")
        self.lineEdit_mintresh.setEnabled(False)
        self.lineEdit_mintresh.setGeometry(QRect(1400, 280, 121, 20))
        self.lineEdit_maxtresh = QLineEdit(self.cmemory)
        self.lineEdit_maxtresh.setObjectName(u"lineEdit_maxtresh")
        self.lineEdit_maxtresh.setEnabled(False)
        self.lineEdit_maxtresh.setGeometry(QRect(1400, 240, 121, 20))
        self.newdevice = QPushButton(self.cmemory)
        self.newdevice.setObjectName(u"newdevice")
        self.newdevice.setGeometry(QRect(700, 490, 331, 51))
        self.newdevice.setStyleSheet(u"QPushButton {\n"
"                                    height: 50px;\n"
"                                    width: 200px;\n"
"                                    background-color: transparent;\n"
"                                    border: 2px solid #252525;\n"
"                                    border-radius: 25px;\n"
"                                    color: #333;\n"
"                                    font-weight: 800;\n"
"                                    letter-spacing: 3px;\n"
"                                    transition: all 200ms ease-in-out;\n"
"                                }\n"
"                                \n"
"                                QPushButton:hover {\n"
"                                    background-color: #333;\n"
"                                    color: white;\n"
"                                    border: none;\n"
"                                }\n"
"                                \n"
"                                QPushButton:pressed {\n"
"                 "
                        "                   background-color: #555;\n"
"                                    color: #fff;\n"
"                                    transform: scale(0.97);\n"
"                                }")
        self.ram_info_widget_3 = QWidget(self.cmemory)
        self.ram_info_widget_3.setObjectName(u"ram_info_widget_3")
        self.ram_info_widget_3.setGeometry(QRect(0, 550, 1690, 195))
        self.ram_info_widget_3.setStyleSheet(u"")
        self.d5_3 = QPushButton(self.ram_info_widget_3)
        self.d5_3.setObjectName(u"d5_3")
        self.d5_3.setGeometry(QRect(1460, 10, 31, 181))
        self.d5_3.setStyleSheet(u"#d5_3{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#d5_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d5_3.setCheckable(True)
        self.d40_13 = QPushButton(self.ram_info_widget_3)
        self.d40_13.setObjectName(u"d40_13")
        self.d40_13.setGeometry(QRect(1270, 10, 21, 111))
        self.d40_13.setStyleSheet(u"#d40_13{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_13:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.d40_13.setCheckable(True)
        self.a4_15 = QPushButton(self.ram_info_widget_3)
        self.a4_15.setObjectName(u"a4_15")
        self.a4_15.setGeometry(QRect(1370, 10, 31, 181))
        self.a4_15.setStyleSheet(u"#a4_15{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#a4_15:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a4_15.setCheckable(True)
        self.f40_13 = QPushButton(self.ram_info_widget_3)
        self.f40_13.setObjectName(u"f40_13")
        self.f40_13.setGeometry(QRect(1330, 10, 21, 111))
        self.f40_13.setStyleSheet(u"#f40_13{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_13:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.f40_13.setCheckable(True)
        self.f50_3 = QPushButton(self.ram_info_widget_3)
        self.f50_3.setObjectName(u"f50_3")
        self.f50_3.setGeometry(QRect(1540, 10, 21, 111))
        self.f50_3.setStyleSheet(u"#f50_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f50_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.f50_3.setCheckable(True)
        self.a5_3 = QPushButton(self.ram_info_widget_3)
        self.a5_3.setObjectName(u"a5_3")
        self.a5_3.setGeometry(QRect(1580, 10, 31, 181))
        self.a5_3.setStyleSheet(u"#a5_3{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#a5_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a5_3.setCheckable(True)
        self.d50_3 = QPushButton(self.ram_info_widget_3)
        self.d50_3.setObjectName(u"d50_3")
        self.d50_3.setGeometry(QRect(1480, 10, 21, 111))
        self.d50_3.setStyleSheet(u"#d50_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d50_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.d50_3.setCheckable(True)
        self.e5_3 = QPushButton(self.ram_info_widget_3)
        self.e5_3.setObjectName(u"e5_3")
        self.e5_3.setGeometry(QRect(1490, 10, 31, 181))
        self.e5_3.setStyleSheet(u"#e5_3{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#e5_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e5_3.setCheckable(True)
        self.c5_3 = QPushButton(self.ram_info_widget_3)
        self.c5_3.setObjectName(u"c5_3")
        self.c5_3.setGeometry(QRect(1430, 10, 31, 181))
        self.c5_3.setStyleSheet(u"#c5_3{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#c5_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c5_3.setCheckable(True)
        self.g4_13 = QPushButton(self.ram_info_widget_3)
        self.g4_13.setObjectName(u"g4_13")
        self.g4_13.setGeometry(QRect(1340, 10, 31, 181))
        self.g4_13.setStyleSheet(u"#g4_13{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#g4_13:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_13.setCheckable(True)
        self.g50_3 = QPushButton(self.ram_info_widget_3)
        self.g50_3.setObjectName(u"g50_3")
        self.g50_3.setGeometry(QRect(1570, 10, 21, 111))
        self.g50_3.setStyleSheet(u"#g50_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g50_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.g50_3.setCheckable(True)
        self.c40_13 = QPushButton(self.ram_info_widget_3)
        self.c40_13.setObjectName(u"c40_13")
        self.c40_13.setGeometry(QRect(1240, 10, 21, 111))
        self.c40_13.setStyleSheet(u"#c40_13{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_13:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c40_13.setCheckable(True)
        self.b4_15 = QPushButton(self.ram_info_widget_3)
        self.b4_15.setObjectName(u"b4_15")
        self.b4_15.setGeometry(QRect(1400, 10, 31, 181))
        self.b4_15.setStyleSheet(u"#b4_15{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#b4_15:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_15.setCheckable(True)
        self.c4_13 = QPushButton(self.ram_info_widget_3)
        self.c4_13.setObjectName(u"c4_13")
        self.c4_13.setGeometry(QRect(1220, 10, 31, 181))
        self.c4_13.setStyleSheet(u"#c4_13{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#c4_13:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c4_13.setCheckable(True)
        self.g5_3 = QPushButton(self.ram_info_widget_3)
        self.g5_3.setObjectName(u"g5_3")
        self.g5_3.setGeometry(QRect(1550, 10, 31, 181))
        self.g5_3.setStyleSheet(u"#g5_3{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#g5_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g5_3.setCheckable(True)
        self.d4_13 = QPushButton(self.ram_info_widget_3)
        self.d4_13.setObjectName(u"d4_13")
        self.d4_13.setGeometry(QRect(1250, 10, 31, 181))
        self.d4_13.setStyleSheet(u"#d4_13{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#d4_13:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_13.setCheckable(True)
        self.a40_15 = QPushButton(self.ram_info_widget_3)
        self.a40_15.setObjectName(u"a40_15")
        self.a40_15.setGeometry(QRect(1390, 10, 21, 111))
        self.a40_15.setStyleSheet(u"#a40_15{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_15:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.a40_15.setCheckable(True)
        self.e4_13 = QPushButton(self.ram_info_widget_3)
        self.e4_13.setObjectName(u"e4_13")
        self.e4_13.setGeometry(QRect(1280, 10, 31, 181))
        self.e4_13.setStyleSheet(u"#e4_13{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#e4_13:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_13.setCheckable(True)
        self.f5_3 = QPushButton(self.ram_info_widget_3)
        self.f5_3.setObjectName(u"f5_3")
        self.f5_3.setGeometry(QRect(1520, 10, 31, 181))
        self.f5_3.setStyleSheet(u"#f5_3{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#f5_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f5_3.setCheckable(True)
        self.a50_3 = QPushButton(self.ram_info_widget_3)
        self.a50_3.setObjectName(u"a50_3")
        self.a50_3.setGeometry(QRect(1600, 10, 21, 111))
        self.a50_3.setStyleSheet(u"#a50_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a50_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.a50_3.setCheckable(True)
        self.c50_3 = QPushButton(self.ram_info_widget_3)
        self.c50_3.setObjectName(u"c50_3")
        self.c50_3.setGeometry(QRect(1450, 10, 21, 111))
        self.c50_3.setStyleSheet(u"#c50_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c50_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.c50_3.setCheckable(True)
        self.b5_3 = QPushButton(self.ram_info_widget_3)
        self.b5_3.setObjectName(u"b5_3")
        self.b5_3.setGeometry(QRect(1610, 10, 31, 181))
        self.b5_3.setStyleSheet(u"#b5_3{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#b5_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b5_3.setCheckable(True)
        self.f4_13 = QPushButton(self.ram_info_widget_3)
        self.f4_13.setObjectName(u"f4_13")
        self.f4_13.setGeometry(QRect(1310, 10, 31, 181))
        self.f4_13.setStyleSheet(u"#f4_13{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#f4_13:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_13.setCheckable(True)
        self.g40_13 = QPushButton(self.ram_info_widget_3)
        self.g40_13.setObjectName(u"g40_13")
        self.g40_13.setGeometry(QRect(1360, 10, 21, 111))
        self.g40_13.setStyleSheet(u"#g40_13{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_13:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.g40_13.setCheckable(True)
        self.c6_3 = QPushButton(self.ram_info_widget_3)
        self.c6_3.setObjectName(u"c6_3")
        self.c6_3.setGeometry(QRect(1640, 10, 31, 181))
        self.c6_3.setStyleSheet(u"#c6_3{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#c6_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c6_3.setCheckable(True)
        self.b4_16 = QPushButton(self.ram_info_widget_3)
        self.b4_16.setObjectName(u"b4_16")
        self.b4_16.setGeometry(QRect(1190, 10, 31, 181))
        self.b4_16.setStyleSheet(u"#b4_16{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#b4_16:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_16.setCheckable(True)
        self.f4_14 = QPushButton(self.ram_info_widget_3)
        self.f4_14.setObjectName(u"f4_14")
        self.f4_14.setGeometry(QRect(1100, 10, 31, 181))
        self.f4_14.setStyleSheet(u"#f4_14{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#f4_14:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_14.setCheckable(True)
        self.e4_14 = QPushButton(self.ram_info_widget_3)
        self.e4_14.setObjectName(u"e4_14")
        self.e4_14.setGeometry(QRect(1070, 10, 31, 181))
        self.e4_14.setStyleSheet(u"#e4_14{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#e4_14:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_14.setCheckable(True)
        self.g4_14 = QPushButton(self.ram_info_widget_3)
        self.g4_14.setObjectName(u"g4_14")
        self.g4_14.setGeometry(QRect(1130, 10, 31, 181))
        self.g4_14.setStyleSheet(u"#g4_14{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#g4_14:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_14.setCheckable(True)
        self.d4_14 = QPushButton(self.ram_info_widget_3)
        self.d4_14.setObjectName(u"d4_14")
        self.d4_14.setGeometry(QRect(1040, 10, 31, 181))
        self.d4_14.setStyleSheet(u"#d4_14{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#d4_14:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_14.setCheckable(True)
        self.a40_16 = QPushButton(self.ram_info_widget_3)
        self.a40_16.setObjectName(u"a40_16")
        self.a40_16.setGeometry(QRect(1180, 10, 21, 111))
        self.a40_16.setStyleSheet(u"#a40_16{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_16:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.a40_16.setCheckable(True)
        self.c40_14 = QPushButton(self.ram_info_widget_3)
        self.c40_14.setObjectName(u"c40_14")
        self.c40_14.setGeometry(QRect(1030, 10, 21, 111))
        self.c40_14.setStyleSheet(u"#c40_14{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_14:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.c40_14.setCheckable(True)
        self.f40_14 = QPushButton(self.ram_info_widget_3)
        self.f40_14.setObjectName(u"f40_14")
        self.f40_14.setGeometry(QRect(1120, 10, 21, 111))
        self.f40_14.setStyleSheet(u"#f40_14{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_14:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.f40_14.setCheckable(True)
        self.a4_16 = QPushButton(self.ram_info_widget_3)
        self.a4_16.setObjectName(u"a4_16")
        self.a4_16.setGeometry(QRect(1160, 10, 31, 181))
        self.a4_16.setStyleSheet(u"#a4_16{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#a4_16:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a4_16.setCheckable(True)
        self.d40_14 = QPushButton(self.ram_info_widget_3)
        self.d40_14.setObjectName(u"d40_14")
        self.d40_14.setGeometry(QRect(1060, 10, 21, 111))
        self.d40_14.setStyleSheet(u"#d40_14{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_14:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.d40_14.setCheckable(True)
        self.g40_14 = QPushButton(self.ram_info_widget_3)
        self.g40_14.setObjectName(u"g40_14")
        self.g40_14.setGeometry(QRect(1150, 10, 21, 111))
        self.g40_14.setStyleSheet(u"#g40_14{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_14:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.g40_14.setCheckable(True)
        self.c4_14 = QPushButton(self.ram_info_widget_3)
        self.c4_14.setObjectName(u"c4_14")
        self.c4_14.setGeometry(QRect(1010, 10, 31, 181))
        self.c4_14.setStyleSheet(u"#c4_14{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#c4_14:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c4_14.setCheckable(True)
        self.b4_17 = QPushButton(self.ram_info_widget_3)
        self.b4_17.setObjectName(u"b4_17")
        self.b4_17.setGeometry(QRect(980, 10, 31, 181))
        self.b4_17.setStyleSheet(u"#b4_17{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#b4_17:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_17.setCheckable(True)
        self.f4_15 = QPushButton(self.ram_info_widget_3)
        self.f4_15.setObjectName(u"f4_15")
        self.f4_15.setGeometry(QRect(890, 10, 31, 181))
        self.f4_15.setStyleSheet(u"#f4_15{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#f4_15:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_15.setCheckable(True)
        self.e4_15 = QPushButton(self.ram_info_widget_3)
        self.e4_15.setObjectName(u"e4_15")
        self.e4_15.setGeometry(QRect(860, 10, 31, 181))
        self.e4_15.setStyleSheet(u"#e4_15{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#e4_15:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_15.setCheckable(True)
        self.g4_15 = QPushButton(self.ram_info_widget_3)
        self.g4_15.setObjectName(u"g4_15")
        self.g4_15.setGeometry(QRect(920, 10, 31, 181))
        self.g4_15.setStyleSheet(u"#g4_15{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#g4_15:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_15.setCheckable(True)
        self.d4_15 = QPushButton(self.ram_info_widget_3)
        self.d4_15.setObjectName(u"d4_15")
        self.d4_15.setGeometry(QRect(830, 10, 31, 181))
        self.d4_15.setStyleSheet(u"#d4_15{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#d4_15:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_15.setCheckable(True)
        self.a40_17 = QPushButton(self.ram_info_widget_3)
        self.a40_17.setObjectName(u"a40_17")
        self.a40_17.setGeometry(QRect(970, 10, 21, 111))
        self.a40_17.setStyleSheet(u"#a40_17{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_17:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.a40_17.setCheckable(True)
        self.c40_15 = QPushButton(self.ram_info_widget_3)
        self.c40_15.setObjectName(u"c40_15")
        self.c40_15.setGeometry(QRect(820, 10, 21, 111))
        self.c40_15.setStyleSheet(u"#c40_15{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_15:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c40_15.setCheckable(True)
        self.f40_15 = QPushButton(self.ram_info_widget_3)
        self.f40_15.setObjectName(u"f40_15")
        self.f40_15.setGeometry(QRect(910, 10, 21, 111))
        self.f40_15.setStyleSheet(u"#f40_15{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_15:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.f40_15.setCheckable(True)
        self.a4_17 = QPushButton(self.ram_info_widget_3)
        self.a4_17.setObjectName(u"a4_17")
        self.a4_17.setGeometry(QRect(950, 10, 31, 181))
        self.a4_17.setStyleSheet(u"#a4_17{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#a4_17:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a4_17.setCheckable(True)
        self.d40_15 = QPushButton(self.ram_info_widget_3)
        self.d40_15.setObjectName(u"d40_15")
        self.d40_15.setGeometry(QRect(850, 10, 21, 111))
        self.d40_15.setStyleSheet(u"#d40_15{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_15:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.d40_15.setCheckable(True)
        self.g40_15 = QPushButton(self.ram_info_widget_3)
        self.g40_15.setObjectName(u"g40_15")
        self.g40_15.setGeometry(QRect(940, 10, 21, 111))
        self.g40_15.setStyleSheet(u"#g40_15{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_15:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.g40_15.setCheckable(True)
        self.c4_15 = QPushButton(self.ram_info_widget_3)
        self.c4_15.setObjectName(u"c4_15")
        self.c4_15.setGeometry(QRect(800, 10, 31, 181))
        self.c4_15.setStyleSheet(u"#c4_15{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#c4_15:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c4_15.setCheckable(True)
        self.b4_18 = QPushButton(self.ram_info_widget_3)
        self.b4_18.setObjectName(u"b4_18")
        self.b4_18.setGeometry(QRect(770, 10, 31, 181))
        self.b4_18.setStyleSheet(u"#b4_18{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#b4_18:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_18.setCheckable(True)
        self.f4_16 = QPushButton(self.ram_info_widget_3)
        self.f4_16.setObjectName(u"f4_16")
        self.f4_16.setGeometry(QRect(680, 10, 31, 181))
        self.f4_16.setStyleSheet(u"#f4_16{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#f4_16:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_16.setCheckable(True)
        self.e4_16 = QPushButton(self.ram_info_widget_3)
        self.e4_16.setObjectName(u"e4_16")
        self.e4_16.setGeometry(QRect(650, 10, 31, 181))
        self.e4_16.setStyleSheet(u"#e4_16{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#e4_16:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_16.setCheckable(True)
        self.g4_16 = QPushButton(self.ram_info_widget_3)
        self.g4_16.setObjectName(u"g4_16")
        self.g4_16.setGeometry(QRect(710, 10, 31, 181))
        self.g4_16.setStyleSheet(u"#g4_16{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#g4_16:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_16.setCheckable(True)
        self.d4_16 = QPushButton(self.ram_info_widget_3)
        self.d4_16.setObjectName(u"d4_16")
        self.d4_16.setGeometry(QRect(620, 10, 31, 181))
        self.d4_16.setStyleSheet(u"#d4_16{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#d4_16:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_16.setCheckable(True)
        self.a40_18 = QPushButton(self.ram_info_widget_3)
        self.a40_18.setObjectName(u"a40_18")
        self.a40_18.setGeometry(QRect(760, 10, 21, 111))
        self.a40_18.setStyleSheet(u"#a40_18{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_18:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.a40_18.setCheckable(True)
        self.c40_16 = QPushButton(self.ram_info_widget_3)
        self.c40_16.setObjectName(u"c40_16")
        self.c40_16.setGeometry(QRect(610, 10, 21, 111))
        self.c40_16.setStyleSheet(u"#c40_16{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_16:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c40_16.setCheckable(True)
        self.f40_16 = QPushButton(self.ram_info_widget_3)
        self.f40_16.setObjectName(u"f40_16")
        self.f40_16.setGeometry(QRect(700, 10, 21, 111))
        self.f40_16.setStyleSheet(u"#f40_16{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_16:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.f40_16.setCheckable(True)
        self.a4_18 = QPushButton(self.ram_info_widget_3)
        self.a4_18.setObjectName(u"a4_18")
        self.a4_18.setGeometry(QRect(740, 10, 31, 181))
        self.a4_18.setStyleSheet(u"#a4_18{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#a4_18:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a4_18.setCheckable(True)
        self.d40_16 = QPushButton(self.ram_info_widget_3)
        self.d40_16.setObjectName(u"d40_16")
        self.d40_16.setGeometry(QRect(640, 10, 21, 111))
        self.d40_16.setStyleSheet(u"#d40_16{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_16:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.d40_16.setCheckable(True)
        self.g40_16 = QPushButton(self.ram_info_widget_3)
        self.g40_16.setObjectName(u"g40_16")
        self.g40_16.setGeometry(QRect(730, 10, 21, 111))
        self.g40_16.setStyleSheet(u"#g40_16{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_16:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.g40_16.setCheckable(True)
        self.c4_16 = QPushButton(self.ram_info_widget_3)
        self.c4_16.setObjectName(u"c4_16")
        self.c4_16.setGeometry(QRect(590, 10, 31, 181))
        self.c4_16.setStyleSheet(u"#c4_16{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#c4_16:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c4_16.setCheckable(True)
        self.b4_19 = QPushButton(self.ram_info_widget_3)
        self.b4_19.setObjectName(u"b4_19")
        self.b4_19.setGeometry(QRect(560, 10, 31, 181))
        self.b4_19.setStyleSheet(u"#b4_19{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#b4_19:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_19.setCheckable(True)
        self.f4_17 = QPushButton(self.ram_info_widget_3)
        self.f4_17.setObjectName(u"f4_17")
        self.f4_17.setGeometry(QRect(470, 10, 31, 181))
        self.f4_17.setStyleSheet(u"#f4_17{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#f4_17:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_17.setCheckable(True)
        self.e4_17 = QPushButton(self.ram_info_widget_3)
        self.e4_17.setObjectName(u"e4_17")
        self.e4_17.setGeometry(QRect(440, 10, 31, 181))
        self.e4_17.setStyleSheet(u"#e4_17{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#e4_17:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_17.setCheckable(True)
        self.g4_17 = QPushButton(self.ram_info_widget_3)
        self.g4_17.setObjectName(u"g4_17")
        self.g4_17.setGeometry(QRect(500, 10, 31, 181))
        self.g4_17.setStyleSheet(u"#g4_17{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#g4_17:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_17.setCheckable(True)
        self.d4_17 = QPushButton(self.ram_info_widget_3)
        self.d4_17.setObjectName(u"d4_17")
        self.d4_17.setGeometry(QRect(410, 10, 31, 181))
        self.d4_17.setStyleSheet(u"#d4_17{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#d4_17:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_17.setCheckable(True)
        self.a40_19 = QPushButton(self.ram_info_widget_3)
        self.a40_19.setObjectName(u"a40_19")
        self.a40_19.setGeometry(QRect(550, 10, 21, 111))
        self.a40_19.setStyleSheet(u"#a40_19{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_19:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.a40_19.setCheckable(True)
        self.c40_17 = QPushButton(self.ram_info_widget_3)
        self.c40_17.setObjectName(u"c40_17")
        self.c40_17.setGeometry(QRect(400, 10, 21, 111))
        self.c40_17.setStyleSheet(u"#c40_17{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_17:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c40_17.setCheckable(True)
        self.f40_17 = QPushButton(self.ram_info_widget_3)
        self.f40_17.setObjectName(u"f40_17")
        self.f40_17.setGeometry(QRect(490, 10, 21, 111))
        self.f40_17.setStyleSheet(u"#f40_17{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_17:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.f40_17.setCheckable(True)
        self.a4_19 = QPushButton(self.ram_info_widget_3)
        self.a4_19.setObjectName(u"a4_19")
        self.a4_19.setGeometry(QRect(530, 10, 31, 181))
        self.a4_19.setStyleSheet(u"#a4_19{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#a4_19:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a4_19.setCheckable(True)
        self.d40_17 = QPushButton(self.ram_info_widget_3)
        self.d40_17.setObjectName(u"d40_17")
        self.d40_17.setGeometry(QRect(430, 10, 21, 111))
        self.d40_17.setStyleSheet(u"#d40_17{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_17:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.d40_17.setCheckable(True)
        self.g40_17 = QPushButton(self.ram_info_widget_3)
        self.g40_17.setObjectName(u"g40_17")
        self.g40_17.setGeometry(QRect(520, 10, 21, 111))
        self.g40_17.setStyleSheet(u"#g40_17{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_17:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.g40_17.setCheckable(True)
        self.c4_17 = QPushButton(self.ram_info_widget_3)
        self.c4_17.setObjectName(u"c4_17")
        self.c4_17.setGeometry(QRect(380, 10, 31, 181))
        self.c4_17.setStyleSheet(u"#c4_17{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#c4_17:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c4_17.setCheckable(True)
        self.b4_20 = QPushButton(self.ram_info_widget_3)
        self.b4_20.setObjectName(u"b4_20")
        self.b4_20.setGeometry(QRect(350, 10, 31, 181))
        self.b4_20.setStyleSheet(u"#b4_20{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#b4_20:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_20.setCheckable(True)
        self.f4_18 = QPushButton(self.ram_info_widget_3)
        self.f4_18.setObjectName(u"f4_18")
        self.f4_18.setGeometry(QRect(260, 10, 31, 181))
        self.f4_18.setStyleSheet(u"#f4_18{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#f4_18:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_18.setCheckable(True)
        self.e4_18 = QPushButton(self.ram_info_widget_3)
        self.e4_18.setObjectName(u"e4_18")
        self.e4_18.setGeometry(QRect(230, 10, 31, 181))
        self.e4_18.setStyleSheet(u"#e4_18{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#e4_18:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_18.setCheckable(True)
        self.g4_18 = QPushButton(self.ram_info_widget_3)
        self.g4_18.setObjectName(u"g4_18")
        self.g4_18.setGeometry(QRect(290, 10, 31, 181))
        self.g4_18.setStyleSheet(u"#g4_18{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#g4_18:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_18.setCheckable(True)
        self.d4_18 = QPushButton(self.ram_info_widget_3)
        self.d4_18.setObjectName(u"d4_18")
        self.d4_18.setGeometry(QRect(200, 10, 31, 181))
        self.d4_18.setStyleSheet(u"#d4_18{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#d4_18:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_18.setCheckable(True)
        self.a40_20 = QPushButton(self.ram_info_widget_3)
        self.a40_20.setObjectName(u"a40_20")
        self.a40_20.setGeometry(QRect(340, 10, 21, 111))
        self.a40_20.setStyleSheet(u"#a40_20{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_20:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.a40_20.setCheckable(True)
        self.c40_18 = QPushButton(self.ram_info_widget_3)
        self.c40_18.setObjectName(u"c40_18")
        self.c40_18.setGeometry(QRect(190, 10, 21, 111))
        self.c40_18.setStyleSheet(u"#c40_18{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_18:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c40_18.setCheckable(True)
        self.f40_18 = QPushButton(self.ram_info_widget_3)
        self.f40_18.setObjectName(u"f40_18")
        self.f40_18.setGeometry(QRect(280, 10, 21, 111))
        self.f40_18.setStyleSheet(u"#f40_18{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_18:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.f40_18.setCheckable(True)
        self.a4_20 = QPushButton(self.ram_info_widget_3)
        self.a4_20.setObjectName(u"a4_20")
        self.a4_20.setGeometry(QRect(320, 10, 31, 181))
        self.a4_20.setStyleSheet(u"#a4_20{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#a4_20:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a4_20.setCheckable(True)
        self.d40_18 = QPushButton(self.ram_info_widget_3)
        self.d40_18.setObjectName(u"d40_18")
        self.d40_18.setGeometry(QRect(220, 10, 21, 111))
        self.d40_18.setStyleSheet(u"#d40_18{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_18:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.d40_18.setCheckable(True)
        self.g40_18 = QPushButton(self.ram_info_widget_3)
        self.g40_18.setObjectName(u"g40_18")
        self.g40_18.setGeometry(QRect(310, 10, 21, 111))
        self.g40_18.setStyleSheet(u"#g40_18{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_18:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.g40_18.setCheckable(True)
        self.c4_18 = QPushButton(self.ram_info_widget_3)
        self.c4_18.setObjectName(u"c4_18")
        self.c4_18.setGeometry(QRect(170, 10, 31, 181))
        self.c4_18.setStyleSheet(u"#c4_18{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#c4_18:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c4_18.setCheckable(True)
        self.b4_21 = QPushButton(self.ram_info_widget_3)
        self.b4_21.setObjectName(u"b4_21")
        self.b4_21.setGeometry(QRect(140, 10, 31, 181))
        self.b4_21.setStyleSheet(u"#b4_21{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#b4_21:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_21.setCheckable(True)
        self.a40_21 = QPushButton(self.ram_info_widget_3)
        self.a40_21.setObjectName(u"a40_21")
        self.a40_21.setGeometry(QRect(130, 10, 21, 111))
        self.a40_21.setStyleSheet(u"#a40_21{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_21:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.a40_21.setCheckable(True)
        self.a4_21 = QPushButton(self.ram_info_widget_3)
        self.a4_21.setObjectName(u"a4_21")
        self.a4_21.setGeometry(QRect(110, 10, 31, 181))
        self.a4_21.setStyleSheet(u"#a4_21{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"#a4_21:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a4_21.setCheckable(True)
        self.f5_3.raise_()
        self.g4_13.raise_()
        self.d4_13.raise_()
        self.e4_13.raise_()
        self.d5_3.raise_()
        self.a4_15.raise_()
        self.a5_3.raise_()
        self.e5_3.raise_()
        self.c5_3.raise_()
        self.b4_15.raise_()
        self.c4_13.raise_()
        self.g5_3.raise_()
        self.c50_3.raise_()
        self.b5_3.raise_()
        self.f4_13.raise_()
        self.c6_3.raise_()
        self.b4_16.raise_()
        self.f4_14.raise_()
        self.e4_14.raise_()
        self.g4_14.raise_()
        self.d4_14.raise_()
        self.f40_14.raise_()
        self.a4_16.raise_()
        self.d40_14.raise_()
        self.g40_14.raise_()
        self.c4_14.raise_()
        self.b4_17.raise_()
        self.f4_15.raise_()
        self.e4_15.raise_()
        self.g4_15.raise_()
        self.d4_15.raise_()
        self.f40_15.raise_()
        self.a4_17.raise_()
        self.d40_15.raise_()
        self.g40_15.raise_()
        self.c4_15.raise_()
        self.b4_18.raise_()
        self.f4_16.raise_()
        self.e4_16.raise_()
        self.g4_16.raise_()
        self.d4_16.raise_()
        self.f40_16.raise_()
        self.a4_18.raise_()
        self.d40_16.raise_()
        self.g40_16.raise_()
        self.c4_16.raise_()
        self.b4_19.raise_()
        self.f4_17.raise_()
        self.e4_17.raise_()
        self.g4_17.raise_()
        self.d4_17.raise_()
        self.f40_17.raise_()
        self.a4_19.raise_()
        self.d40_17.raise_()
        self.g40_17.raise_()
        self.c4_17.raise_()
        self.b4_20.raise_()
        self.f4_18.raise_()
        self.e4_18.raise_()
        self.g4_18.raise_()
        self.d4_18.raise_()
        self.f40_18.raise_()
        self.a4_20.raise_()
        self.d40_18.raise_()
        self.g40_18.raise_()
        self.c4_18.raise_()
        self.b4_21.raise_()
        self.a4_21.raise_()
        self.a40_21.raise_()
        self.c40_18.raise_()
        self.a40_20.raise_()
        self.c40_17.raise_()
        self.a40_19.raise_()
        self.c40_16.raise_()
        self.a40_18.raise_()
        self.c40_15.raise_()
        self.a40_17.raise_()
        self.c40_14.raise_()
        self.a40_16.raise_()
        self.d40_13.raise_()
        self.c40_13.raise_()
        self.f40_13.raise_()
        self.g40_13.raise_()
        self.a40_15.raise_()
        self.d50_3.raise_()
        self.f50_3.raise_()
        self.g50_3.raise_()
        self.a50_3.raise_()
        self.clear_notes = QPushButton(self.cmemory)
        self.clear_notes.setObjectName(u"clear_notes")
        self.clear_notes.setGeometry(QRect(950, 780, 161, 41))
        self.clear_notes.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff,\n"
"        stop:0.5 rgba(255, 200, 150, 0.3),\n"
"        stop:1 rgba(255, 180, 80, 0.2)\n"
"    );\n"
"    border: 2px solid rgba(255, 165, 0, 0.4);\n"
"    border-radius: 12px;\n"
"    color: #333;\n"
"    font-weight: 600;\n"
"    font-size: 12px;\n"
"    padding: 8px 20px;\n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);\n"
"    transition: all 0.2s ease-in-out;\n"
"}\n"
"\n"
"/* Simulate outer glow layer */\n"
"QPushButton::before {\n"
"    content: \"\";\n"
"    border-radius: 16px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(255, 255, 255, 0.7),\n"
"        stop:1 rgba(255, 180, 80, 0.15)\n"
"    );\n"
"}\n"
"\n"
"/* Hover effect: warmer orange and deeper glow */\n"
"QPushButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #fff5e6,\n"
"        stop:1 rgba(255, 150, 0, 0.4)\n"
"   "
                        " );\n"
"    border: 2px solid rgba(255, 140, 0, 0.7);\n"
"    color: #000;\n"
"    box-shadow: 0 0 10px rgba(255, 165, 0, 0.6);\n"
"}\n"
"\n"
"/* Pressed (active) effect */\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(255, 200, 100, 0.8),\n"
"        stop:1 rgba(255, 150, 0, 0.6)\n"
"    );\n"
"    box-shadow: 0 0 4px rgba(255, 120, 0, 0.5);\n"
"    transform: scale(0.98);\n"
"}\n"
"\n"
"/* Focus ring effect */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 2px solid #ff8800;\n"
"}\n"
"")
        self.select_all = QPushButton(self.cmemory)
        self.select_all.setObjectName(u"select_all")
        self.select_all.setGeometry(QRect(630, 780, 171, 41))
        self.select_all.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff,\n"
"        stop:0.5 rgba(255, 200, 150, 0.3),\n"
"        stop:1 rgba(255, 180, 80, 0.2)\n"
"    );\n"
"    border: 2px solid rgba(255, 165, 0, 0.4);\n"
"    border-radius: 12px;\n"
"    color: #333;\n"
"    font-weight: 600;\n"
"    font-size: 12px;\n"
"    padding: 8px 20px;\n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);\n"
"    transition: all 0.2s ease-in-out;\n"
"}\n"
"\n"
"/* Simulate outer glow layer */\n"
"QPushButton::before {\n"
"    content: \"\";\n"
"    border-radius: 16px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(255, 255, 255, 0.7),\n"
"        stop:1 rgba(255, 180, 80, 0.15)\n"
"    );\n"
"}\n"
"\n"
"/* Hover effect: warmer orange and deeper glow */\n"
"QPushButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #fff5e6,\n"
"        stop:1 rgba(255, 150, 0, 0.4)\n"
"   "
                        " );\n"
"    border: 2px solid rgba(255, 140, 0, 0.7);\n"
"    color: #000;\n"
"    box-shadow: 0 0 10px rgba(255, 165, 0, 0.6);\n"
"}\n"
"\n"
"/* Pressed (active) effect */\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(255, 200, 100, 0.8),\n"
"        stop:1 rgba(255, 150, 0, 0.6)\n"
"    );\n"
"    box-shadow: 0 0 4px rgba(255, 120, 0, 0.5);\n"
"    transform: scale(0.98);\n"
"}\n"
"\n"
"/* Focus ring effect */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 2px solid #ff8800;\n"
"}\n"
"")
        self.groupBox_3 = QGroupBox(self.cmemory)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(80, 20, 491, 451))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #D0D0D0;  /* light gray border */\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"    font-weight: bold;\n"
"    color: #555;\n"
"    padding: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"}\n"
"")
        self.gridLayoutWidget = QWidget(self.groupBox_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 471, 241))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.gridLayoutWidget)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.gridLayout_2.addWidget(self.label_54, 3, 0, 1, 1)

        self.lineEdit_counter_period = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_counter_period.setObjectName(u"lineEdit_counter_period")
        self.lineEdit_counter_period.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_counter_period, 0, 1, 1, 1)

        self.lineEdit_ratio = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ratio.setObjectName(u"lineEdit_ratio")
        self.lineEdit_ratio.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_ratio, 1, 1, 1, 1)

        self.label_53 = QLabel(self.gridLayoutWidget)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)

        self.gridLayout_2.addWidget(self.label_53, 2, 0, 1, 1)

        self.lineEdit_ratio_black = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ratio_black.setObjectName(u"lineEdit_ratio_black")
        self.lineEdit_ratio_black.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_ratio_black, 2, 1, 1, 1)

        self.lineEdit_ratio_white = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ratio_white.setObjectName(u"lineEdit_ratio_white")
        self.lineEdit_ratio_white.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_ratio_white, 3, 1, 1, 1)

        self.label_52 = QLabel(self.gridLayoutWidget)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)

        self.gridLayout_2.addWidget(self.label_52, 0, 0, 1, 1)

        self.label_49 = QLabel(self.gridLayoutWidget)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)

        self.gridLayout_2.addWidget(self.label_49, 1, 0, 1, 1)

        self.gridLayoutWidget_5 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 280, 471, 91))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scan_nogoodkeyboards = QCheckBox(self.gridLayoutWidget_5)
        self.scan_nogoodkeyboards.setObjectName(u"scan_nogoodkeyboards")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.scan_nogoodkeyboards.setFont(font3)
        self.scan_nogoodkeyboards.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 3px;\n"
"    background: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: none;\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked::before {\n"
"    content: \"\u2713\";\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    position: absolute;\n"
"    left: 3px;\n"
"    top: -1px;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.scan_nogoodkeyboards.setIconSize(QSize(16, 16))
        self.scan_nogoodkeyboards.setChecked(True)

        self.gridLayout_7.addWidget(self.scan_nogoodkeyboards, 0, 1, 1, 1)

        self.checkBoxrebounded = QCheckBox(self.gridLayoutWidget_5)
        self.checkBoxrebounded.setObjectName(u"checkBoxrebounded")
        self.checkBoxrebounded.setFont(font3)
        self.checkBoxrebounded.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 3px;\n"
"    background: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: none;\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked::before {\n"
"    content: \"\u2713\";\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    position: absolute;\n"
"    left: 3px;\n"
"    top: -1px;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.checkBoxrebounded.setIconSize(QSize(16, 16))
        self.checkBoxrebounded.setChecked(True)

        self.gridLayout_7.addWidget(self.checkBoxrebounded, 1, 0, 1, 1)

        self.checkBox_notimer = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_notimer.setObjectName(u"checkBox_notimer")
        self.checkBox_notimer.setFont(font3)
        self.checkBox_notimer.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 3px;\n"
"    background: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: none;\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked::before {\n"
"    content: \"\u2713\";\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    position: absolute;\n"
"    left: 3px;\n"
"    top: -1px;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.checkBox_notimer.setIconSize(QSize(16, 16))
        self.checkBox_notimer.setChecked(True)

        self.gridLayout_7.addWidget(self.checkBox_notimer, 1, 1, 1, 1)

        self.checkBoxresplit = QCheckBox(self.gridLayoutWidget_5)
        self.checkBoxresplit.setObjectName(u"checkBoxresplit")
        self.checkBoxresplit.setFont(font3)
        self.checkBoxresplit.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 3px;\n"
"    background: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: none;\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked::before {\n"
"    content: \"\u2713\";\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    position: absolute;\n"
"    left: 3px;\n"
"    top: -1px;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.checkBoxresplit.setIconSize(QSize(16, 16))
        self.checkBoxresplit.setChecked(True)

        self.gridLayout_7.addWidget(self.checkBoxresplit, 0, 0, 1, 1)

        self.gridLayoutWidget_6 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 380, 471, 51))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dynamic_radio = QRadioButton(self.gridLayoutWidget_6)
        self.dynamic_radio.setObjectName(u"dynamic_radio")
        self.dynamic_radio.setStyleSheet(u"/* Hide default radio indicator */\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"/* Base style */\n"
"QRadioButton {\n"
"    padding: 3px 14px;\n"
"    min-height: 16px;\n"
"    border-radius: 8px;\n"
"    border: 1px solid #d0d0d0;\n"
"    background-color: #f8f8f8;\n"
"    color: #333;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QRadioButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"/* Checked (orange highlight) */\n"
"QRadioButton:checked {\n"
"    background-color: #fff2e0;\n"
"    border: 1.5px solid #ff9800;\n"
"    color: #222;\n"
"    padding-left: 16px;   /* tiny shift = premium look */\n"
"    transition: 0.15s;\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.dynamic_radio, 0, 0, 1, 1)

        self.aft_radio = QRadioButton(self.gridLayoutWidget_6)
        self.aft_radio.setObjectName(u"aft_radio")
        self.aft_radio.setStyleSheet(u"/* Hide default radio indicator */\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"/* Base style */\n"
"QRadioButton {\n"
"    padding: 3px 14px;\n"
"    min-height: 16px;\n"
"    border-radius: 8px;\n"
"    border: 1px solid #d0d0d0;\n"
"    background-color: #f8f8f8;\n"
"    color: #333;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QRadioButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"/* Checked (orange highlight) */\n"
"QRadioButton:checked {\n"
"    background-color: #fff2e0;\n"
"    border: 1.5px solid #ff9800;\n"
"    color: #222;\n"
"    padding-left: 16px;   /* tiny shift = premium look */\n"
"    transition: 0.15s;\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.aft_radio, 0, 1, 1, 1)

        self.full_radio = QRadioButton(self.gridLayoutWidget_6)
        self.full_radio.setObjectName(u"full_radio")
        self.full_radio.setStyleSheet(u"/* Hide default radio indicator */\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"/* Base style */\n"
"QRadioButton {\n"
"    padding: 3px 14px;\n"
"    min-height: 16px;\n"
"    border-radius: 8px;\n"
"    border: 1px solid #d0d0d0;\n"
"    background-color: #f8f8f8;\n"
"    color: #333;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QRadioButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"/* Checked (orange highlight) */\n"
"QRadioButton:checked {\n"
"    background-color: #fff2e0;\n"
"    border: 1.5px solid #ff9800;\n"
"    color: #222;\n"
"    padding-left: 16px;   /* tiny shift = premium look */\n"
"    transition: 0.15s;\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.full_radio, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.cmemory)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(620, 20, 491, 451))
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #D0D0D0;  /* light gray border */\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"    font-weight: bold;\n"
"    color: #555;\n"
"    padding: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"}\n"
"")
        self.v_gain_lineEdit_2 = QLineEdit(self.groupBox_4)
        self.v_gain_lineEdit_2.setObjectName(u"v_gain_lineEdit_2")
        self.v_gain_lineEdit_2.setEnabled(False)
        self.v_gain_lineEdit_2.setGeometry(QRect(110, 390, 61, 20))
        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(40, 390, 51, 16))
        self.label_35.setFont(font)
        self.v_gain_slider_2 = QSlider(self.groupBox_4)
        self.v_gain_slider_2.setObjectName(u"v_gain_slider_2")
        self.v_gain_slider_2.setGeometry(QRect(130, 290, 16, 101))
        self.v_gain_slider_2.setStyleSheet(u"/* === Groove === */\n"
"QSlider::groove:vertical {\n"
"    width: 14px;\n"
"    border-radius: 7px;\n"
"    background: rgba(255, 140, 0, 0.15);  /* soft orange glow */\n"
"    margin: 4px 0;\n"
"}\n"
"\n"
"/* === Filled Part (active section) === */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:1, x2:0, y2:0,\n"
"        stop:0 #ffb84d,\n"
"        stop:0.5 #ff9a1f,\n"
"        stop:1 #ff6b00\n"
"    );\n"
"    border-radius: 7px;\n"
"    box-shadow: 0 0 8px rgba(255, 140, 0, 0.4);\n"
"}\n"
"\n"
"/* === Empty Part === */\n"
"QSlider::add-page:vertical {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"/* === Smaller Handle === */\n"
"QSlider::handle:vertical {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        stop:0 #fff,\n"
"        stop:1 #ff8c00\n"
"    );\n"
"    border: 1px solid #ff8c00;\n"
"    width: 10px;\n"
"    height: 6px;              /* smaller horizontal bar */\n"
"    bo"
                        "rder-radius: 3px;\n"
"    margin: -3px -3px;\n"
"    transition: all 0.2s ease-in-out;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        stop:0 #fff,\n"
"        stop:1 #ffaa33\n"
"    );\n"
"    box-shadow: 0 0 6px rgba(255, 140, 0, 0.6);\n"
"}\n"
"\n"
"/* === Optional: Matching LineEdit === */\n"
"QLineEdit {\n"
"    font-size: 16px;\n"
"    border: 2px solid #ff9a1f;\n"
"    border-radius: 8px;\n"
"    background-color: #fffaf2;\n"
"    color: #333;\n"
"    padding: 4px 8px;\n"
"}\n"
"")
        self.v_gain_slider_2.setMinimum(40)
        self.v_gain_slider_2.setMaximum(200)
        self.v_gain_slider_2.setOrientation(Qt.Vertical)
        self.label_38 = QLabel(self.groupBox_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(40, 380, 47, 14))
        self.label_38.setFont(font)
        self.v_gain_lineEdit = QLineEdit(self.groupBox_4)
        self.v_gain_lineEdit.setObjectName(u"v_gain_lineEdit")
        self.v_gain_lineEdit.setEnabled(False)
        self.v_gain_lineEdit.setGeometry(QRect(350, 390, 61, 20))
        self.label_45 = QLabel(self.groupBox_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(280, 380, 47, 14))
        self.label_45.setFont(font)
        self.v_gain_slider = QSlider(self.groupBox_4)
        self.v_gain_slider.setObjectName(u"v_gain_slider")
        self.v_gain_slider.setGeometry(QRect(370, 290, 16, 101))
        self.v_gain_slider.setStyleSheet(u"/* === Groove === */\n"
"QSlider::groove:vertical {\n"
"    width: 14px;\n"
"    border-radius: 7px;\n"
"    background: rgba(255, 140, 0, 0.15);  /* soft orange glow */\n"
"    margin: 4px 0;\n"
"}\n"
"\n"
"/* === Filled Part (active section) === */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:1, x2:0, y2:0,\n"
"        stop:0 #ffb84d,\n"
"        stop:0.5 #ff9a1f,\n"
"        stop:1 #ff6b00\n"
"    );\n"
"    border-radius: 7px;\n"
"    box-shadow: 0 0 8px rgba(255, 140, 0, 0.4);\n"
"}\n"
"\n"
"/* === Empty Part === */\n"
"QSlider::add-page:vertical {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"/* === Smaller Handle === */\n"
"QSlider::handle:vertical {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        stop:0 #fff,\n"
"        stop:1 #ff8c00\n"
"    );\n"
"    border: 1px solid #ff8c00;\n"
"    width: 10px;\n"
"    height: 6px;              /* smaller horizontal bar */\n"
"    bo"
                        "rder-radius: 3px;\n"
"    margin: -3px -3px;\n"
"    transition: all 0.2s ease-in-out;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        stop:0 #fff,\n"
"        stop:1 #ffaa33\n"
"    );\n"
"    box-shadow: 0 0 6px rgba(255, 140, 0, 0.6);\n"
"}\n"
"\n"
"/* === Optional: Matching LineEdit === */\n"
"QLineEdit {\n"
"    font-size: 16px;\n"
"    border: 2px solid #ff9a1f;\n"
"    border-radius: 8px;\n"
"    background-color: #fffaf2;\n"
"    color: #333;\n"
"    padding: 4px 8px;\n"
"}\n"
"")
        self.v_gain_slider.setMinimum(40)
        self.v_gain_slider.setMaximum(200)
        self.v_gain_slider.setOrientation(Qt.Vertical)
        self.label_25 = QLabel(self.groupBox_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(280, 390, 51, 16))
        self.label_25.setFont(font)
        self.gridLayoutWidget_3 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 30, 471, 121))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_min_vel = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_min_vel.setObjectName(u"lineEdit_min_vel")
        self.lineEdit_min_vel.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.lineEdit_min_vel, 1, 1, 1, 1)

        self.lineEdit_max_vel = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_max_vel.setObjectName(u"lineEdit_max_vel")
        self.lineEdit_max_vel.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.lineEdit_max_vel, 0, 1, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)

        self.gridLayout_4.addWidget(self.label_47, 0, 0, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.gridLayout_4.addWidget(self.label_48, 1, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 180, 471, 71))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.two_sw = QRadioButton(self.gridLayoutWidget_4)
        self.two_sw.setObjectName(u"two_sw")
        self.two_sw.setStyleSheet(u"/* Hide default radio dot */\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"/* Base (unselected) */\n"
"QRadioButton {\n"
"    padding: 3px 14px;\n"
"    min-height: 16px;\n"
"    border-radius: 8px;\n"
"    border: 1px solid #d0d0d0;\n"
"    background-color: #f5f5f5;\n"
"    color: #333;\n"
"    font-weight: 600;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* Hover */\n"
"QRadioButton:hover {\n"
"    background-color: #ededed;\n"
"}\n"
"\n"
"/* Selected (ORANGE) */\n"
"QRadioButton#two_sw:checked,\n"
"QRadioButton#three_sw:checked {\n"
"    background-color: #fff4e5;\n"
"    border: 1.5px solid #FFA500;\n"
"    color: #000;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.two_sw, 0, 0, 1, 1)

        self.three_sw = QRadioButton(self.gridLayoutWidget_4)
        self.three_sw.setObjectName(u"three_sw")
        self.three_sw.setStyleSheet(u"/* Hide default radio dot */\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"/* Base (unselected) */\n"
"QRadioButton {\n"
"    padding: 4px 14px;\n"
"    min-height: 16px;\n"
"    border-radius: 8px;\n"
"    border: 1px solid #d0d0d0;\n"
"    background-color: #f5f5f5;\n"
"    color: #333;\n"
"    font-weight: 600;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* Hover */\n"
"QRadioButton:hover {\n"
"    background-color: #ededed;\n"
"}\n"
"\n"
"/* Selected (ORANGE) */\n"
"QRadioButton#two_sw:checked,\n"
"QRadioButton#three_sw:checked {\n"
"    background-color: #fff4e5;\n"
"    border: 1.5px solid #FFA500;\n"
"    color: #000;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.three_sw, 0, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.cmemory)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(1160, 19, 531, 451))
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #D0D0D0;  /* light gray border */\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"    font-weight: bold;\n"
"    color: #555;\n"
"    padding: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"}\n"
"")
        self.gridLayoutWidget_2 = QWidget(self.groupBox_5)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 30, 511, 241))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_3.addWidget(self.label_20, 1, 0, 1, 1)

        self.lineEdit_user_min = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_user_min.setObjectName(u"lineEdit_user_min")
        self.lineEdit_user_min.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_user_min, 1, 1, 1, 1)

        self.label_50 = QLabel(self.gridLayoutWidget_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)

        self.gridLayout_3.addWidget(self.label_50, 2, 0, 1, 1)

        self.lineEdit_user_max = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_user_max.setObjectName(u"lineEdit_user_max")
        self.lineEdit_user_max.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_user_max, 0, 1, 1, 1)

        self.lineEdit_max_RES = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_max_RES.setObjectName(u"lineEdit_max_RES")
        self.lineEdit_max_RES.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_max_RES, 2, 1, 1, 1)

        self.label_51 = QLabel(self.gridLayoutWidget_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.gridLayout_3.addWidget(self.label_51, 3, 0, 1, 1)

        self.lineEdit_min_RES = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_min_RES.setObjectName(u"lineEdit_min_RES")
        self.lineEdit_min_RES.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;       /* orange outline */\n"
"    background-color: #e2e2e2;\n"
"    padding: 10px 12px;\n"
"    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFB347;       /* lighter orange on focus */\n"
"    background-color: #ffffff;\n"
"	box-shadow: 0 0 8px #FFD580;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFC266;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_min_RES, 3, 1, 1, 1)

        self.exponent_slider = QSlider(self.groupBox_5)
        self.exponent_slider.setObjectName(u"exponent_slider")
        self.exponent_slider.setGeometry(QRect(280, 290, 16, 101))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        self.exponent_slider.setFont(font4)
        self.exponent_slider.setStyleSheet(u"/* === Groove === */\n"
"QSlider::groove:vertical {\n"
"    width: 14px;\n"
"    border-radius: 7px;\n"
"    background: rgba(255, 140, 0, 0.15);  /* soft orange glow */\n"
"    margin: 4px 0;\n"
"}\n"
"\n"
"/* === Filled Part (active section) === */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:1, x2:0, y2:0,\n"
"        stop:0 #ffb84d,\n"
"        stop:0.5 #ff9a1f,\n"
"        stop:1 #ff6b00\n"
"    );\n"
"    border-radius: 7px;\n"
"    box-shadow: 0 0 8px rgba(255, 140, 0, 0.4);\n"
"}\n"
"\n"
"/* === Empty Part === */\n"
"QSlider::add-page:vertical {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"/* === Smaller Handle === */\n"
"QSlider::handle:vertical {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        stop:0 #fff,\n"
"        stop:1 #ff8c00\n"
"    );\n"
"    border: 1px solid #ff8c00;\n"
"    width: 10px;\n"
"    height: 6px;              /* smaller horizontal bar */\n"
"    bo"
                        "rder-radius: 3px;\n"
"    margin: -3px -3px;\n"
"    transition: all 0.2s ease-in-out;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        stop:0 #fff,\n"
"        stop:1 #ffaa33\n"
"    );\n"
"    box-shadow: 0 0 6px rgba(255, 140, 0, 0.6);\n"
"}\n"
"\n"
"/* === Optional: Matching LineEdit === */\n"
"QLineEdit {\n"
"    font-size: 16px;\n"
"    border: 2px solid #ff9a1f;\n"
"    border-radius: 8px;\n"
"    background-color: #fffaf2;\n"
"    color: #333;\n"
"    padding: 4px 8px;\n"
"}\n"
"")
        self.exponent_slider.setMinimum(100)
        self.exponent_slider.setMaximum(500)
        self.exponent_slider.setValue(100)
        self.exponent_slider.setOrientation(Qt.Vertical)
        self.lineEdit_exponent = QLineEdit(self.groupBox_5)
        self.lineEdit_exponent.setObjectName(u"lineEdit_exponent")
        self.lineEdit_exponent.setEnabled(False)
        self.lineEdit_exponent.setGeometry(QRect(260, 390, 71, 21))
        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(140, 390, 81, 20))
        self.label_24.setFont(font)
        self.stackedWidget.addWidget(self.cmemory)
        self.encoders_buttons = QWidget()
        self.encoders_buttons.setObjectName(u"encoders_buttons")
        self.label_15 = QLabel(self.encoders_buttons)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(100, -4, 111, 16))
        self.label_15.setFont(font)
        self.ram_info_widget = QWidget(self.encoders_buttons)
        self.ram_info_widget.setObjectName(u"ram_info_widget")
        self.ram_info_widget.setGeometry(QRect(9, 320, 1690, 195))
        self.ram_info_widget.setStyleSheet(u"")
        self.d5 = QPushButton(self.ram_info_widget)
        self.d5.setObjectName(u"d5")
        self.d5.setGeometry(QRect(1460, 10, 31, 181))
        self.d5.setStyleSheet(u"#d5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#d5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d40 = QPushButton(self.ram_info_widget)
        self.d40.setObjectName(u"d40")
        self.d40.setGeometry(QRect(1270, 10, 21, 111))
        self.d40.setStyleSheet(u"#d40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.a4 = QPushButton(self.ram_info_widget)
        self.a4.setObjectName(u"a4")
        self.a4.setGeometry(QRect(1370, 10, 31, 181))
        self.a4.setStyleSheet(u"#a4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#a4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f40 = QPushButton(self.ram_info_widget)
        self.f40.setObjectName(u"f40")
        self.f40.setGeometry(QRect(1330, 10, 21, 111))
        self.f40.setStyleSheet(u"#f40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.f50 = QPushButton(self.ram_info_widget)
        self.f50.setObjectName(u"f50")
        self.f50.setGeometry(QRect(1540, 10, 21, 111))
        self.f50.setStyleSheet(u"#f50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"#f50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.a5 = QPushButton(self.ram_info_widget)
        self.a5.setObjectName(u"a5")
        self.a5.setGeometry(QRect(1580, 10, 31, 181))
        self.a5.setStyleSheet(u"#a5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"#a5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d50 = QPushButton(self.ram_info_widget)
        self.d50.setObjectName(u"d50")
        self.d50.setGeometry(QRect(1480, 10, 21, 111))
        self.d50.setStyleSheet(u"#d50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.e5 = QPushButton(self.ram_info_widget)
        self.e5.setObjectName(u"e5")
        self.e5.setGeometry(QRect(1490, 10, 31, 181))
        self.e5.setStyleSheet(u"#e5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#e5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c5 = QPushButton(self.ram_info_widget)
        self.c5.setObjectName(u"c5")
        self.c5.setGeometry(QRect(1430, 10, 31, 181))
        self.c5.setStyleSheet(u"#c5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#c5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4 = QPushButton(self.ram_info_widget)
        self.g4.setObjectName(u"g4")
        self.g4.setGeometry(QRect(1340, 10, 31, 181))
        self.g4.setStyleSheet(u"#g4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#g4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g50 = QPushButton(self.ram_info_widget)
        self.g50.setObjectName(u"g50")
        self.g50.setGeometry(QRect(1570, 10, 21, 111))
        self.g50.setStyleSheet(u"#g50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"#g50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.c40 = QPushButton(self.ram_info_widget)
        self.c40.setObjectName(u"c40")
        self.c40.setGeometry(QRect(1240, 10, 21, 111))
        self.c40.setStyleSheet(u"#c40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.b4 = QPushButton(self.ram_info_widget)
        self.b4.setObjectName(u"b4")
        self.b4.setGeometry(QRect(1400, 10, 31, 181))
        self.b4.setStyleSheet(u"#b4{\n"
"background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"\n"
"#b4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c4 = QPushButton(self.ram_info_widget)
        self.c4.setObjectName(u"c4")
        self.c4.setGeometry(QRect(1220, 10, 31, 181))
        self.c4.setStyleSheet(u"#c4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#c4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g5 = QPushButton(self.ram_info_widget)
        self.g5.setObjectName(u"g5")
        self.g5.setGeometry(QRect(1550, 10, 31, 181))
        self.g5.setStyleSheet(u"#g5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#g5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4 = QPushButton(self.ram_info_widget)
        self.d4.setObjectName(u"d4")
        self.d4.setGeometry(QRect(1250, 10, 31, 181))
        self.d4.setStyleSheet(u"#d4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#d4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a40 = QPushButton(self.ram_info_widget)
        self.a40.setObjectName(u"a40")
        self.a40.setGeometry(QRect(1390, 10, 21, 111))
        self.a40.setStyleSheet(u"#a40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.e4 = QPushButton(self.ram_info_widget)
        self.e4.setObjectName(u"e4")
        self.e4.setGeometry(QRect(1280, 10, 31, 181))
        self.e4.setStyleSheet(u"#e4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#e4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f5 = QPushButton(self.ram_info_widget)
        self.f5.setObjectName(u"f5")
        self.f5.setGeometry(QRect(1520, 10, 31, 181))
        self.f5.setStyleSheet(u"#f5{\n"
"background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"\n"
"#f5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a50 = QPushButton(self.ram_info_widget)
        self.a50.setObjectName(u"a50")
        self.a50.setGeometry(QRect(1600, 10, 21, 111))
        self.a50.setStyleSheet(u"#a50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"#a50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.c50 = QPushButton(self.ram_info_widget)
        self.c50.setObjectName(u"c50")
        self.c50.setGeometry(QRect(1450, 10, 21, 111))
        self.c50.setStyleSheet(u"#c50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.b5 = QPushButton(self.ram_info_widget)
        self.b5.setObjectName(u"b5")
        self.b5.setGeometry(QRect(1610, 10, 31, 181))
        self.b5.setStyleSheet(u"#b5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#b5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4 = QPushButton(self.ram_info_widget)
        self.f4.setObjectName(u"f4")
        self.f4.setGeometry(QRect(1310, 10, 31, 181))
        self.f4.setStyleSheet(u"#f4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#f4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g40 = QPushButton(self.ram_info_widget)
        self.g40.setObjectName(u"g40")
        self.g40.setGeometry(QRect(1360, 10, 21, 111))
        self.g40.setStyleSheet(u"#g40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.c6 = QPushButton(self.ram_info_widget)
        self.c6.setObjectName(u"c6")
        self.c6.setGeometry(QRect(1640, 10, 31, 181))
        self.c6.setStyleSheet(u"#c6{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#c6:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_2 = QPushButton(self.ram_info_widget)
        self.b4_2.setObjectName(u"b4_2")
        self.b4_2.setGeometry(QRect(1190, 10, 31, 181))
        self.b4_2.setStyleSheet(u"#b4_2{\n"
"background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"\n"
"#b4_2:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_2 = QPushButton(self.ram_info_widget)
        self.f4_2.setObjectName(u"f4_2")
        self.f4_2.setGeometry(QRect(1100, 10, 31, 181))
        self.f4_2.setStyleSheet(u"#f4_2{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#f4_2:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_2 = QPushButton(self.ram_info_widget)
        self.e4_2.setObjectName(u"e4_2")
        self.e4_2.setGeometry(QRect(1070, 10, 31, 181))
        self.e4_2.setStyleSheet(u"#e4_2{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#e4_2:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_2 = QPushButton(self.ram_info_widget)
        self.g4_2.setObjectName(u"g4_2")
        self.g4_2.setGeometry(QRect(1130, 10, 31, 181))
        self.g4_2.setStyleSheet(u"#g4_2{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#g4_2:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_2 = QPushButton(self.ram_info_widget)
        self.d4_2.setObjectName(u"d4_2")
        self.d4_2.setGeometry(QRect(1040, 10, 31, 181))
        self.d4_2.setStyleSheet(u"#d4_2{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#d4_2:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a40_2 = QPushButton(self.ram_info_widget)
        self.a40_2.setObjectName(u"a40_2")
        self.a40_2.setGeometry(QRect(1180, 10, 21, 111))
        self.a40_2.setStyleSheet(u"#a40_2{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_2:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.c40_2 = QPushButton(self.ram_info_widget)
        self.c40_2.setObjectName(u"c40_2")
        self.c40_2.setGeometry(QRect(1030, 10, 21, 111))
        self.c40_2.setStyleSheet(u"#c40_2{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_2:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.f40_2 = QPushButton(self.ram_info_widget)
        self.f40_2.setObjectName(u"f40_2")
        self.f40_2.setGeometry(QRect(1120, 10, 21, 111))
        self.f40_2.setStyleSheet(u"#f40_2{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_2:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.a4_2 = QPushButton(self.ram_info_widget)
        self.a4_2.setObjectName(u"a4_2")
        self.a4_2.setGeometry(QRect(1160, 10, 31, 181))
        self.a4_2.setStyleSheet(u"#a4_2{\n"
"background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"\n"
"#a4_2:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d40_2 = QPushButton(self.ram_info_widget)
        self.d40_2.setObjectName(u"d40_2")
        self.d40_2.setGeometry(QRect(1060, 10, 21, 111))
        self.d40_2.setStyleSheet(u"#d40_2{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_2:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.g40_2 = QPushButton(self.ram_info_widget)
        self.g40_2.setObjectName(u"g40_2")
        self.g40_2.setGeometry(QRect(1150, 10, 21, 111))
        self.g40_2.setStyleSheet(u"#g40_2{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_2:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.c4_2 = QPushButton(self.ram_info_widget)
        self.c4_2.setObjectName(u"c4_2")
        self.c4_2.setGeometry(QRect(1010, 10, 31, 181))
        self.c4_2.setStyleSheet(u"#c4_2{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#c4_2:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_3 = QPushButton(self.ram_info_widget)
        self.b4_3.setObjectName(u"b4_3")
        self.b4_3.setGeometry(QRect(980, 10, 31, 181))
        self.b4_3.setStyleSheet(u"#b4_3{\n"
"background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"\n"
"#b4_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_3 = QPushButton(self.ram_info_widget)
        self.f4_3.setObjectName(u"f4_3")
        self.f4_3.setGeometry(QRect(890, 10, 31, 181))
        self.f4_3.setStyleSheet(u"#f4_3{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#f4_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_3 = QPushButton(self.ram_info_widget)
        self.e4_3.setObjectName(u"e4_3")
        self.e4_3.setGeometry(QRect(860, 10, 31, 181))
        self.e4_3.setStyleSheet(u"#e4_3{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#e4_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_3 = QPushButton(self.ram_info_widget)
        self.g4_3.setObjectName(u"g4_3")
        self.g4_3.setGeometry(QRect(920, 10, 31, 181))
        self.g4_3.setStyleSheet(u"#g4_3{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#g4_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_3 = QPushButton(self.ram_info_widget)
        self.d4_3.setObjectName(u"d4_3")
        self.d4_3.setGeometry(QRect(830, 10, 31, 181))
        self.d4_3.setStyleSheet(u"#d4_3{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#d4_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a40_3 = QPushButton(self.ram_info_widget)
        self.a40_3.setObjectName(u"a40_3")
        self.a40_3.setGeometry(QRect(970, 10, 21, 111))
        self.a40_3.setStyleSheet(u"#a40_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c40_3 = QPushButton(self.ram_info_widget)
        self.c40_3.setObjectName(u"c40_3")
        self.c40_3.setGeometry(QRect(820, 10, 21, 111))
        self.c40_3.setStyleSheet(u"#c40_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.f40_3 = QPushButton(self.ram_info_widget)
        self.f40_3.setObjectName(u"f40_3")
        self.f40_3.setGeometry(QRect(910, 10, 21, 111))
        self.f40_3.setStyleSheet(u"#f40_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.a4_3 = QPushButton(self.ram_info_widget)
        self.a4_3.setObjectName(u"a4_3")
        self.a4_3.setGeometry(QRect(950, 10, 31, 181))
        self.a4_3.setStyleSheet(u"#a4_3{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#a4_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d40_3 = QPushButton(self.ram_info_widget)
        self.d40_3.setObjectName(u"d40_3")
        self.d40_3.setGeometry(QRect(850, 10, 21, 111))
        self.d40_3.setStyleSheet(u"#d40_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.g40_3 = QPushButton(self.ram_info_widget)
        self.g40_3.setObjectName(u"g40_3")
        self.g40_3.setGeometry(QRect(940, 10, 21, 111))
        self.g40_3.setStyleSheet(u"#g40_3{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_3:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c4_3 = QPushButton(self.ram_info_widget)
        self.c4_3.setObjectName(u"c4_3")
        self.c4_3.setGeometry(QRect(800, 10, 31, 181))
        self.c4_3.setStyleSheet(u"#c4_3{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#c4_3:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_4 = QPushButton(self.ram_info_widget)
        self.b4_4.setObjectName(u"b4_4")
        self.b4_4.setGeometry(QRect(770, 10, 31, 181))
        self.b4_4.setStyleSheet(u"#b4_4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#b4_4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_4 = QPushButton(self.ram_info_widget)
        self.f4_4.setObjectName(u"f4_4")
        self.f4_4.setGeometry(QRect(680, 10, 31, 181))
        self.f4_4.setStyleSheet(u"#f4_4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#f4_4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_4 = QPushButton(self.ram_info_widget)
        self.e4_4.setObjectName(u"e4_4")
        self.e4_4.setGeometry(QRect(650, 10, 31, 181))
        self.e4_4.setStyleSheet(u"#e4_4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#e4_4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_4 = QPushButton(self.ram_info_widget)
        self.g4_4.setObjectName(u"g4_4")
        self.g4_4.setGeometry(QRect(710, 10, 31, 181))
        self.g4_4.setStyleSheet(u"#g4_4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#g4_4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_4 = QPushButton(self.ram_info_widget)
        self.d4_4.setObjectName(u"d4_4")
        self.d4_4.setGeometry(QRect(620, 10, 31, 181))
        self.d4_4.setStyleSheet(u"#d4_4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#d4_4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a40_4 = QPushButton(self.ram_info_widget)
        self.a40_4.setObjectName(u"a40_4")
        self.a40_4.setGeometry(QRect(760, 10, 21, 111))
        self.a40_4.setStyleSheet(u"#a40_4{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_4:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c40_4 = QPushButton(self.ram_info_widget)
        self.c40_4.setObjectName(u"c40_4")
        self.c40_4.setGeometry(QRect(610, 10, 21, 111))
        self.c40_4.setStyleSheet(u"#c40_4{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_4:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.f40_4 = QPushButton(self.ram_info_widget)
        self.f40_4.setObjectName(u"f40_4")
        self.f40_4.setGeometry(QRect(700, 10, 21, 111))
        self.f40_4.setStyleSheet(u"#f40_4{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_4:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.a4_4 = QPushButton(self.ram_info_widget)
        self.a4_4.setObjectName(u"a4_4")
        self.a4_4.setGeometry(QRect(740, 10, 31, 181))
        self.a4_4.setStyleSheet(u"#a4_4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#a4_4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d40_4 = QPushButton(self.ram_info_widget)
        self.d40_4.setObjectName(u"d40_4")
        self.d40_4.setGeometry(QRect(640, 10, 21, 111))
        self.d40_4.setStyleSheet(u"#d40_4{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_4:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.g40_4 = QPushButton(self.ram_info_widget)
        self.g40_4.setObjectName(u"g40_4")
        self.g40_4.setGeometry(QRect(730, 10, 21, 111))
        self.g40_4.setStyleSheet(u"#g40_4{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_4:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c4_4 = QPushButton(self.ram_info_widget)
        self.c4_4.setObjectName(u"c4_4")
        self.c4_4.setGeometry(QRect(590, 10, 31, 181))
        self.c4_4.setStyleSheet(u"#c4_4{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#c4_4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_5 = QPushButton(self.ram_info_widget)
        self.b4_5.setObjectName(u"b4_5")
        self.b4_5.setGeometry(QRect(560, 10, 31, 181))
        self.b4_5.setStyleSheet(u"#b4_5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#b4_5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_5 = QPushButton(self.ram_info_widget)
        self.f4_5.setObjectName(u"f4_5")
        self.f4_5.setGeometry(QRect(470, 10, 31, 181))
        self.f4_5.setStyleSheet(u"#f4_5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#f4_5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_5 = QPushButton(self.ram_info_widget)
        self.e4_5.setObjectName(u"e4_5")
        self.e4_5.setGeometry(QRect(440, 10, 31, 181))
        self.e4_5.setStyleSheet(u"#e4_5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#e4_5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_5 = QPushButton(self.ram_info_widget)
        self.g4_5.setObjectName(u"g4_5")
        self.g4_5.setGeometry(QRect(500, 10, 31, 181))
        self.g4_5.setStyleSheet(u"#g4_5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#g4_5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_5 = QPushButton(self.ram_info_widget)
        self.d4_5.setObjectName(u"d4_5")
        self.d4_5.setGeometry(QRect(410, 10, 31, 181))
        self.d4_5.setStyleSheet(u"#d4_5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#d4_5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a40_5 = QPushButton(self.ram_info_widget)
        self.a40_5.setObjectName(u"a40_5")
        self.a40_5.setGeometry(QRect(550, 10, 21, 111))
        self.a40_5.setStyleSheet(u"#a40_5{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_5:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c40_5 = QPushButton(self.ram_info_widget)
        self.c40_5.setObjectName(u"c40_5")
        self.c40_5.setGeometry(QRect(400, 10, 21, 111))
        self.c40_5.setStyleSheet(u"#c40_5{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_5:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.f40_5 = QPushButton(self.ram_info_widget)
        self.f40_5.setObjectName(u"f40_5")
        self.f40_5.setGeometry(QRect(490, 10, 21, 111))
        self.f40_5.setStyleSheet(u"#f40_5{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_5:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"")
        self.a4_5 = QPushButton(self.ram_info_widget)
        self.a4_5.setObjectName(u"a4_5")
        self.a4_5.setGeometry(QRect(530, 10, 31, 181))
        self.a4_5.setStyleSheet(u"#a4_5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#a4_5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d40_5 = QPushButton(self.ram_info_widget)
        self.d40_5.setObjectName(u"d40_5")
        self.d40_5.setGeometry(QRect(430, 10, 21, 111))
        self.d40_5.setStyleSheet(u"#d40_5{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_5:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.g40_5 = QPushButton(self.ram_info_widget)
        self.g40_5.setObjectName(u"g40_5")
        self.g40_5.setGeometry(QRect(520, 10, 21, 111))
        self.g40_5.setStyleSheet(u"#g40_5{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_5:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c4_5 = QPushButton(self.ram_info_widget)
        self.c4_5.setObjectName(u"c4_5")
        self.c4_5.setGeometry(QRect(380, 10, 31, 181))
        self.c4_5.setStyleSheet(u"#c4_5{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#c4_5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_6 = QPushButton(self.ram_info_widget)
        self.b4_6.setObjectName(u"b4_6")
        self.b4_6.setGeometry(QRect(350, 10, 31, 181))
        self.b4_6.setStyleSheet(u"#b4_6{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#b4_6:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4_6 = QPushButton(self.ram_info_widget)
        self.f4_6.setObjectName(u"f4_6")
        self.f4_6.setGeometry(QRect(260, 10, 31, 181))
        self.f4_6.setStyleSheet(u"#f4_6{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#f4_6:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4_6 = QPushButton(self.ram_info_widget)
        self.e4_6.setObjectName(u"e4_6")
        self.e4_6.setGeometry(QRect(230, 10, 31, 181))
        self.e4_6.setStyleSheet(u"#e4_6{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#e4_6:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4_6 = QPushButton(self.ram_info_widget)
        self.g4_6.setObjectName(u"g4_6")
        self.g4_6.setGeometry(QRect(290, 10, 31, 181))
        self.g4_6.setStyleSheet(u"#g4_6{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#g4_6:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4_6 = QPushButton(self.ram_info_widget)
        self.d4_6.setObjectName(u"d4_6")
        self.d4_6.setGeometry(QRect(200, 10, 31, 181))
        self.d4_6.setStyleSheet(u"#d4_6{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#d4_6:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a40_6 = QPushButton(self.ram_info_widget)
        self.a40_6.setObjectName(u"a40_6")
        self.a40_6.setGeometry(QRect(340, 10, 21, 111))
        self.a40_6.setStyleSheet(u"#a40_6{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_6:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.c40_6 = QPushButton(self.ram_info_widget)
        self.c40_6.setObjectName(u"c40_6")
        self.c40_6.setGeometry(QRect(190, 10, 21, 111))
        self.c40_6.setStyleSheet(u"#c40_6{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#c40_6:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.f40_6 = QPushButton(self.ram_info_widget)
        self.f40_6.setObjectName(u"f40_6")
        self.f40_6.setGeometry(QRect(280, 10, 21, 111))
        self.f40_6.setStyleSheet(u"#f40_6{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#f40_6:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.a4_6 = QPushButton(self.ram_info_widget)
        self.a4_6.setObjectName(u"a4_6")
        self.a4_6.setGeometry(QRect(320, 10, 31, 181))
        self.a4_6.setStyleSheet(u"#a4_6{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#a4_6:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d40_6 = QPushButton(self.ram_info_widget)
        self.d40_6.setObjectName(u"d40_6")
        self.d40_6.setGeometry(QRect(220, 10, 21, 111))
        self.d40_6.setStyleSheet(u"#d40_6{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#d40_6:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.g40_6 = QPushButton(self.ram_info_widget)
        self.g40_6.setObjectName(u"g40_6")
        self.g40_6.setGeometry(QRect(310, 10, 21, 111))
        self.g40_6.setStyleSheet(u"#g40_6{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#g40_6:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.c4_6 = QPushButton(self.ram_info_widget)
        self.c4_6.setObjectName(u"c4_6")
        self.c4_6.setGeometry(QRect(170, 10, 31, 181))
        self.c4_6.setStyleSheet(u"#c4_6{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#c4_6:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4_7 = QPushButton(self.ram_info_widget)
        self.b4_7.setObjectName(u"b4_7")
        self.b4_7.setGeometry(QRect(140, 10, 31, 181))
        self.b4_7.setStyleSheet(u"#b4_7{\n"
"background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"\n"
"#b4_7:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a40_7 = QPushButton(self.ram_info_widget)
        self.a40_7.setObjectName(u"a40_7")
        self.a40_7.setGeometry(QRect(130, 10, 21, 111))
        self.a40_7.setStyleSheet(u"#a40_7{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid black;\n"
"}\n"
"#a40_6:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.a4_7 = QPushButton(self.ram_info_widget)
        self.a4_7.setObjectName(u"a4_7")
        self.a4_7.setGeometry(QRect(110, 10, 31, 181))
        self.a4_7.setStyleSheet(u"#a4_7{\n"
"background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#a4_7:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.verticalSlider_3 = QSlider(self.ram_info_widget)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setGeometry(QRect(130, 10, 21, 111))
        self.verticalSlider_3.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_3.setMaximum(127)
        self.verticalSlider_3.setOrientation(Qt.Vertical)
        self.verticalSlider = QSlider(self.ram_info_widget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(110, 10, 31, 181))
        self.verticalSlider.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider.setMaximum(127)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider_2 = QSlider(self.ram_info_widget)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setGeometry(QRect(140, 10, 31, 181))
        self.verticalSlider_2.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_2.setMaximum(127)
        self.verticalSlider_2.setOrientation(Qt.Vertical)
        self.verticalSlider_4 = QSlider(self.ram_info_widget)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setGeometry(QRect(170, 10, 31, 181))
        self.verticalSlider_4.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_4.setMaximum(127)
        self.verticalSlider_4.setOrientation(Qt.Vertical)
        self.verticalSlider_5 = QSlider(self.ram_info_widget)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        self.verticalSlider_5.setGeometry(QRect(200, 10, 31, 181))
        self.verticalSlider_5.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_5.setMaximum(127)
        self.verticalSlider_5.setOrientation(Qt.Vertical)
        self.verticalSlider_6 = QSlider(self.ram_info_widget)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        self.verticalSlider_6.setGeometry(QRect(230, 10, 31, 181))
        self.verticalSlider_6.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_6.setMaximum(127)
        self.verticalSlider_6.setOrientation(Qt.Vertical)
        self.verticalSlider_7 = QSlider(self.ram_info_widget)
        self.verticalSlider_7.setObjectName(u"verticalSlider_7")
        self.verticalSlider_7.setGeometry(QRect(260, 10, 31, 181))
        self.verticalSlider_7.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_7.setMaximum(127)
        self.verticalSlider_7.setOrientation(Qt.Vertical)
        self.verticalSlider_8 = QSlider(self.ram_info_widget)
        self.verticalSlider_8.setObjectName(u"verticalSlider_8")
        self.verticalSlider_8.setGeometry(QRect(290, 10, 31, 181))
        self.verticalSlider_8.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_8.setMaximum(127)
        self.verticalSlider_8.setOrientation(Qt.Vertical)
        self.verticalSlider_9 = QSlider(self.ram_info_widget)
        self.verticalSlider_9.setObjectName(u"verticalSlider_9")
        self.verticalSlider_9.setGeometry(QRect(320, 10, 31, 181))
        self.verticalSlider_9.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_9.setMaximum(127)
        self.verticalSlider_9.setOrientation(Qt.Vertical)
        self.verticalSlider_10 = QSlider(self.ram_info_widget)
        self.verticalSlider_10.setObjectName(u"verticalSlider_10")
        self.verticalSlider_10.setGeometry(QRect(350, 10, 31, 181))
        self.verticalSlider_10.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_10.setMaximum(127)
        self.verticalSlider_10.setOrientation(Qt.Vertical)
        self.verticalSlider_11 = QSlider(self.ram_info_widget)
        self.verticalSlider_11.setObjectName(u"verticalSlider_11")
        self.verticalSlider_11.setGeometry(QRect(380, 10, 31, 181))
        self.verticalSlider_11.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_11.setMaximum(127)
        self.verticalSlider_11.setOrientation(Qt.Vertical)
        self.verticalSlider_12 = QSlider(self.ram_info_widget)
        self.verticalSlider_12.setObjectName(u"verticalSlider_12")
        self.verticalSlider_12.setGeometry(QRect(410, 10, 31, 181))
        self.verticalSlider_12.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_12.setMaximum(127)
        self.verticalSlider_12.setOrientation(Qt.Vertical)
        self.verticalSlider_13 = QSlider(self.ram_info_widget)
        self.verticalSlider_13.setObjectName(u"verticalSlider_13")
        self.verticalSlider_13.setGeometry(QRect(440, 10, 31, 181))
        self.verticalSlider_13.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_13.setMaximum(127)
        self.verticalSlider_13.setOrientation(Qt.Vertical)
        self.verticalSlider_14 = QSlider(self.ram_info_widget)
        self.verticalSlider_14.setObjectName(u"verticalSlider_14")
        self.verticalSlider_14.setGeometry(QRect(470, 10, 31, 181))
        self.verticalSlider_14.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_14.setMaximum(127)
        self.verticalSlider_14.setOrientation(Qt.Vertical)
        self.verticalSlider_15 = QSlider(self.ram_info_widget)
        self.verticalSlider_15.setObjectName(u"verticalSlider_15")
        self.verticalSlider_15.setGeometry(QRect(500, 10, 31, 181))
        self.verticalSlider_15.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_15.setMaximum(127)
        self.verticalSlider_15.setOrientation(Qt.Vertical)
        self.verticalSlider_16 = QSlider(self.ram_info_widget)
        self.verticalSlider_16.setObjectName(u"verticalSlider_16")
        self.verticalSlider_16.setGeometry(QRect(530, 10, 31, 181))
        self.verticalSlider_16.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_16.setMaximum(127)
        self.verticalSlider_16.setOrientation(Qt.Vertical)
        self.verticalSlider_17 = QSlider(self.ram_info_widget)
        self.verticalSlider_17.setObjectName(u"verticalSlider_17")
        self.verticalSlider_17.setGeometry(QRect(560, 10, 31, 181))
        self.verticalSlider_17.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_17.setMaximum(127)
        self.verticalSlider_17.setOrientation(Qt.Vertical)
        self.verticalSlider_18 = QSlider(self.ram_info_widget)
        self.verticalSlider_18.setObjectName(u"verticalSlider_18")
        self.verticalSlider_18.setGeometry(QRect(590, 10, 31, 181))
        self.verticalSlider_18.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_18.setMaximum(127)
        self.verticalSlider_18.setOrientation(Qt.Vertical)
        self.verticalSlider_19 = QSlider(self.ram_info_widget)
        self.verticalSlider_19.setObjectName(u"verticalSlider_19")
        self.verticalSlider_19.setGeometry(QRect(620, 10, 31, 181))
        self.verticalSlider_19.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_19.setMaximum(127)
        self.verticalSlider_19.setOrientation(Qt.Vertical)
        self.verticalSlider_20 = QSlider(self.ram_info_widget)
        self.verticalSlider_20.setObjectName(u"verticalSlider_20")
        self.verticalSlider_20.setGeometry(QRect(650, 10, 31, 181))
        self.verticalSlider_20.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_20.setMaximum(127)
        self.verticalSlider_20.setOrientation(Qt.Vertical)
        self.verticalSlider_21 = QSlider(self.ram_info_widget)
        self.verticalSlider_21.setObjectName(u"verticalSlider_21")
        self.verticalSlider_21.setGeometry(QRect(680, 10, 31, 181))
        self.verticalSlider_21.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_21.setMaximum(127)
        self.verticalSlider_21.setOrientation(Qt.Vertical)
        self.verticalSlider_22 = QSlider(self.ram_info_widget)
        self.verticalSlider_22.setObjectName(u"verticalSlider_22")
        self.verticalSlider_22.setGeometry(QRect(710, 10, 31, 181))
        self.verticalSlider_22.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_22.setMaximum(127)
        self.verticalSlider_22.setOrientation(Qt.Vertical)
        self.verticalSlider_23 = QSlider(self.ram_info_widget)
        self.verticalSlider_23.setObjectName(u"verticalSlider_23")
        self.verticalSlider_23.setGeometry(QRect(740, 10, 31, 181))
        self.verticalSlider_23.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_23.setMaximum(127)
        self.verticalSlider_23.setOrientation(Qt.Vertical)
        self.verticalSlider_24 = QSlider(self.ram_info_widget)
        self.verticalSlider_24.setObjectName(u"verticalSlider_24")
        self.verticalSlider_24.setGeometry(QRect(770, 10, 31, 181))
        self.verticalSlider_24.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_24.setMaximum(127)
        self.verticalSlider_24.setOrientation(Qt.Vertical)
        self.verticalSlider_25 = QSlider(self.ram_info_widget)
        self.verticalSlider_25.setObjectName(u"verticalSlider_25")
        self.verticalSlider_25.setGeometry(QRect(800, 10, 31, 181))
        self.verticalSlider_25.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_25.setMaximum(127)
        self.verticalSlider_25.setOrientation(Qt.Vertical)
        self.verticalSlider_26 = QSlider(self.ram_info_widget)
        self.verticalSlider_26.setObjectName(u"verticalSlider_26")
        self.verticalSlider_26.setGeometry(QRect(830, 10, 31, 181))
        self.verticalSlider_26.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_26.setMaximum(127)
        self.verticalSlider_26.setOrientation(Qt.Vertical)
        self.verticalSlider_27 = QSlider(self.ram_info_widget)
        self.verticalSlider_27.setObjectName(u"verticalSlider_27")
        self.verticalSlider_27.setGeometry(QRect(860, 10, 31, 181))
        self.verticalSlider_27.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_27.setMaximum(127)
        self.verticalSlider_27.setOrientation(Qt.Vertical)
        self.verticalSlider_28 = QSlider(self.ram_info_widget)
        self.verticalSlider_28.setObjectName(u"verticalSlider_28")
        self.verticalSlider_28.setGeometry(QRect(890, 10, 31, 181))
        self.verticalSlider_28.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_28.setMaximum(127)
        self.verticalSlider_28.setOrientation(Qt.Vertical)
        self.verticalSlider_29 = QSlider(self.ram_info_widget)
        self.verticalSlider_29.setObjectName(u"verticalSlider_29")
        self.verticalSlider_29.setGeometry(QRect(920, 10, 31, 181))
        self.verticalSlider_29.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_29.setMaximum(127)
        self.verticalSlider_29.setOrientation(Qt.Vertical)
        self.verticalSlider_30 = QSlider(self.ram_info_widget)
        self.verticalSlider_30.setObjectName(u"verticalSlider_30")
        self.verticalSlider_30.setGeometry(QRect(950, 10, 31, 181))
        self.verticalSlider_30.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_30.setMaximum(127)
        self.verticalSlider_30.setOrientation(Qt.Vertical)
        self.verticalSlider_31 = QSlider(self.ram_info_widget)
        self.verticalSlider_31.setObjectName(u"verticalSlider_31")
        self.verticalSlider_31.setGeometry(QRect(980, 10, 31, 181))
        self.verticalSlider_31.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_31.setMaximum(127)
        self.verticalSlider_31.setOrientation(Qt.Vertical)
        self.verticalSlider_32 = QSlider(self.ram_info_widget)
        self.verticalSlider_32.setObjectName(u"verticalSlider_32")
        self.verticalSlider_32.setGeometry(QRect(1010, 10, 31, 181))
        self.verticalSlider_32.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_32.setMaximum(127)
        self.verticalSlider_32.setOrientation(Qt.Vertical)
        self.verticalSlider_33 = QSlider(self.ram_info_widget)
        self.verticalSlider_33.setObjectName(u"verticalSlider_33")
        self.verticalSlider_33.setGeometry(QRect(1040, 10, 31, 181))
        self.verticalSlider_33.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_33.setMaximum(127)
        self.verticalSlider_33.setOrientation(Qt.Vertical)
        self.verticalSlider_34 = QSlider(self.ram_info_widget)
        self.verticalSlider_34.setObjectName(u"verticalSlider_34")
        self.verticalSlider_34.setGeometry(QRect(1070, 10, 31, 181))
        self.verticalSlider_34.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_34.setMaximum(127)
        self.verticalSlider_34.setOrientation(Qt.Vertical)
        self.verticalSlider_35 = QSlider(self.ram_info_widget)
        self.verticalSlider_35.setObjectName(u"verticalSlider_35")
        self.verticalSlider_35.setGeometry(QRect(1100, 10, 31, 181))
        self.verticalSlider_35.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_35.setMaximum(127)
        self.verticalSlider_35.setOrientation(Qt.Vertical)
        self.verticalSlider_36 = QSlider(self.ram_info_widget)
        self.verticalSlider_36.setObjectName(u"verticalSlider_36")
        self.verticalSlider_36.setGeometry(QRect(1130, 10, 31, 181))
        self.verticalSlider_36.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_36.setMaximum(127)
        self.verticalSlider_36.setOrientation(Qt.Vertical)
        self.verticalSlider_37 = QSlider(self.ram_info_widget)
        self.verticalSlider_37.setObjectName(u"verticalSlider_37")
        self.verticalSlider_37.setGeometry(QRect(1160, 10, 31, 181))
        self.verticalSlider_37.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_37.setMaximum(127)
        self.verticalSlider_37.setOrientation(Qt.Vertical)
        self.verticalSlider_38 = QSlider(self.ram_info_widget)
        self.verticalSlider_38.setObjectName(u"verticalSlider_38")
        self.verticalSlider_38.setGeometry(QRect(1190, 10, 31, 181))
        self.verticalSlider_38.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_38.setMaximum(127)
        self.verticalSlider_38.setOrientation(Qt.Vertical)
        self.verticalSlider_39 = QSlider(self.ram_info_widget)
        self.verticalSlider_39.setObjectName(u"verticalSlider_39")
        self.verticalSlider_39.setGeometry(QRect(1220, 10, 31, 181))
        self.verticalSlider_39.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_39.setMaximum(127)
        self.verticalSlider_39.setOrientation(Qt.Vertical)
        self.verticalSlider_40 = QSlider(self.ram_info_widget)
        self.verticalSlider_40.setObjectName(u"verticalSlider_40")
        self.verticalSlider_40.setGeometry(QRect(1250, 10, 31, 181))
        self.verticalSlider_40.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_40.setMaximum(127)
        self.verticalSlider_40.setOrientation(Qt.Vertical)
        self.verticalSlider_41 = QSlider(self.ram_info_widget)
        self.verticalSlider_41.setObjectName(u"verticalSlider_41")
        self.verticalSlider_41.setGeometry(QRect(1280, 10, 31, 181))
        self.verticalSlider_41.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_41.setMaximum(127)
        self.verticalSlider_41.setOrientation(Qt.Vertical)
        self.verticalSlider_42 = QSlider(self.ram_info_widget)
        self.verticalSlider_42.setObjectName(u"verticalSlider_42")
        self.verticalSlider_42.setGeometry(QRect(1310, 10, 31, 181))
        self.verticalSlider_42.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_42.setMaximum(127)
        self.verticalSlider_42.setOrientation(Qt.Vertical)
        self.verticalSlider_43 = QSlider(self.ram_info_widget)
        self.verticalSlider_43.setObjectName(u"verticalSlider_43")
        self.verticalSlider_43.setGeometry(QRect(1340, 10, 31, 181))
        self.verticalSlider_43.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_43.setMaximum(127)
        self.verticalSlider_43.setOrientation(Qt.Vertical)
        self.verticalSlider_44 = QSlider(self.ram_info_widget)
        self.verticalSlider_44.setObjectName(u"verticalSlider_44")
        self.verticalSlider_44.setGeometry(QRect(1370, 10, 31, 181))
        self.verticalSlider_44.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_44.setMaximum(127)
        self.verticalSlider_44.setOrientation(Qt.Vertical)
        self.verticalSlider_45 = QSlider(self.ram_info_widget)
        self.verticalSlider_45.setObjectName(u"verticalSlider_45")
        self.verticalSlider_45.setGeometry(QRect(1400, 10, 31, 181))
        self.verticalSlider_45.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_45.setMaximum(127)
        self.verticalSlider_45.setOrientation(Qt.Vertical)
        self.verticalSlider_46 = QSlider(self.ram_info_widget)
        self.verticalSlider_46.setObjectName(u"verticalSlider_46")
        self.verticalSlider_46.setGeometry(QRect(1430, 10, 31, 181))
        self.verticalSlider_46.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_46.setMaximum(127)
        self.verticalSlider_46.setOrientation(Qt.Vertical)
        self.verticalSlider_47 = QSlider(self.ram_info_widget)
        self.verticalSlider_47.setObjectName(u"verticalSlider_47")
        self.verticalSlider_47.setGeometry(QRect(1460, 10, 31, 181))
        self.verticalSlider_47.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_47.setMaximum(127)
        self.verticalSlider_47.setOrientation(Qt.Vertical)
        self.verticalSlider_48 = QSlider(self.ram_info_widget)
        self.verticalSlider_48.setObjectName(u"verticalSlider_48")
        self.verticalSlider_48.setGeometry(QRect(1490, 10, 31, 181))
        self.verticalSlider_48.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_48.setMaximum(127)
        self.verticalSlider_48.setOrientation(Qt.Vertical)
        self.verticalSlider_49 = QSlider(self.ram_info_widget)
        self.verticalSlider_49.setObjectName(u"verticalSlider_49")
        self.verticalSlider_49.setGeometry(QRect(1520, 10, 31, 181))
        self.verticalSlider_49.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_49.setMaximum(127)
        self.verticalSlider_49.setOrientation(Qt.Vertical)
        self.verticalSlider_50 = QSlider(self.ram_info_widget)
        self.verticalSlider_50.setObjectName(u"verticalSlider_50")
        self.verticalSlider_50.setGeometry(QRect(1550, 10, 31, 181))
        self.verticalSlider_50.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_50.setMaximum(127)
        self.verticalSlider_50.setOrientation(Qt.Vertical)
        self.verticalSlider_51 = QSlider(self.ram_info_widget)
        self.verticalSlider_51.setObjectName(u"verticalSlider_51")
        self.verticalSlider_51.setGeometry(QRect(1580, 10, 31, 181))
        self.verticalSlider_51.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_51.setMaximum(127)
        self.verticalSlider_51.setOrientation(Qt.Vertical)
        self.verticalSlider_52 = QSlider(self.ram_info_widget)
        self.verticalSlider_52.setObjectName(u"verticalSlider_52")
        self.verticalSlider_52.setGeometry(QRect(1610, 10, 31, 181))
        self.verticalSlider_52.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_52.setMaximum(127)
        self.verticalSlider_52.setOrientation(Qt.Vertical)
        self.verticalSlider_53 = QSlider(self.ram_info_widget)
        self.verticalSlider_53.setObjectName(u"verticalSlider_53")
        self.verticalSlider_53.setGeometry(QRect(1640, 10, 31, 181))
        self.verticalSlider_53.setStyleSheet(u"/* Groove styling - matches the original button */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches button border */\n"
"    width: 29px; /* Double the standard groove width */\n"
"    margin: 0px; /* Covers the entire slider area */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Add page styling (below the handle) - Yellow gradient to represent the active value */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(255, 255, 102, 255), /* Light Yellow */\n"
"        stop:1 rgba(255, 204, 0, 255)    /* Darker Yellow */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Sub page styling (above the handle) - Gradient to match the original button */\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,\n"
"        stop:0 rgba(0, 0, 0, 255), /* Black gradient start */\n"
""
                        "        stop:1 rgba(255, 255, 255, 255) /* Gradient end to white */\n"
"    );\n"
"    border: 1px solid black; /* Matches the button's border */\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 29px;  /* Full width of the groove */\n"
"    height: 5px;  /* Small horizontal line for the handle */\n"
"    margin: -2px 0; /* Centers the handle on the groove */\n"
"    border-radius: 0; /* No rounded corners for a button-like shape */\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matching the button's border */\n"
"    margin: -5px 0;\n"
"}\n"
"")
        self.verticalSlider_53.setMaximum(127)
        self.verticalSlider_53.setOrientation(Qt.Vertical)
        self.verticalSlider_54 = QSlider(self.ram_info_widget)
        self.verticalSlider_54.setObjectName(u"verticalSlider_54")
        self.verticalSlider_54.setGeometry(QRect(190, 10, 21, 111))
        self.verticalSlider_54.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_54.setMaximum(127)
        self.verticalSlider_54.setOrientation(Qt.Vertical)
        self.verticalSlider_55 = QSlider(self.ram_info_widget)
        self.verticalSlider_55.setObjectName(u"verticalSlider_55")
        self.verticalSlider_55.setGeometry(QRect(220, 10, 21, 111))
        self.verticalSlider_55.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_55.setMaximum(127)
        self.verticalSlider_55.setOrientation(Qt.Vertical)
        self.verticalSlider_56 = QSlider(self.ram_info_widget)
        self.verticalSlider_56.setObjectName(u"verticalSlider_56")
        self.verticalSlider_56.setGeometry(QRect(280, 10, 21, 111))
        self.verticalSlider_56.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_56.setMaximum(127)
        self.verticalSlider_56.setOrientation(Qt.Vertical)
        self.verticalSlider_57 = QSlider(self.ram_info_widget)
        self.verticalSlider_57.setObjectName(u"verticalSlider_57")
        self.verticalSlider_57.setGeometry(QRect(310, 10, 21, 111))
        self.verticalSlider_57.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_57.setMaximum(127)
        self.verticalSlider_57.setOrientation(Qt.Vertical)
        self.verticalSlider_58 = QSlider(self.ram_info_widget)
        self.verticalSlider_58.setObjectName(u"verticalSlider_58")
        self.verticalSlider_58.setGeometry(QRect(340, 10, 21, 111))
        self.verticalSlider_58.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_58.setMaximum(127)
        self.verticalSlider_58.setOrientation(Qt.Vertical)
        self.verticalSlider_59 = QSlider(self.ram_info_widget)
        self.verticalSlider_59.setObjectName(u"verticalSlider_59")
        self.verticalSlider_59.setGeometry(QRect(400, 10, 21, 111))
        self.verticalSlider_59.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_59.setMaximum(127)
        self.verticalSlider_59.setOrientation(Qt.Vertical)
        self.verticalSlider_60 = QSlider(self.ram_info_widget)
        self.verticalSlider_60.setObjectName(u"verticalSlider_60")
        self.verticalSlider_60.setGeometry(QRect(430, 10, 21, 111))
        self.verticalSlider_60.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_60.setMaximum(127)
        self.verticalSlider_60.setOrientation(Qt.Vertical)
        self.verticalSlider_61 = QSlider(self.ram_info_widget)
        self.verticalSlider_61.setObjectName(u"verticalSlider_61")
        self.verticalSlider_61.setGeometry(QRect(490, 10, 21, 111))
        self.verticalSlider_61.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_61.setMaximum(127)
        self.verticalSlider_61.setOrientation(Qt.Vertical)
        self.verticalSlider_62 = QSlider(self.ram_info_widget)
        self.verticalSlider_62.setObjectName(u"verticalSlider_62")
        self.verticalSlider_62.setGeometry(QRect(520, 10, 21, 111))
        self.verticalSlider_62.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_62.setMaximum(127)
        self.verticalSlider_62.setOrientation(Qt.Vertical)
        self.verticalSlider_63 = QSlider(self.ram_info_widget)
        self.verticalSlider_63.setObjectName(u"verticalSlider_63")
        self.verticalSlider_63.setGeometry(QRect(550, 10, 21, 111))
        self.verticalSlider_63.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_63.setMaximum(127)
        self.verticalSlider_63.setOrientation(Qt.Vertical)
        self.verticalSlider_64 = QSlider(self.ram_info_widget)
        self.verticalSlider_64.setObjectName(u"verticalSlider_64")
        self.verticalSlider_64.setGeometry(QRect(610, 10, 21, 111))
        self.verticalSlider_64.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_64.setMaximum(127)
        self.verticalSlider_64.setOrientation(Qt.Vertical)
        self.verticalSlider_65 = QSlider(self.ram_info_widget)
        self.verticalSlider_65.setObjectName(u"verticalSlider_65")
        self.verticalSlider_65.setGeometry(QRect(640, 10, 21, 111))
        self.verticalSlider_65.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_65.setMaximum(127)
        self.verticalSlider_65.setOrientation(Qt.Vertical)
        self.verticalSlider_66 = QSlider(self.ram_info_widget)
        self.verticalSlider_66.setObjectName(u"verticalSlider_66")
        self.verticalSlider_66.setGeometry(QRect(700, 10, 21, 111))
        self.verticalSlider_66.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_66.setMaximum(127)
        self.verticalSlider_66.setOrientation(Qt.Vertical)
        self.verticalSlider_67 = QSlider(self.ram_info_widget)
        self.verticalSlider_67.setObjectName(u"verticalSlider_67")
        self.verticalSlider_67.setGeometry(QRect(730, 10, 21, 111))
        self.verticalSlider_67.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_67.setMaximum(127)
        self.verticalSlider_67.setOrientation(Qt.Vertical)
        self.verticalSlider_68 = QSlider(self.ram_info_widget)
        self.verticalSlider_68.setObjectName(u"verticalSlider_68")
        self.verticalSlider_68.setGeometry(QRect(760, 10, 21, 111))
        self.verticalSlider_68.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_68.setMaximum(127)
        self.verticalSlider_68.setOrientation(Qt.Vertical)
        self.verticalSlider_69 = QSlider(self.ram_info_widget)
        self.verticalSlider_69.setObjectName(u"verticalSlider_69")
        self.verticalSlider_69.setGeometry(QRect(820, 10, 21, 111))
        self.verticalSlider_69.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_69.setMaximum(127)
        self.verticalSlider_69.setOrientation(Qt.Vertical)
        self.verticalSlider_70 = QSlider(self.ram_info_widget)
        self.verticalSlider_70.setObjectName(u"verticalSlider_70")
        self.verticalSlider_70.setGeometry(QRect(850, 10, 21, 111))
        self.verticalSlider_70.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_70.setMaximum(127)
        self.verticalSlider_70.setOrientation(Qt.Vertical)
        self.verticalSlider_71 = QSlider(self.ram_info_widget)
        self.verticalSlider_71.setObjectName(u"verticalSlider_71")
        self.verticalSlider_71.setGeometry(QRect(910, 10, 21, 111))
        self.verticalSlider_71.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_71.setMaximum(127)
        self.verticalSlider_71.setOrientation(Qt.Vertical)
        self.verticalSlider_72 = QSlider(self.ram_info_widget)
        self.verticalSlider_72.setObjectName(u"verticalSlider_72")
        self.verticalSlider_72.setGeometry(QRect(940, 10, 21, 111))
        self.verticalSlider_72.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_72.setMaximum(127)
        self.verticalSlider_72.setOrientation(Qt.Vertical)
        self.verticalSlider_73 = QSlider(self.ram_info_widget)
        self.verticalSlider_73.setObjectName(u"verticalSlider_73")
        self.verticalSlider_73.setGeometry(QRect(970, 10, 21, 111))
        self.verticalSlider_73.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_73.setMaximum(127)
        self.verticalSlider_73.setOrientation(Qt.Vertical)
        self.verticalSlider_74 = QSlider(self.ram_info_widget)
        self.verticalSlider_74.setObjectName(u"verticalSlider_74")
        self.verticalSlider_74.setGeometry(QRect(1030, 10, 21, 111))
        self.verticalSlider_74.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_74.setMaximum(127)
        self.verticalSlider_74.setOrientation(Qt.Vertical)
        self.verticalSlider_75 = QSlider(self.ram_info_widget)
        self.verticalSlider_75.setObjectName(u"verticalSlider_75")
        self.verticalSlider_75.setGeometry(QRect(1060, 10, 21, 111))
        self.verticalSlider_75.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_75.setMaximum(127)
        self.verticalSlider_75.setOrientation(Qt.Vertical)
        self.verticalSlider_76 = QSlider(self.ram_info_widget)
        self.verticalSlider_76.setObjectName(u"verticalSlider_76")
        self.verticalSlider_76.setGeometry(QRect(1120, 10, 21, 111))
        self.verticalSlider_76.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_76.setMaximum(127)
        self.verticalSlider_76.setOrientation(Qt.Vertical)
        self.verticalSlider_77 = QSlider(self.ram_info_widget)
        self.verticalSlider_77.setObjectName(u"verticalSlider_77")
        self.verticalSlider_77.setGeometry(QRect(1150, 10, 21, 111))
        self.verticalSlider_77.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_77.setMaximum(127)
        self.verticalSlider_77.setOrientation(Qt.Vertical)
        self.verticalSlider_78 = QSlider(self.ram_info_widget)
        self.verticalSlider_78.setObjectName(u"verticalSlider_78")
        self.verticalSlider_78.setGeometry(QRect(1180, 10, 21, 111))
        self.verticalSlider_78.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_78.setMaximum(127)
        self.verticalSlider_78.setOrientation(Qt.Vertical)
        self.verticalSlider_79 = QSlider(self.ram_info_widget)
        self.verticalSlider_79.setObjectName(u"verticalSlider_79")
        self.verticalSlider_79.setGeometry(QRect(1240, 10, 21, 111))
        self.verticalSlider_79.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_79.setMaximum(127)
        self.verticalSlider_79.setOrientation(Qt.Vertical)
        self.verticalSlider_80 = QSlider(self.ram_info_widget)
        self.verticalSlider_80.setObjectName(u"verticalSlider_80")
        self.verticalSlider_80.setGeometry(QRect(1270, 10, 21, 111))
        self.verticalSlider_80.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_80.setMaximum(127)
        self.verticalSlider_80.setOrientation(Qt.Vertical)
        self.verticalSlider_81 = QSlider(self.ram_info_widget)
        self.verticalSlider_81.setObjectName(u"verticalSlider_81")
        self.verticalSlider_81.setGeometry(QRect(1330, 10, 21, 111))
        self.verticalSlider_81.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_81.setMaximum(127)
        self.verticalSlider_81.setOrientation(Qt.Vertical)
        self.verticalSlider_82 = QSlider(self.ram_info_widget)
        self.verticalSlider_82.setObjectName(u"verticalSlider_82")
        self.verticalSlider_82.setGeometry(QRect(1360, 10, 21, 111))
        self.verticalSlider_82.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_82.setMaximum(127)
        self.verticalSlider_82.setOrientation(Qt.Vertical)
        self.verticalSlider_83 = QSlider(self.ram_info_widget)
        self.verticalSlider_83.setObjectName(u"verticalSlider_83")
        self.verticalSlider_83.setGeometry(QRect(1390, 10, 21, 111))
        self.verticalSlider_83.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_83.setMaximum(127)
        self.verticalSlider_83.setOrientation(Qt.Vertical)
        self.verticalSlider_84 = QSlider(self.ram_info_widget)
        self.verticalSlider_84.setObjectName(u"verticalSlider_84")
        self.verticalSlider_84.setGeometry(QRect(1450, 10, 21, 111))
        self.verticalSlider_84.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_84.setMaximum(127)
        self.verticalSlider_84.setOrientation(Qt.Vertical)
        self.verticalSlider_85 = QSlider(self.ram_info_widget)
        self.verticalSlider_85.setObjectName(u"verticalSlider_85")
        self.verticalSlider_85.setGeometry(QRect(1480, 10, 21, 111))
        self.verticalSlider_85.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_85.setMaximum(127)
        self.verticalSlider_85.setOrientation(Qt.Vertical)
        self.verticalSlider_86 = QSlider(self.ram_info_widget)
        self.verticalSlider_86.setObjectName(u"verticalSlider_86")
        self.verticalSlider_86.setGeometry(QRect(1540, 10, 21, 111))
        self.verticalSlider_86.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_86.setMaximum(127)
        self.verticalSlider_86.setOrientation(Qt.Vertical)
        self.verticalSlider_87 = QSlider(self.ram_info_widget)
        self.verticalSlider_87.setObjectName(u"verticalSlider_87")
        self.verticalSlider_87.setGeometry(QRect(1570, 10, 21, 111))
        self.verticalSlider_87.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_87.setMaximum(127)
        self.verticalSlider_87.setOrientation(Qt.Vertical)
        self.verticalSlider_88 = QSlider(self.ram_info_widget)
        self.verticalSlider_88.setObjectName(u"verticalSlider_88")
        self.verticalSlider_88.setGeometry(QRect(1600, 10, 21, 111))
        self.verticalSlider_88.setStyleSheet(u"/* Groove styling */\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid black; /* Matches the button border */\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Handle styling */\n"
"QSlider::handle:vertical {\n"
"    background: none;\n"
"    width: 20px;\n"
"    height: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 0;\n"
"    background-color: transparent;\n"
"    border: 1px solid black; /* Matches the button border */\n"
"	 margin: -5px 0;\n"
"}\n"
"\n"
"/* Add-page (above the handle) - Initial style similar to button */\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 150, 0, 250), /* Matches initial button color */\n"
"        stop:1 rgba(255, 255, 255, 255)\n"
"    );\n"
"    border: 1px solid black; /* Matches the button border */\n"
"}\n"
"\n"
"/* Sub-page (below the handle) - Initial style, solid black */\n"
"QSlider::sub-page:vertic"
                        "al {\n"
"    background: black;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* Dynamic color change as value increases */\n"
"QSlider::add-page:vertical:active {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,\n"
"        stop:0.852273 rgba(0, 100, 0, 250), /* Dark green as value increases */\n"
"        stop:1 rgba(0, 255, 0, 255) /* Bright green transition */\n"
"    );\n"
"}\n"
"")
        self.verticalSlider_88.setMaximum(127)
        self.verticalSlider_88.setOrientation(Qt.Vertical)
        self.a4_7.raise_()
        self.b4_7.raise_()
        self.c4_6.raise_()
        self.a4_6.raise_()
        self.b4_6.raise_()
        self.a4_5.raise_()
        self.c4_5.raise_()
        self.b5.raise_()
        self.c4_4.raise_()
        self.d4_4.raise_()
        self.a4_4.raise_()
        self.a4_3.raise_()
        self.c4_3.raise_()
        self.c4_2.raise_()
        self.d4_2.raise_()
        self.a4_2.raise_()
        self.a5.raise_()
        self.g5.raise_()
        self.f5.raise_()
        self.e5.raise_()
        self.d5.raise_()
        self.c5.raise_()
        self.b4.raise_()
        self.g4.raise_()
        self.f4.raise_()
        self.a4.raise_()
        self.d4.raise_()
        self.e4.raise_()
        self.c4.raise_()
        self.c6.raise_()
        self.b4_2.raise_()
        self.f4_2.raise_()
        self.e4_2.raise_()
        self.g4_2.raise_()
        self.b4_3.raise_()
        self.f4_3.raise_()
        self.e4_3.raise_()
        self.g4_3.raise_()
        self.d4_3.raise_()
        self.b4_4.raise_()
        self.f4_4.raise_()
        self.e4_4.raise_()
        self.g4_4.raise_()
        self.b4_5.raise_()
        self.f4_5.raise_()
        self.e4_5.raise_()
        self.g4_5.raise_()
        self.d4_5.raise_()
        self.f4_6.raise_()
        self.e4_6.raise_()
        self.g4_6.raise_()
        self.d4_6.raise_()
        self.verticalSlider.raise_()
        self.verticalSlider_2.raise_()
        self.verticalSlider_4.raise_()
        self.verticalSlider_5.raise_()
        self.verticalSlider_6.raise_()
        self.verticalSlider_7.raise_()
        self.verticalSlider_8.raise_()
        self.verticalSlider_9.raise_()
        self.g40_6.raise_()
        self.verticalSlider_10.raise_()
        self.verticalSlider_11.raise_()
        self.verticalSlider_12.raise_()
        self.verticalSlider_13.raise_()
        self.d40_5.raise_()
        self.c40_5.raise_()
        self.verticalSlider_14.raise_()
        self.verticalSlider_15.raise_()
        self.verticalSlider_16.raise_()
        self.verticalSlider_17.raise_()
        self.verticalSlider_18.raise_()
        self.verticalSlider_19.raise_()
        self.verticalSlider_20.raise_()
        self.verticalSlider_21.raise_()
        self.verticalSlider_22.raise_()
        self.verticalSlider_23.raise_()
        self.verticalSlider_24.raise_()
        self.a40_4.raise_()
        self.verticalSlider_25.raise_()
        self.verticalSlider_26.raise_()
        self.verticalSlider_27.raise_()
        self.d40_3.raise_()
        self.verticalSlider_28.raise_()
        self.verticalSlider_29.raise_()
        self.verticalSlider_30.raise_()
        self.g40_3.raise_()
        self.verticalSlider_31.raise_()
        self.a40_3.raise_()
        self.verticalSlider_32.raise_()
        self.verticalSlider_33.raise_()
        self.verticalSlider_34.raise_()
        self.verticalSlider_35.raise_()
        self.verticalSlider_36.raise_()
        self.verticalSlider_37.raise_()
        self.verticalSlider_38.raise_()
        self.verticalSlider_39.raise_()
        self.verticalSlider_40.raise_()
        self.verticalSlider_41.raise_()
        self.verticalSlider_42.raise_()
        self.verticalSlider_43.raise_()
        self.verticalSlider_44.raise_()
        self.verticalSlider_45.raise_()
        self.a40.raise_()
        self.verticalSlider_46.raise_()
        self.verticalSlider_47.raise_()
        self.verticalSlider_48.raise_()
        self.d50.raise_()
        self.verticalSlider_49.raise_()
        self.verticalSlider_50.raise_()
        self.f50.raise_()
        self.verticalSlider_51.raise_()
        self.verticalSlider_52.raise_()
        self.verticalSlider_53.raise_()
        self.a40_6.raise_()
        self.a40_7.raise_()
        self.c40_6.raise_()
        self.f40_6.raise_()
        self.c40_4.raise_()
        self.g40_5.raise_()
        self.g40_4.raise_()
        self.c40_3.raise_()
        self.c40_2.raise_()
        self.a40_2.raise_()
        self.c40.raise_()
        self.f40.raise_()
        self.g40.raise_()
        self.c50.raise_()
        self.a50.raise_()
        self.a40_5.raise_()
        self.d40.raise_()
        self.d40_2.raise_()
        self.d40_4.raise_()
        self.d40_6.raise_()
        self.f40_2.raise_()
        self.f40_3.raise_()
        self.f40_4.raise_()
        self.f40_5.raise_()
        self.g40_2.raise_()
        self.g50.raise_()
        self.verticalSlider_88.raise_()
        self.verticalSlider_87.raise_()
        self.verticalSlider_86.raise_()
        self.verticalSlider_85.raise_()
        self.verticalSlider_84.raise_()
        self.verticalSlider_83.raise_()
        self.verticalSlider_82.raise_()
        self.verticalSlider_81.raise_()
        self.verticalSlider_80.raise_()
        self.verticalSlider_79.raise_()
        self.verticalSlider_78.raise_()
        self.verticalSlider_77.raise_()
        self.verticalSlider_76.raise_()
        self.verticalSlider_75.raise_()
        self.verticalSlider_74.raise_()
        self.verticalSlider_73.raise_()
        self.verticalSlider_72.raise_()
        self.verticalSlider_71.raise_()
        self.verticalSlider_70.raise_()
        self.verticalSlider_69.raise_()
        self.verticalSlider_68.raise_()
        self.verticalSlider_67.raise_()
        self.verticalSlider_66.raise_()
        self.verticalSlider_65.raise_()
        self.verticalSlider_64.raise_()
        self.verticalSlider_63.raise_()
        self.verticalSlider_62.raise_()
        self.verticalSlider_61.raise_()
        self.verticalSlider_60.raise_()
        self.verticalSlider_59.raise_()
        self.verticalSlider_58.raise_()
        self.verticalSlider_57.raise_()
        self.verticalSlider_56.raise_()
        self.verticalSlider_55.raise_()
        self.verticalSlider_54.raise_()
        self.verticalSlider_3.raise_()
        self.lineEdit_3 = QLineEdit(self.encoders_buttons)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QRect(90, 518, 41, 16))
        self.lineEdit_7 = QLineEdit(self.encoders_buttons)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_7.setGeometry(QRect(130, 518, 41, 16))
        self.lineEdit_8 = QLineEdit(self.encoders_buttons)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_8.setGeometry(QRect(170, 518, 41, 16))
        self.lineEdit_9 = QLineEdit(self.encoders_buttons)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_9.setGeometry(QRect(200, 518, 41, 16))
        self.lineEdit_10 = QLineEdit(self.encoders_buttons)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setEnabled(True)
        self.lineEdit_10.setGeometry(QRect(230, 518, 41, 16))
        self.lineEdit_11 = QLineEdit(self.encoders_buttons)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setEnabled(True)
        self.lineEdit_11.setGeometry(QRect(260, 518, 41, 16))
        self.lineEdit_12 = QLineEdit(self.encoders_buttons)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setEnabled(True)
        self.lineEdit_12.setGeometry(QRect(290, 518, 41, 16))
        self.lineEdit_13 = QLineEdit(self.encoders_buttons)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setEnabled(True)
        self.lineEdit_13.setGeometry(QRect(320, 518, 41, 16))
        self.lineEdit_14 = QLineEdit(self.encoders_buttons)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setEnabled(True)
        self.lineEdit_14.setGeometry(QRect(350, 518, 41, 16))
        self.lineEdit_15 = QLineEdit(self.encoders_buttons)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setEnabled(True)
        self.lineEdit_15.setGeometry(QRect(380, 518, 41, 16))
        self.lineEdit_16 = QLineEdit(self.encoders_buttons)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setEnabled(True)
        self.lineEdit_16.setGeometry(QRect(410, 518, 41, 16))
        self.lineEdit_17 = QLineEdit(self.encoders_buttons)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setEnabled(True)
        self.lineEdit_17.setGeometry(QRect(440, 518, 41, 16))
        self.lineEdit_18 = QLineEdit(self.encoders_buttons)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setEnabled(True)
        self.lineEdit_18.setGeometry(QRect(470, 518, 41, 16))
        self.lineEdit_19 = QLineEdit(self.encoders_buttons)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setEnabled(True)
        self.lineEdit_19.setGeometry(QRect(500, 518, 41, 16))
        self.lineEdit_20 = QLineEdit(self.encoders_buttons)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setEnabled(True)
        self.lineEdit_20.setGeometry(QRect(530, 518, 41, 16))
        self.lineEdit_21 = QLineEdit(self.encoders_buttons)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setEnabled(True)
        self.lineEdit_21.setGeometry(QRect(560, 518, 41, 16))
        self.lineEdit_22 = QLineEdit(self.encoders_buttons)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setEnabled(True)
        self.lineEdit_22.setGeometry(QRect(590, 518, 41, 16))
        self.lineEdit_23 = QLineEdit(self.encoders_buttons)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setEnabled(True)
        self.lineEdit_23.setGeometry(QRect(620, 518, 41, 16))
        self.lineEdit_24 = QLineEdit(self.encoders_buttons)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setEnabled(True)
        self.lineEdit_24.setGeometry(QRect(650, 518, 41, 16))
        self.lineEdit_25 = QLineEdit(self.encoders_buttons)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setEnabled(True)
        self.lineEdit_25.setGeometry(QRect(680, 518, 41, 16))
        self.lineEdit_26 = QLineEdit(self.encoders_buttons)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setEnabled(True)
        self.lineEdit_26.setGeometry(QRect(710, 518, 41, 16))
        self.lineEdit_27 = QLineEdit(self.encoders_buttons)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setEnabled(True)
        self.lineEdit_27.setGeometry(QRect(740, 518, 41, 16))
        self.lineEdit_28 = QLineEdit(self.encoders_buttons)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setEnabled(True)
        self.lineEdit_28.setGeometry(QRect(770, 518, 41, 16))
        self.lineEdit_29 = QLineEdit(self.encoders_buttons)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setEnabled(True)
        self.lineEdit_29.setGeometry(QRect(800, 518, 41, 16))
        self.lineEdit_30 = QLineEdit(self.encoders_buttons)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setEnabled(True)
        self.lineEdit_30.setGeometry(QRect(830, 518, 41, 16))
        self.lineEdit_31 = QLineEdit(self.encoders_buttons)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setEnabled(True)
        self.lineEdit_31.setGeometry(QRect(860, 518, 41, 16))
        self.lineEdit_32 = QLineEdit(self.encoders_buttons)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setEnabled(True)
        self.lineEdit_32.setGeometry(QRect(890, 518, 41, 16))
        self.lineEdit_33 = QLineEdit(self.encoders_buttons)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setEnabled(True)
        self.lineEdit_33.setGeometry(QRect(920, 518, 41, 16))
        self.lineEdit_34 = QLineEdit(self.encoders_buttons)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setEnabled(True)
        self.lineEdit_34.setGeometry(QRect(950, 518, 41, 16))
        self.lineEdit_35 = QLineEdit(self.encoders_buttons)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setEnabled(True)
        self.lineEdit_35.setGeometry(QRect(980, 518, 41, 16))
        self.lineEdit_36 = QLineEdit(self.encoders_buttons)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setEnabled(True)
        self.lineEdit_36.setGeometry(QRect(1010, 518, 41, 16))
        self.lineEdit_37 = QLineEdit(self.encoders_buttons)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setEnabled(True)
        self.lineEdit_37.setGeometry(QRect(1040, 518, 41, 16))
        self.lineEdit_38 = QLineEdit(self.encoders_buttons)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setEnabled(True)
        self.lineEdit_38.setGeometry(QRect(1070, 518, 41, 16))
        self.lineEdit_39 = QLineEdit(self.encoders_buttons)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setEnabled(True)
        self.lineEdit_39.setGeometry(QRect(1100, 518, 41, 16))
        self.lineEdit_40 = QLineEdit(self.encoders_buttons)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setEnabled(True)
        self.lineEdit_40.setGeometry(QRect(1130, 518, 41, 16))
        self.lineEdit_41 = QLineEdit(self.encoders_buttons)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setEnabled(True)
        self.lineEdit_41.setGeometry(QRect(1160, 518, 41, 16))
        self.lineEdit_42 = QLineEdit(self.encoders_buttons)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setEnabled(True)
        self.lineEdit_42.setGeometry(QRect(1190, 518, 41, 16))
        self.lineEdit_43 = QLineEdit(self.encoders_buttons)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setEnabled(True)
        self.lineEdit_43.setGeometry(QRect(1220, 518, 41, 16))
        self.lineEdit_44 = QLineEdit(self.encoders_buttons)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setEnabled(True)
        self.lineEdit_44.setGeometry(QRect(1250, 518, 41, 16))
        self.lineEdit_45 = QLineEdit(self.encoders_buttons)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setEnabled(True)
        self.lineEdit_45.setGeometry(QRect(1280, 518, 41, 16))
        self.lineEdit_46 = QLineEdit(self.encoders_buttons)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setEnabled(True)
        self.lineEdit_46.setGeometry(QRect(1310, 518, 41, 16))
        self.lineEdit_47 = QLineEdit(self.encoders_buttons)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setEnabled(True)
        self.lineEdit_47.setGeometry(QRect(1340, 518, 41, 16))
        self.lineEdit_48 = QLineEdit(self.encoders_buttons)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setEnabled(True)
        self.lineEdit_48.setGeometry(QRect(1370, 518, 41, 16))
        self.lineEdit_49 = QLineEdit(self.encoders_buttons)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setEnabled(True)
        self.lineEdit_49.setGeometry(QRect(1400, 518, 41, 16))
        self.lineEdit_50 = QLineEdit(self.encoders_buttons)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setEnabled(True)
        self.lineEdit_50.setGeometry(QRect(1430, 518, 41, 16))
        self.lineEdit_51 = QLineEdit(self.encoders_buttons)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setEnabled(True)
        self.lineEdit_51.setGeometry(QRect(1460, 518, 41, 16))
        self.lineEdit_52 = QLineEdit(self.encoders_buttons)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setEnabled(True)
        self.lineEdit_52.setGeometry(QRect(1490, 518, 41, 16))
        self.lineEdit_53 = QLineEdit(self.encoders_buttons)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setEnabled(True)
        self.lineEdit_53.setGeometry(QRect(1520, 518, 41, 16))
        self.lineEdit_54 = QLineEdit(self.encoders_buttons)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setEnabled(True)
        self.lineEdit_54.setGeometry(QRect(1550, 518, 41, 16))
        self.lineEdit_55 = QLineEdit(self.encoders_buttons)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setEnabled(True)
        self.lineEdit_55.setGeometry(QRect(1580, 518, 41, 16))
        font5 = QFont()
        font5.setPointSize(7)
        self.lineEdit_55.setFont(font5)
        self.lineEdit_56 = QLineEdit(self.encoders_buttons)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setEnabled(True)
        self.lineEdit_56.setGeometry(QRect(1610, 518, 41, 16))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_56.sizePolicy().hasHeightForWidth())
        self.lineEdit_56.setSizePolicy(sizePolicy2)
        self.lineEdit_56.setMinimumSize(QSize(41, 0))
        self.lineEdit_56.setMaximumSize(QSize(31, 16))
        self.lineEdit_56.setFont(font5)
        self.lineEdit_57 = QLineEdit(self.encoders_buttons)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setEnabled(True)
        self.lineEdit_57.setGeometry(QRect(1640, 518, 41, 16))
        self.lineEdit_57.setFont(font5)
        self.lineEdit_58 = QLineEdit(self.encoders_buttons)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setEnabled(True)
        self.lineEdit_58.setGeometry(QRect(120, 308, 41, 20))
        self.lineEdit_59 = QLineEdit(self.encoders_buttons)
        self.lineEdit_59.setObjectName(u"lineEdit_59")
        self.lineEdit_59.setEnabled(True)
        self.lineEdit_59.setGeometry(QRect(180, 308, 41, 20))
        self.lineEdit_60 = QLineEdit(self.encoders_buttons)
        self.lineEdit_60.setObjectName(u"lineEdit_60")
        self.lineEdit_60.setEnabled(True)
        self.lineEdit_60.setGeometry(QRect(210, 308, 41, 20))
        self.lineEdit_61 = QLineEdit(self.encoders_buttons)
        self.lineEdit_61.setObjectName(u"lineEdit_61")
        self.lineEdit_61.setEnabled(True)
        self.lineEdit_61.setGeometry(QRect(270, 308, 41, 20))
        self.lineEdit_62 = QLineEdit(self.encoders_buttons)
        self.lineEdit_62.setObjectName(u"lineEdit_62")
        self.lineEdit_62.setEnabled(True)
        self.lineEdit_62.setGeometry(QRect(300, 308, 41, 20))
        self.lineEdit_63 = QLineEdit(self.encoders_buttons)
        self.lineEdit_63.setObjectName(u"lineEdit_63")
        self.lineEdit_63.setEnabled(True)
        self.lineEdit_63.setGeometry(QRect(340, 308, 41, 20))
        self.lineEdit_64 = QLineEdit(self.encoders_buttons)
        self.lineEdit_64.setObjectName(u"lineEdit_64")
        self.lineEdit_64.setEnabled(True)
        self.lineEdit_64.setGeometry(QRect(400, 308, 41, 20))
        self.lineEdit_65 = QLineEdit(self.encoders_buttons)
        self.lineEdit_65.setObjectName(u"lineEdit_65")
        self.lineEdit_65.setEnabled(True)
        self.lineEdit_65.setGeometry(QRect(430, 308, 41, 20))
        self.lineEdit_66 = QLineEdit(self.encoders_buttons)
        self.lineEdit_66.setObjectName(u"lineEdit_66")
        self.lineEdit_66.setEnabled(True)
        self.lineEdit_66.setGeometry(QRect(480, 308, 41, 20))
        self.lineEdit_67 = QLineEdit(self.encoders_buttons)
        self.lineEdit_67.setObjectName(u"lineEdit_67")
        self.lineEdit_67.setEnabled(True)
        self.lineEdit_67.setGeometry(QRect(520, 308, 41, 20))
        self.lineEdit_68 = QLineEdit(self.encoders_buttons)
        self.lineEdit_68.setObjectName(u"lineEdit_68")
        self.lineEdit_68.setEnabled(True)
        self.lineEdit_68.setGeometry(QRect(550, 308, 41, 20))
        self.lineEdit_69 = QLineEdit(self.encoders_buttons)
        self.lineEdit_69.setObjectName(u"lineEdit_69")
        self.lineEdit_69.setEnabled(True)
        self.lineEdit_69.setGeometry(QRect(610, 308, 41, 20))
        self.lineEdit_70 = QLineEdit(self.encoders_buttons)
        self.lineEdit_70.setObjectName(u"lineEdit_70")
        self.lineEdit_70.setEnabled(True)
        self.lineEdit_70.setGeometry(QRect(640, 308, 41, 20))
        self.lineEdit_71 = QLineEdit(self.encoders_buttons)
        self.lineEdit_71.setObjectName(u"lineEdit_71")
        self.lineEdit_71.setEnabled(True)
        self.lineEdit_71.setGeometry(QRect(690, 308, 41, 20))
        self.lineEdit_72 = QLineEdit(self.encoders_buttons)
        self.lineEdit_72.setObjectName(u"lineEdit_72")
        self.lineEdit_72.setEnabled(True)
        self.lineEdit_72.setGeometry(QRect(720, 308, 41, 20))
        self.lineEdit_73 = QLineEdit(self.encoders_buttons)
        self.lineEdit_73.setObjectName(u"lineEdit_73")
        self.lineEdit_73.setEnabled(True)
        self.lineEdit_73.setGeometry(QRect(750, 308, 41, 20))
        self.lineEdit_74 = QLineEdit(self.encoders_buttons)
        self.lineEdit_74.setObjectName(u"lineEdit_74")
        self.lineEdit_74.setEnabled(True)
        self.lineEdit_74.setGeometry(QRect(810, 308, 41, 20))
        self.lineEdit_75 = QLineEdit(self.encoders_buttons)
        self.lineEdit_75.setObjectName(u"lineEdit_75")
        self.lineEdit_75.setEnabled(True)
        self.lineEdit_75.setGeometry(QRect(850, 308, 41, 20))
        self.lineEdit_76 = QLineEdit(self.encoders_buttons)
        self.lineEdit_76.setObjectName(u"lineEdit_76")
        self.lineEdit_76.setEnabled(True)
        self.lineEdit_76.setGeometry(QRect(900, 308, 41, 20))
        self.lineEdit_77 = QLineEdit(self.encoders_buttons)
        self.lineEdit_77.setObjectName(u"lineEdit_77")
        self.lineEdit_77.setEnabled(True)
        self.lineEdit_77.setGeometry(QRect(940, 308, 41, 20))
        self.lineEdit_78 = QLineEdit(self.encoders_buttons)
        self.lineEdit_78.setObjectName(u"lineEdit_78")
        self.lineEdit_78.setEnabled(True)
        self.lineEdit_78.setGeometry(QRect(970, 308, 41, 20))
        self.lineEdit_79 = QLineEdit(self.encoders_buttons)
        self.lineEdit_79.setObjectName(u"lineEdit_79")
        self.lineEdit_79.setEnabled(True)
        self.lineEdit_79.setGeometry(QRect(1020, 308, 41, 20))
        self.lineEdit_80 = QLineEdit(self.encoders_buttons)
        self.lineEdit_80.setObjectName(u"lineEdit_80")
        self.lineEdit_80.setEnabled(True)
        self.lineEdit_80.setGeometry(QRect(1050, 308, 41, 20))
        self.lineEdit_81 = QLineEdit(self.encoders_buttons)
        self.lineEdit_81.setObjectName(u"lineEdit_81")
        self.lineEdit_81.setEnabled(True)
        self.lineEdit_81.setGeometry(QRect(1110, 308, 41, 20))
        self.lineEdit_82 = QLineEdit(self.encoders_buttons)
        self.lineEdit_82.setObjectName(u"lineEdit_82")
        self.lineEdit_82.setEnabled(True)
        self.lineEdit_82.setGeometry(QRect(1140, 308, 41, 20))
        self.lineEdit_83 = QLineEdit(self.encoders_buttons)
        self.lineEdit_83.setObjectName(u"lineEdit_83")
        self.lineEdit_83.setEnabled(True)
        self.lineEdit_83.setGeometry(QRect(1180, 308, 41, 20))
        self.lineEdit_84 = QLineEdit(self.encoders_buttons)
        self.lineEdit_84.setObjectName(u"lineEdit_84")
        self.lineEdit_84.setEnabled(True)
        self.lineEdit_84.setGeometry(QRect(1230, 308, 41, 20))
        self.lineEdit_85 = QLineEdit(self.encoders_buttons)
        self.lineEdit_85.setObjectName(u"lineEdit_85")
        self.lineEdit_85.setEnabled(True)
        self.lineEdit_85.setGeometry(QRect(1270, 308, 41, 20))
        self.lineEdit_86 = QLineEdit(self.encoders_buttons)
        self.lineEdit_86.setObjectName(u"lineEdit_86")
        self.lineEdit_86.setEnabled(True)
        self.lineEdit_86.setGeometry(QRect(1320, 308, 41, 20))
        self.lineEdit_87 = QLineEdit(self.encoders_buttons)
        self.lineEdit_87.setObjectName(u"lineEdit_87")
        self.lineEdit_87.setEnabled(True)
        self.lineEdit_87.setGeometry(QRect(1350, 308, 41, 20))
        self.lineEdit_88 = QLineEdit(self.encoders_buttons)
        self.lineEdit_88.setObjectName(u"lineEdit_88")
        self.lineEdit_88.setEnabled(True)
        self.lineEdit_88.setGeometry(QRect(1390, 308, 41, 20))
        self.lineEdit_89 = QLineEdit(self.encoders_buttons)
        self.lineEdit_89.setObjectName(u"lineEdit_89")
        self.lineEdit_89.setEnabled(True)
        self.lineEdit_89.setGeometry(QRect(1450, 308, 41, 20))
        self.lineEdit_90 = QLineEdit(self.encoders_buttons)
        self.lineEdit_90.setObjectName(u"lineEdit_90")
        self.lineEdit_90.setEnabled(True)
        self.lineEdit_90.setGeometry(QRect(1480, 308, 41, 20))
        self.lineEdit_91 = QLineEdit(self.encoders_buttons)
        self.lineEdit_91.setObjectName(u"lineEdit_91")
        self.lineEdit_91.setEnabled(True)
        self.lineEdit_91.setGeometry(QRect(1530, 308, 41, 20))
        self.lineEdit_92 = QLineEdit(self.encoders_buttons)
        self.lineEdit_92.setObjectName(u"lineEdit_92")
        self.lineEdit_92.setEnabled(True)
        self.lineEdit_92.setGeometry(QRect(1570, 308, 41, 20))
        self.lineEdit_93 = QLineEdit(self.encoders_buttons)
        self.lineEdit_93.setObjectName(u"lineEdit_93")
        self.lineEdit_93.setEnabled(True)
        self.lineEdit_93.setGeometry(QRect(1600, 308, 41, 20))
        self.file_name = QLabel(self.encoders_buttons)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(210, -4, 281, 16))
        self.file_name.setFont(font)
        self.label_weight = QLabel(self.encoders_buttons)
        self.label_weight.setObjectName(u"label_weight")
        self.label_weight.setGeometry(QRect(1530, -4, 151, 16))
        self.label_weight.setFont(font)
        self.label_11 = QLabel(self.encoders_buttons)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(1430, -4, 81, 16))
        self.label_11.setFont(font)
        self.groupBox = QGroupBox(self.encoders_buttons)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(90, 540, 1200, 271))
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	background-color: #fafafa;\n"
"    border: 2px solid #D0D0D0;  /* light gray border */\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"    font-weight: bold;\n"
"    color: #555;\n"
"    padding: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"}\n"
"")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_velocity = QLineEdit(self.groupBox)
        self.lineEdit_velocity.setObjectName(u"lineEdit_velocity")
        self.lineEdit_velocity.setEnabled(False)
        font6 = QFont()
        font6.setPointSize(72)
        font6.setBold(True)
        font6.setWeight(75)
        self.lineEdit_velocity.setFont(font6)
        self.lineEdit_velocity.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_velocity, 2, 3, 1, 1)

        self.lineEdit_note = QLineEdit(self.groupBox)
        self.lineEdit_note.setObjectName(u"lineEdit_note")
        self.lineEdit_note.setEnabled(False)
        self.lineEdit_note.setFont(font6)
        self.lineEdit_note.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_note, 0, 3, 1, 1)

        self.label_94 = QLabel(self.groupBox)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font4)

        self.gridLayout.addWidget(self.label_94, 4, 0, 1, 1)

        self.label_93 = QLabel(self.groupBox)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font4)

        self.gridLayout.addWidget(self.label_93, 0, 0, 1, 1)

        self.lineEdit_velo = QLineEdit(self.groupBox)
        self.lineEdit_velo.setObjectName(u"lineEdit_velo")
        self.lineEdit_velo.setEnabled(False)
        self.lineEdit_velo.setFont(font6)
        self.lineEdit_velo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_velo, 4, 1, 1, 1)

        self.lineEdit_aftertouch = QLineEdit(self.groupBox)
        self.lineEdit_aftertouch.setObjectName(u"lineEdit_aftertouch")
        self.lineEdit_aftertouch.setEnabled(False)
        self.lineEdit_aftertouch.setFont(font6)
        self.lineEdit_aftertouch.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_aftertouch, 0, 1, 1, 1)

        self.label_77 = QLabel(self.groupBox)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font4)

        self.gridLayout.addWidget(self.label_77, 2, 2, 1, 1)

        self.lineEdit_resistance = QLineEdit(self.groupBox)
        self.lineEdit_resistance.setObjectName(u"lineEdit_resistance")
        self.lineEdit_resistance.setEnabled(False)
        font7 = QFont()
        font7.setPointSize(65)
        font7.setBold(True)
        font7.setWeight(75)
        self.lineEdit_resistance.setFont(font7)
        self.lineEdit_resistance.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_resistance, 2, 1, 1, 1)

        self.label_95 = QLabel(self.groupBox)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font4)

        self.gridLayout.addWidget(self.label_95, 0, 2, 1, 1)

        self.label_78 = QLabel(self.groupBox)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font4)

        self.gridLayout.addWidget(self.label_78, 2, 0, 1, 1)

        self.label_46 = QLabel(self.groupBox)
        self.label_46.setObjectName(u"label_46")
        palette = QPalette()
        brush = QBrush(QColor(255, 165, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(255, 165, 0, 128))
        brush1.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(255, 165, 0, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(255, 165, 0, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.label_46.setPalette(palette)
        font8 = QFont()
        font8.setFamily(u"MS Shell Dlg 2")
        font8.setPointSize(16)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setWeight(75)
        font8.setStrikeOut(False)
        font8.setKerning(True)
        self.label_46.setFont(font8)
        self.label_46.setStyleSheet(u"QLabel {\n"
"    color: orange;\n"
"    font-weight: bold;\n"
"    font-size: 16pt;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_46, 5, 0, 1, 1)

        self.lineEdit_counter_display = QLineEdit(self.groupBox)
        self.lineEdit_counter_display.setObjectName(u"lineEdit_counter_display")
        self.lineEdit_counter_display.setEnabled(False)
        self.lineEdit_counter_display.setFont(font)
        self.lineEdit_counter_display.setStyleSheet(u"QLineEdit {\n"
" border: 2px solid orange;\n"
"                       border-radius: 5px;\n"
"                       padding: 2px;\n"
"                       font-size: 40px;\n"
"                       background-color: #fff8e1;\n"
"                       font-weight: bold;\n"
"                       color: orange;\n"
"                       qproperty-alignment: 'AlignCenter';\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_counter_display, 5, 1, 1, 1)

        self.label_message = QLabel(self.groupBox)
        self.label_message.setObjectName(u"label_message")

        self.gridLayout.addWidget(self.label_message, 5, 3, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout)

        self.groupBox_2 = QGroupBox(self.encoders_buttons)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(1310, 540, 371, 271))
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #D0D0D0;  /* light gray border */\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"    font-weight: bold;\n"
"    color: #555;\n"
"    padding: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"}\n"
"")
        self.horizontalLayoutWidget = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 341, 231))
        self.verticalLayout_3 = QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioAcoustic = QRadioButton(self.horizontalLayoutWidget)
        self.radioAcoustic.setObjectName(u"radioAcoustic")
        self.radioAcoustic.setStyleSheet(u"/* Hide the default radio circle */\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"/* Base style */\n"
"QRadioButton {\n"
"    padding: 8px 18px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;\n"
"    background-color: transparent;\n"
"    color: #FFA500;\n"
"    font-weight: bold;\n"
"    min-width: 110px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QRadioButton:hover {\n"
"    background-color: rgba(255, 165, 0, 0.15);\n"
"}\n"
"\n"
"/* Checked = Electrical (Orange) */\n"
"QRadioButton#radioElectrical:checked {\n"
"    background-color: #FFA500;\n"
"    color: white;\n"
"    border: 2px solid #FFA500;\n"
"}\n"
"\n"
"/* Checked = Acoustic (Green) */\n"
"QRadioButton#radioAcoustic:checked {\n"
"    background-color: #10B981;\n"
"    color: white;\n"
"    border: 2px solid #10B981;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.radioAcoustic)

        self.radioElectrical = QRadioButton(self.horizontalLayoutWidget)
        self.radioElectrical.setObjectName(u"radioElectrical")
        self.radioElectrical.setStyleSheet(u"/* Hide the default radio circle */\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"/* Base style */\n"
"QRadioButton {\n"
"    padding: 8px 18px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFA500;\n"
"    background-color: transparent;\n"
"    color: #FFA500;\n"
"    font-weight: bold;\n"
"    min-width: 110px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QRadioButton:hover {\n"
"    background-color: rgba(255, 165, 0, 0.15);\n"
"}\n"
"\n"
"/* Checked = Electrical (Orange) */\n"
"QRadioButton#radioElectrical:checked {\n"
"    background-color: #FFA500;\n"
"    color: white;\n"
"    border: 2px solid #FFA500;\n"
"}\n"
"\n"
"/* Checked = Acoustic (Green) */\n"
"QRadioButton#radioAcoustic:checked {\n"
"    background-color: #10B981;\n"
"    color: white;\n"
"    border: 2px solid #10B981;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.radioElectrical)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.newdevice2 = QPushButton(self.horizontalLayoutWidget)
        self.newdevice2.setObjectName(u"newdevice2")

        self.verticalLayout_6.addWidget(self.newdevice2)

        self.reset_pushButton = QPushButton(self.horizontalLayoutWidget)
        self.reset_pushButton.setObjectName(u"reset_pushButton")
        self.reset_pushButton.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.reset_pushButton)

        self.new_file_ini = QPushButton(self.horizontalLayoutWidget)
        self.new_file_ini.setObjectName(u"new_file_ini")

        self.verticalLayout_6.addWidget(self.new_file_ini)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.encoders_buttons)
        self.label_15.raise_()
        self.ram_info_widget.raise_()
        self.lineEdit_57.raise_()
        self.lineEdit_58.raise_()
        self.lineEdit_60.raise_()
        self.lineEdit_63.raise_()
        self.lineEdit_65.raise_()
        self.lineEdit_68.raise_()
        self.lineEdit_70.raise_()
        self.lineEdit_73.raise_()
        self.lineEdit_75.raise_()
        self.lineEdit_78.raise_()
        self.lineEdit_80.raise_()
        self.lineEdit_83.raise_()
        self.lineEdit_85.raise_()
        self.lineEdit_88.raise_()
        self.lineEdit_90.raise_()
        self.lineEdit_91.raise_()
        self.lineEdit_93.raise_()
        self.lineEdit_92.raise_()
        self.lineEdit_56.raise_()
        self.lineEdit_55.raise_()
        self.lineEdit_54.raise_()
        self.lineEdit_53.raise_()
        self.lineEdit_52.raise_()
        self.lineEdit_51.raise_()
        self.lineEdit_50.raise_()
        self.lineEdit_49.raise_()
        self.lineEdit_48.raise_()
        self.lineEdit_89.raise_()
        self.lineEdit_47.raise_()
        self.lineEdit_87.raise_()
        self.lineEdit_86.raise_()
        self.lineEdit_84.raise_()
        self.lineEdit_46.raise_()
        self.lineEdit_45.raise_()
        self.lineEdit_44.raise_()
        self.lineEdit_43.raise_()
        self.lineEdit_82.raise_()
        self.lineEdit_81.raise_()
        self.lineEdit_42.raise_()
        self.lineEdit_41.raise_()
        self.lineEdit_40.raise_()
        self.lineEdit_39.raise_()
        self.lineEdit_38.raise_()
        self.lineEdit_37.raise_()
        self.lineEdit_36.raise_()
        self.lineEdit_35.raise_()
        self.lineEdit_34.raise_()
        self.lineEdit_33.raise_()
        self.lineEdit_32.raise_()
        self.lineEdit_31.raise_()
        self.lineEdit_30.raise_()
        self.lineEdit_29.raise_()
        self.lineEdit_28.raise_()
        self.lineEdit_27.raise_()
        self.lineEdit_26.raise_()
        self.lineEdit_25.raise_()
        self.lineEdit_24.raise_()
        self.lineEdit_23.raise_()
        self.lineEdit_22.raise_()
        self.lineEdit_21.raise_()
        self.lineEdit_20.raise_()
        self.lineEdit_19.raise_()
        self.lineEdit_18.raise_()
        self.lineEdit_17.raise_()
        self.lineEdit_16.raise_()
        self.lineEdit_15.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_13.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_79.raise_()
        self.lineEdit_77.raise_()
        self.lineEdit_76.raise_()
        self.lineEdit_74.raise_()
        self.lineEdit_72.raise_()
        self.lineEdit_71.raise_()
        self.lineEdit_69.raise_()
        self.lineEdit_67.raise_()
        self.lineEdit_66.raise_()
        self.lineEdit_64.raise_()
        self.lineEdit_62.raise_()
        self.lineEdit_61.raise_()
        self.lineEdit_59.raise_()
        self.file_name.raise_()
        self.label_weight.raise_()
        self.label_11.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.estorage = QWidget()
        self.estorage.setObjectName(u"estorage")
        self.verticalLayout_10 = QVBoxLayout(self.estorage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.stackedWidget.addWidget(self.estorage)
        self.fsensors = QWidget()
        self.fsensors.setObjectName(u"fsensors")
        self.gridLayout_6 = QGridLayout(self.fsensors)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_10 = QLabel(self.fsensors)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_6 = QLabel(self.fsensors)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_41 = QLabel(self.fsensors)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 4, 0, 1, 1)

        self.label_8 = QLabel(self.fsensors)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_36 = QLabel(self.fsensors)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.fsensors)
        self.aagcommunication = QWidget()
        self.aagcommunication.setObjectName(u"aagcommunication")
        self.verticalLayout_9 = QVBoxLayout(self.aagcommunication)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_37 = QLabel(self.aagcommunication)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.verticalLayout_9.addWidget(self.label_37)

        self.label_132 = QLabel(self.aagcommunication)
        self.label_132.setObjectName(u"label_132")

        self.verticalLayout_9.addWidget(self.label_132, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.aagcommunication)
        self.CanCommunication = QWidget()
        self.CanCommunication.setObjectName(u"CanCommunication")
        self.verticalLayout_12 = QVBoxLayout(self.CanCommunication)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.stackedWidget.addWidget(self.CanCommunication)
        self.Test = QWidget()
        self.Test.setObjectName(u"Test")
        self.verticalLayout_14 = QVBoxLayout(self.Test)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.stackedWidget.addWidget(self.Test)
        self.pedalss = QWidget()
        self.pedalss.setObjectName(u"pedalss")
        self.verticalLayout_4 = QVBoxLayout(self.pedalss)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget.addWidget(self.pedalss)
        self.dactivities = QWidget()
        self.dactivities.setObjectName(u"dactivities")
        self.verticalLayout_5 = QVBoxLayout(self.dactivities)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget.addWidget(self.dactivities)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.pushButton_4 = QPushButton(self.centre_menu_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 0))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        icon7 = QIcon()
        icon7.addFile(u"bootstrap_icons/images/Logo FATAR.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(174, 40))

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.horizontalLayout_8.addWidget(self.centre_menu_frame)

        self.right_menu_frame = QFrame(self.main_body_frame)
        self.right_menu_frame.setObjectName(u"right_menu_frame")
        self.right_menu_frame.setMinimumSize(QSize(0, 0))
        self.right_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.right_menu_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.right_menu_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ARTURIA MANAGER", None))
        self.min_window_button.setText("")
        self.max_window_button.setText("")
        self.close_window_button.setText("")
        self.encoder_bnt.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Device Info", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_5.setText("")
        self.label_7.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Hedi", None))
        self.label_32.setText("")
        self.sys_btn.setText("")
        self.label_40.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"V5.2.3", None))
        self.newdevice.setText(QCoreApplication.translate("MainWindow", u"LOAD CONFIG (.INI) FILE ", None))
        self.d5_3.setText("")
#if QT_CONFIG(shortcut)
        self.d5_3.setShortcut(QCoreApplication.translate("MainWindow", u"L", None))
#endif // QT_CONFIG(shortcut)
        self.d40_13.setText("")
#if QT_CONFIG(shortcut)
        self.d40_13.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.a4_15.setText("")
#if QT_CONFIG(shortcut)
        self.a4_15.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.f40_13.setText("")
#if QT_CONFIG(shortcut)
        self.f40_13.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.f50_3.setText("")
#if QT_CONFIG(shortcut)
        self.f50_3.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.a5_3.setText("")
#if QT_CONFIG(shortcut)
        self.a5_3.setShortcut(QCoreApplication.translate("MainWindow", u"V", None))
#endif // QT_CONFIG(shortcut)
        self.d50_3.setText("")
#if QT_CONFIG(shortcut)
        self.d50_3.setShortcut(QCoreApplication.translate("MainWindow", u"U", None))
#endif // QT_CONFIG(shortcut)
        self.e5_3.setText("")
#if QT_CONFIG(shortcut)
        self.e5_3.setShortcut(QCoreApplication.translate("MainWindow", u"Z", None))
#endif // QT_CONFIG(shortcut)
        self.c5_3.setText("")
#if QT_CONFIG(shortcut)
        self.c5_3.setShortcut(QCoreApplication.translate("MainWindow", u"K", None))
#endif // QT_CONFIG(shortcut)
        self.g4_13.setText("")
#if QT_CONFIG(shortcut)
        self.g4_13.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.g50_3.setText("")
#if QT_CONFIG(shortcut)
        self.g50_3.setShortcut(QCoreApplication.translate("MainWindow", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.c40_13.setText("")
#if QT_CONFIG(shortcut)
        self.c40_13.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.b4_15.setText("")
#if QT_CONFIG(shortcut)
        self.b4_15.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.c4_13.setText("")
#if QT_CONFIG(shortcut)
        self.c4_13.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.g5_3.setText("")
#if QT_CONFIG(shortcut)
        self.g5_3.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.d4_13.setText("")
#if QT_CONFIG(shortcut)
        self.d4_13.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_15.setText("")
#if QT_CONFIG(shortcut)
        self.a40_15.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.e4_13.setText("")
#if QT_CONFIG(shortcut)
        self.e4_13.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.f5_3.setText("")
#if QT_CONFIG(shortcut)
        self.f5_3.setShortcut(QCoreApplication.translate("MainWindow", u"X", None))
#endif // QT_CONFIG(shortcut)
        self.a50_3.setText("")
#if QT_CONFIG(shortcut)
        self.a50_3.setShortcut(QCoreApplication.translate("MainWindow", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.c50_3.setText("")
#if QT_CONFIG(shortcut)
        self.c50_3.setShortcut(QCoreApplication.translate("MainWindow", u"Y", None))
#endif // QT_CONFIG(shortcut)
        self.b5_3.setText("")
#if QT_CONFIG(shortcut)
        self.b5_3.setShortcut(QCoreApplication.translate("MainWindow", u"B", None))
#endif // QT_CONFIG(shortcut)
        self.f4_13.setText("")
#if QT_CONFIG(shortcut)
        self.f4_13.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.g40_13.setText("")
#if QT_CONFIG(shortcut)
        self.g40_13.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c6_3.setText("")
#if QT_CONFIG(shortcut)
        self.c6_3.setShortcut(QCoreApplication.translate("MainWindow", u"N", None))
#endif // QT_CONFIG(shortcut)
        self.b4_16.setText("")
#if QT_CONFIG(shortcut)
        self.b4_16.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_14.setText("")
#if QT_CONFIG(shortcut)
        self.f4_14.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_14.setText("")
#if QT_CONFIG(shortcut)
        self.e4_14.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_14.setText("")
#if QT_CONFIG(shortcut)
        self.g4_14.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_14.setText("")
#if QT_CONFIG(shortcut)
        self.d4_14.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_16.setText("")
#if QT_CONFIG(shortcut)
        self.a40_16.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_14.setText("")
#if QT_CONFIG(shortcut)
        self.c40_14.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_14.setText("")
#if QT_CONFIG(shortcut)
        self.f40_14.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_16.setText("")
#if QT_CONFIG(shortcut)
        self.a4_16.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_14.setText("")
#if QT_CONFIG(shortcut)
        self.d40_14.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_14.setText("")
#if QT_CONFIG(shortcut)
        self.g40_14.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_14.setText("")
#if QT_CONFIG(shortcut)
        self.c4_14.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_17.setText("")
#if QT_CONFIG(shortcut)
        self.b4_17.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_15.setText("")
#if QT_CONFIG(shortcut)
        self.f4_15.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_15.setText("")
#if QT_CONFIG(shortcut)
        self.e4_15.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_15.setText("")
#if QT_CONFIG(shortcut)
        self.g4_15.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_15.setText("")
#if QT_CONFIG(shortcut)
        self.d4_15.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_17.setText("")
#if QT_CONFIG(shortcut)
        self.a40_17.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_15.setText("")
#if QT_CONFIG(shortcut)
        self.c40_15.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_15.setText("")
#if QT_CONFIG(shortcut)
        self.f40_15.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_17.setText("")
#if QT_CONFIG(shortcut)
        self.a4_17.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_15.setText("")
#if QT_CONFIG(shortcut)
        self.d40_15.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_15.setText("")
#if QT_CONFIG(shortcut)
        self.g40_15.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_15.setText("")
#if QT_CONFIG(shortcut)
        self.c4_15.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_18.setText("")
#if QT_CONFIG(shortcut)
        self.b4_18.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_16.setText("")
#if QT_CONFIG(shortcut)
        self.f4_16.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_16.setText("")
#if QT_CONFIG(shortcut)
        self.e4_16.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_16.setText("")
#if QT_CONFIG(shortcut)
        self.g4_16.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_16.setText("")
#if QT_CONFIG(shortcut)
        self.d4_16.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_18.setText("")
#if QT_CONFIG(shortcut)
        self.a40_18.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_16.setText("")
#if QT_CONFIG(shortcut)
        self.c40_16.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_16.setText("")
#if QT_CONFIG(shortcut)
        self.f40_16.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_18.setText("")
#if QT_CONFIG(shortcut)
        self.a4_18.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_16.setText("")
#if QT_CONFIG(shortcut)
        self.d40_16.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_16.setText("")
#if QT_CONFIG(shortcut)
        self.g40_16.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_16.setText("")
#if QT_CONFIG(shortcut)
        self.c4_16.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_19.setText("")
#if QT_CONFIG(shortcut)
        self.b4_19.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_17.setText("")
#if QT_CONFIG(shortcut)
        self.f4_17.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_17.setText("")
#if QT_CONFIG(shortcut)
        self.e4_17.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_17.setText("")
#if QT_CONFIG(shortcut)
        self.g4_17.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_17.setText("")
#if QT_CONFIG(shortcut)
        self.d4_17.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_19.setText("")
#if QT_CONFIG(shortcut)
        self.a40_19.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_17.setText("")
#if QT_CONFIG(shortcut)
        self.c40_17.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_17.setText("")
#if QT_CONFIG(shortcut)
        self.f40_17.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_19.setText("")
#if QT_CONFIG(shortcut)
        self.a4_19.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_17.setText("")
#if QT_CONFIG(shortcut)
        self.d40_17.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_17.setText("")
#if QT_CONFIG(shortcut)
        self.g40_17.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_17.setText("")
#if QT_CONFIG(shortcut)
        self.c4_17.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_20.setText("")
#if QT_CONFIG(shortcut)
        self.b4_20.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_18.setText("")
#if QT_CONFIG(shortcut)
        self.f4_18.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_18.setText("")
#if QT_CONFIG(shortcut)
        self.e4_18.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_18.setText("")
#if QT_CONFIG(shortcut)
        self.g4_18.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_18.setText("")
#if QT_CONFIG(shortcut)
        self.d4_18.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_20.setText("")
#if QT_CONFIG(shortcut)
        self.a40_20.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_18.setText("")
#if QT_CONFIG(shortcut)
        self.c40_18.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_18.setText("")
#if QT_CONFIG(shortcut)
        self.f40_18.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_20.setText("")
#if QT_CONFIG(shortcut)
        self.a4_20.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_18.setText("")
#if QT_CONFIG(shortcut)
        self.d40_18.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_18.setText("")
#if QT_CONFIG(shortcut)
        self.g40_18.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_18.setText("")
#if QT_CONFIG(shortcut)
        self.c4_18.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_21.setText("")
#if QT_CONFIG(shortcut)
        self.b4_21.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.a40_21.setText("")
#if QT_CONFIG(shortcut)
        self.a40_21.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.a4_21.setText("")
#if QT_CONFIG(shortcut)
        self.a4_21.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.clear_notes.setText(QCoreApplication.translate("MainWindow", u"Clear Selection", None))
        self.select_all.setText(QCoreApplication.translate("MainWindow", u"Select All Keys", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Global Settings", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"White Keys Ratio :", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Black Keys Ratio:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Measurment Delay:                                                          ", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Global Ratio :", None))
        self.scan_nogoodkeyboards.setText(QCoreApplication.translate("MainWindow", u"Save Failed Keyboards", None))
        self.checkBoxrebounded.setText(QCoreApplication.translate("MainWindow", u"Hold Max Value", None))
        self.checkBox_notimer.setText(QCoreApplication.translate("MainWindow", u"Activate Instant Mode", None))
        self.checkBoxresplit.setText(QCoreApplication.translate("MainWindow", u"Split Black and White Keys", None))
        self.dynamic_radio.setText(QCoreApplication.translate("MainWindow", u"Dynamic Only", None))
        self.aft_radio.setText(QCoreApplication.translate("MainWindow", u"Aftertouch Only", None))
        self.full_radio.setText(QCoreApplication.translate("MainWindow", u"Full Test  ", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Velocity Settings", None))
        self.v_gain_lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Vel-gain:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Black", None))
        self.v_gain_lineEdit.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"White", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Vel-gain:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Max Velocity Threshold:                                               ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Min Velocity Threshold: ", None))
        self.two_sw.setText(QCoreApplication.translate("MainWindow", u"2 Contacts", None))
        self.three_sw.setText(QCoreApplication.translate("MainWindow", u"3 Contacts", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Recistance Settings", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Max Voltage Threshold:                                                      ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Min Voltage Threshold:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Max Resistance:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Min Resistance:", None))
        self.lineEdit_exponent.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Curve Exp:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Loaded Config:", None))
        self.d5.setText("")
#if QT_CONFIG(shortcut)
        self.d5.setShortcut(QCoreApplication.translate("MainWindow", u"L", None))
#endif // QT_CONFIG(shortcut)
        self.d40.setText("")
#if QT_CONFIG(shortcut)
        self.d40.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.a4.setText("")
#if QT_CONFIG(shortcut)
        self.a4.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.f40.setText("")
#if QT_CONFIG(shortcut)
        self.f40.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.f50.setText("")
#if QT_CONFIG(shortcut)
        self.f50.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.a5.setText("")
#if QT_CONFIG(shortcut)
        self.a5.setShortcut(QCoreApplication.translate("MainWindow", u"V", None))
#endif // QT_CONFIG(shortcut)
        self.d50.setText("")
#if QT_CONFIG(shortcut)
        self.d50.setShortcut(QCoreApplication.translate("MainWindow", u"U", None))
#endif // QT_CONFIG(shortcut)
        self.e5.setText("")
#if QT_CONFIG(shortcut)
        self.e5.setShortcut(QCoreApplication.translate("MainWindow", u"Z", None))
#endif // QT_CONFIG(shortcut)
        self.c5.setText("")
#if QT_CONFIG(shortcut)
        self.c5.setShortcut(QCoreApplication.translate("MainWindow", u"K", None))
#endif // QT_CONFIG(shortcut)
        self.g4.setText("")
#if QT_CONFIG(shortcut)
        self.g4.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.g50.setText("")
#if QT_CONFIG(shortcut)
        self.g50.setShortcut(QCoreApplication.translate("MainWindow", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.c40.setText("")
#if QT_CONFIG(shortcut)
        self.c40.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.b4.setText("")
#if QT_CONFIG(shortcut)
        self.b4.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.c4.setText("")
#if QT_CONFIG(shortcut)
        self.c4.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.g5.setText("")
#if QT_CONFIG(shortcut)
        self.g5.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.d4.setText("")
#if QT_CONFIG(shortcut)
        self.d4.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40.setText("")
#if QT_CONFIG(shortcut)
        self.a40.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.e4.setText("")
#if QT_CONFIG(shortcut)
        self.e4.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.f5.setText("")
#if QT_CONFIG(shortcut)
        self.f5.setShortcut(QCoreApplication.translate("MainWindow", u"X", None))
#endif // QT_CONFIG(shortcut)
        self.a50.setText("")
#if QT_CONFIG(shortcut)
        self.a50.setShortcut(QCoreApplication.translate("MainWindow", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.c50.setText("")
#if QT_CONFIG(shortcut)
        self.c50.setShortcut(QCoreApplication.translate("MainWindow", u"Y", None))
#endif // QT_CONFIG(shortcut)
        self.b5.setText("")
#if QT_CONFIG(shortcut)
        self.b5.setShortcut(QCoreApplication.translate("MainWindow", u"B", None))
#endif // QT_CONFIG(shortcut)
        self.f4.setText("")
#if QT_CONFIG(shortcut)
        self.f4.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.g40.setText("")
#if QT_CONFIG(shortcut)
        self.g40.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c6.setText("")
#if QT_CONFIG(shortcut)
        self.c6.setShortcut(QCoreApplication.translate("MainWindow", u"N", None))
#endif // QT_CONFIG(shortcut)
        self.b4_2.setText("")
#if QT_CONFIG(shortcut)
        self.b4_2.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_2.setText("")
#if QT_CONFIG(shortcut)
        self.f4_2.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_2.setText("")
#if QT_CONFIG(shortcut)
        self.e4_2.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_2.setText("")
#if QT_CONFIG(shortcut)
        self.g4_2.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_2.setText("")
#if QT_CONFIG(shortcut)
        self.d4_2.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_2.setText("")
#if QT_CONFIG(shortcut)
        self.a40_2.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_2.setText("")
#if QT_CONFIG(shortcut)
        self.c40_2.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_2.setText("")
#if QT_CONFIG(shortcut)
        self.f40_2.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_2.setText("")
#if QT_CONFIG(shortcut)
        self.a4_2.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_2.setText("")
#if QT_CONFIG(shortcut)
        self.d40_2.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_2.setText("")
#if QT_CONFIG(shortcut)
        self.g40_2.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_2.setText("")
#if QT_CONFIG(shortcut)
        self.c4_2.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_3.setText("")
#if QT_CONFIG(shortcut)
        self.b4_3.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_3.setText("")
#if QT_CONFIG(shortcut)
        self.f4_3.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_3.setText("")
#if QT_CONFIG(shortcut)
        self.e4_3.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_3.setText("")
#if QT_CONFIG(shortcut)
        self.g4_3.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_3.setText("")
#if QT_CONFIG(shortcut)
        self.d4_3.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_3.setText("")
#if QT_CONFIG(shortcut)
        self.a40_3.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_3.setText("")
#if QT_CONFIG(shortcut)
        self.c40_3.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_3.setText("")
#if QT_CONFIG(shortcut)
        self.f40_3.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_3.setText("")
#if QT_CONFIG(shortcut)
        self.a4_3.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_3.setText("")
#if QT_CONFIG(shortcut)
        self.d40_3.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_3.setText("")
#if QT_CONFIG(shortcut)
        self.g40_3.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_3.setText("")
#if QT_CONFIG(shortcut)
        self.c4_3.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_4.setText("")
#if QT_CONFIG(shortcut)
        self.b4_4.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_4.setText("")
#if QT_CONFIG(shortcut)
        self.f4_4.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_4.setText("")
#if QT_CONFIG(shortcut)
        self.e4_4.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_4.setText("")
#if QT_CONFIG(shortcut)
        self.g4_4.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_4.setText("")
#if QT_CONFIG(shortcut)
        self.d4_4.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_4.setText("")
#if QT_CONFIG(shortcut)
        self.a40_4.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_4.setText("")
#if QT_CONFIG(shortcut)
        self.c40_4.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_4.setText("")
#if QT_CONFIG(shortcut)
        self.f40_4.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_4.setText("")
#if QT_CONFIG(shortcut)
        self.a4_4.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_4.setText("")
#if QT_CONFIG(shortcut)
        self.d40_4.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_4.setText("")
#if QT_CONFIG(shortcut)
        self.g40_4.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_4.setText("")
#if QT_CONFIG(shortcut)
        self.c4_4.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_5.setText("")
#if QT_CONFIG(shortcut)
        self.b4_5.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_5.setText("")
#if QT_CONFIG(shortcut)
        self.f4_5.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_5.setText("")
#if QT_CONFIG(shortcut)
        self.e4_5.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_5.setText("")
#if QT_CONFIG(shortcut)
        self.g4_5.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_5.setText("")
#if QT_CONFIG(shortcut)
        self.d4_5.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_5.setText("")
#if QT_CONFIG(shortcut)
        self.a40_5.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_5.setText("")
#if QT_CONFIG(shortcut)
        self.c40_5.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_5.setText("")
#if QT_CONFIG(shortcut)
        self.f40_5.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_5.setText("")
#if QT_CONFIG(shortcut)
        self.a4_5.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_5.setText("")
#if QT_CONFIG(shortcut)
        self.d40_5.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_5.setText("")
#if QT_CONFIG(shortcut)
        self.g40_5.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_5.setText("")
#if QT_CONFIG(shortcut)
        self.c4_5.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_6.setText("")
#if QT_CONFIG(shortcut)
        self.b4_6.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.f4_6.setText("")
#if QT_CONFIG(shortcut)
        self.f4_6.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.e4_6.setText("")
#if QT_CONFIG(shortcut)
        self.e4_6.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.g4_6.setText("")
#if QT_CONFIG(shortcut)
        self.g4_6.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.d4_6.setText("")
#if QT_CONFIG(shortcut)
        self.d4_6.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.a40_6.setText("")
#if QT_CONFIG(shortcut)
        self.a40_6.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.c40_6.setText("")
#if QT_CONFIG(shortcut)
        self.c40_6.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.f40_6.setText("")
#if QT_CONFIG(shortcut)
        self.f40_6.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.a4_6.setText("")
#if QT_CONFIG(shortcut)
        self.a4_6.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.d40_6.setText("")
#if QT_CONFIG(shortcut)
        self.d40_6.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.g40_6.setText("")
#if QT_CONFIG(shortcut)
        self.g40_6.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.c4_6.setText("")
#if QT_CONFIG(shortcut)
        self.c4_6.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.b4_7.setText("")
#if QT_CONFIG(shortcut)
        self.b4_7.setShortcut(QCoreApplication.translate("MainWindow", u"J", None))
#endif // QT_CONFIG(shortcut)
        self.a40_7.setText("")
#if QT_CONFIG(shortcut)
        self.a40_7.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.a4_7.setText("")
#if QT_CONFIG(shortcut)
        self.a4_7.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit_3.setText("")
        self.lineEdit_19.setText("")
        self.file_name.setText("")
        self.label_weight.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Test Weight:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Live Data", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Velocity:", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Aftertouch (MIDI):", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Voltage (V):", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Note:                         ", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Resistance (\u03a9):", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Stabilization Timer:", None))
        self.label_message.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.radioAcoustic.setText(QCoreApplication.translate("MainWindow", u"ACOUSTIC TEST  ", None))
        self.radioElectrical.setText(QCoreApplication.translate("MainWindow", u"ELECTRICAL TEST", None))
        self.newdevice2.setText(QCoreApplication.translate("MainWindow", u"NEW DEVICE", None))
        self.reset_pushButton.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.new_file_ini.setText(QCoreApplication.translate("MainWindow", u"LOAD CONFIG (.INI) FILE ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Timeout", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Watchdog test ", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"TX of board", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Board reset", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Communication INFO: USB MIDI", None))
        self.label_132.setText("")
        self.pushButton_4.setText("")
    # retranslateUi

