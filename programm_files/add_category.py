# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_category_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(406, 211)
        Dialog.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(10, 20, 381, 31))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 70, 381, 41))
        self.lineEdit.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")
        self.add_category_button_widget_2 = QPushButton(Dialog)
        self.add_category_button_widget_2.setObjectName(u"add_category_button_widget_2")
        self.add_category_button_widget_2.setGeometry(QRect(150, 140, 93, 28))
        self.add_category_button_widget_2.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(0, 85, 255);\n"
"background-color: rgb(159, 159, 159);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0, 85, 255);\n"
"background-color:rgb(159, 159, 159)\n"
"}\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.add_category_button_widget_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

