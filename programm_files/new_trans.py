# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction_windows.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_new_transaction_window(object):
    def setupUi(self, new_transaction_window):
        if not new_transaction_window.objectName():
            new_transaction_window.setObjectName(u"new_transaction_window")
        new_transaction_window.resize(432, 335)
        new_transaction_window.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")
        self.make_transaction = QPushButton(new_transaction_window)
        self.make_transaction.setObjectName(u"make_transaction")
        self.make_transaction.setGeometry(QRect(170, 280, 93, 28))
        self.make_transaction.setStyleSheet(u"QPushButton{\n"
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
        self.layoutWidget = QWidget(new_transaction_window)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 411, 219))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.verticalLayout.addWidget(self.label_3)

        self.date_transaction = QDateEdit(self.layoutWidget)
        self.date_transaction.setObjectName(u"date_transaction")
        self.date_transaction.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.verticalLayout.addWidget(self.date_transaction)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.verticalLayout.addWidget(self.label_4)

        self.transaction_category = QComboBox(self.layoutWidget)
        self.transaction_category.setObjectName(u"transaction_category")
        self.transaction_category.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.verticalLayout.addWidget(self.transaction_category)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.verticalLayout.addWidget(self.label_5)

        self.comment_category = QLineEdit(self.layoutWidget)
        self.comment_category.setObjectName(u"comment_category")
        self.comment_category.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.verticalLayout.addWidget(self.comment_category)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.verticalLayout.addWidget(self.label_6)

        self.money_count = QLineEdit(self.layoutWidget)
        self.money_count.setObjectName(u"money_count")
        self.money_count.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.verticalLayout.addWidget(self.money_count)


        self.retranslateUi(new_transaction_window)

        QMetaObject.connectSlotsByName(new_transaction_window)
    # setupUi

    def retranslateUi(self, new_transaction_window):
        new_transaction_window.setWindowTitle(QCoreApplication.translate("new_transaction_window", u"\u041d\u043e\u0432\u0430\u044f \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f", None))
        self.make_transaction.setText(QCoreApplication.translate("new_transaction_window", u"\u0422\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f!", None))
        self.label_3.setText(QCoreApplication.translate("new_transaction_window", u"\u0414\u0430\u0442\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("new_transaction_window", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.label_5.setText(QCoreApplication.translate("new_transaction_window", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.label_6.setText(QCoreApplication.translate("new_transaction_window", u"\u0421\u0443\u043c\u043c\u0430:", None))
    # retranslateUi

