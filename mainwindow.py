# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 644)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tests = QLabel(self.centralwidget)
        self.tests.setObjectName(u"tests")
        self.tests.setGeometry(QRect(340, 10, 96, 41))
        self.tests.setMouseTracking(True)
        self.tests.setStyleSheet(u"font: 28pt \"Times New Roman\";")
        self.student = QPushButton(self.centralwidget)
        self.student.setObjectName(u"student")
        self.student.setGeometry(QRect(240, 240, 301, 91))
        self.teacher = QPushButton(self.centralwidget)
        self.teacher.setObjectName(u"teacher")
        self.teacher.setGeometry(QRect(240, 330, 301, 91))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tests.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u044b", None))
        self.student.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u043d\u0438\u043a", None))
        self.teacher.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0438\u0442\u0435\u043b\u044c", None))
    # retranslateUi

