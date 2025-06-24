# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1369, 1012)
        MainWindow.setStyleSheet(u"\n"
"\n"
"\n"
"font-family:Noto Sans SC;\n"
"background-color:rgb(53, 53, 53)\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane{\n"
"border: 1px;\n"
"background:rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QTabWidget{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"\n"
"QTabWidget:tab-bar\n"
"{\n"
"\n"
"\n"
"alignment:left;\n"
"}\n"
"QTabBar:tab{\n"
"\n"
"background-color:rgba(255, 255, 255, 0);\n"
"color:white;\n"
"width:115px;\n"
"height: 40px;\n"
"}\n"
"QTabBar:tab:selected{\n"
"background-color:rgb(159, 159, 159);\n"
"}\n"
"\n"
"QTabBar:tab:selected:hover{\n"
"background-color: rgb(159, 159, 159);\n"
"}\n"
"\n"
"QTabBar:tab:hover{\n"
"background-color: rgb(159, 159, 159);\n"
"}")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.all_incomes = QLineEdit(self.tab_4)
        self.all_incomes.setObjectName(u"all_incomes")
        self.all_incomes.setEnabled(False)
        self.all_incomes.setGeometry(QRect(50, 80, 321, 41))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(10)
        self.all_incomes.setFont(font1)
        self.all_incomes.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")
        self.all_outcomes = QLineEdit(self.tab_4)
        self.all_outcomes.setObjectName(u"all_outcomes")
        self.all_outcomes.setEnabled(False)
        self.all_outcomes.setGeometry(QRect(50, 30, 321, 41))
        self.all_outcomes.setFont(font1)
        self.all_outcomes.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")
        self.all_categories = QLineEdit(self.tab_4)
        self.all_categories.setObjectName(u"all_categories")
        self.all_categories.setEnabled(False)
        self.all_categories.setGeometry(QRect(50, 130, 321, 41))
        self.all_categories.setFont(font1)
        self.all_categories.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")
        self.overview_text = QPlainTextEdit(self.tab_4)
        self.overview_text.setObjectName(u"overview_text")
        self.overview_text.setEnabled(False)
        self.overview_text.setGeometry(QRect(50, 180, 321, 681))
        self.overview_text.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"color:white;")
        self.user_information_button = QPushButton(self.tab_4)
        self.user_information_button.setObjectName(u"user_information_button")
        self.user_information_button.setGeometry(QRect(1140, 30, 51, 51))
        self.user_information_button.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u":/icons2/icons/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.user_information_button.setIcon(icon)
        self.user_information_button.setIconSize(QSize(40, 40))
        self.user_information_button.setCheckable(True)
        self.user_information_button.setAutoExclusive(True)
        self.user_menu = QWidget(self.tab_4)
        self.user_menu.setObjectName(u"user_menu")
        self.user_menu.setEnabled(True)
        self.user_menu.setGeometry(QRect(1130, 90, 201, 121))
        self.user_menu.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"")
        self.layoutWidget = QWidget(self.user_menu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 9, 181, 91))
        self.gridLayout_6 = QGridLayout(self.layoutWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.edit_account = QPushButton(self.layoutWidget)
        self.edit_account.setObjectName(u"edit_account")
        self.edit_account.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit_account.setIcon(icon1)
        self.edit_account.setIconSize(QSize(15, 15))
        self.edit_account.setCheckable(False)

        self.gridLayout_6.addWidget(self.edit_account, 1, 0, 1, 1)

        self.done_button = QPushButton(self.layoutWidget)
        self.done_button.setObjectName(u"done_button")
        self.done_button.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"\n"
"border-radius: 8px;\n"
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
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons2/icons/check_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.done_button.setIcon(icon2)

        self.gridLayout_6.addWidget(self.done_button, 2, 0, 1, 1)

        self.username_inmenu = QLineEdit(self.layoutWidget)
        self.username_inmenu.setObjectName(u"username_inmenu")
        self.username_inmenu.setEnabled(False)

        self.gridLayout_6.addWidget(self.username_inmenu, 0, 0, 1, 1)

        self.hello_label_main = QLabel(self.tab_4)
        self.hello_label_main.setObjectName(u"hello_label_main")
        self.hello_label_main.setGeometry(QRect(380, 30, 741, 31))
        self.hello_label_main.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")
        self.graphicsView = QChartView(self.tab_4)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(380, 70, 741, 791))
        self.graphicsView.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons2/icons/report.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.tab_4, icon3, "")
        self.overview_3 = QWidget()
        self.overview_3.setObjectName(u"overview_3")
        self.layoutWidget1 = QWidget(self.overview_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 10, 1341, 921))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.outcome = QPushButton(self.layoutWidget1)
        self.outcome.setObjectName(u"outcome")
        self.outcome.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/add_circle_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.outcome.setIcon(icon4)
        self.outcome.setIconSize(QSize(15, 15))
        self.outcome.setCheckable(False)

        self.gridLayout_3.addWidget(self.outcome, 0, 1, 1, 1)

        self.edit_outcome = QPushButton(self.layoutWidget1)
        self.edit_outcome.setObjectName(u"edit_outcome")
        self.edit_outcome.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"")
        self.edit_outcome.setIcon(icon1)
        self.edit_outcome.setIconSize(QSize(15, 15))
        self.edit_outcome.setCheckable(False)

        self.gridLayout_3.addWidget(self.edit_outcome, 0, 2, 1, 1)

        self.outcomes = QLineEdit(self.layoutWidget1)
        self.outcomes.setObjectName(u"outcomes")
        self.outcomes.setEnabled(False)
        self.outcomes.setFont(font1)
        self.outcomes.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.outcomes, 0, 0, 1, 1)

        self.Search_by_id_outcome = QLineEdit(self.layoutWidget1)
        self.Search_by_id_outcome.setObjectName(u"Search_by_id_outcome")
        self.Search_by_id_outcome.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.Search_by_id_outcome, 0, 5, 1, 1)

        self.search_button_outcome = QPushButton(self.layoutWidget1)
        self.search_button_outcome.setObjectName(u"search_button_outcome")
        self.search_button_outcome.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"")

        self.gridLayout_3.addWidget(self.search_button_outcome, 0, 6, 1, 1)

        self.outcomes_categories = QPlainTextEdit(self.layoutWidget1)
        self.outcomes_categories.setObjectName(u"outcomes_categories")
        self.outcomes_categories.setEnabled(False)
        self.outcomes_categories.setToolTipDuration(2)
        self.outcomes_categories.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"color:white;")

        self.gridLayout_3.addWidget(self.outcomes_categories, 1, 0, 1, 1)

        self.delete_outcome = QPushButton(self.layoutWidget1)
        self.delete_outcome.setObjectName(u"delete_outcome")
        self.delete_outcome.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/delete_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_outcome.setIcon(icon5)
        self.delete_outcome.setIconSize(QSize(15, 15))
        self.delete_outcome.setCheckable(False)

        self.gridLayout_3.addWidget(self.delete_outcome, 0, 3, 1, 1)

        self.add_category_outcome = QPushButton(self.layoutWidget1)
        self.add_category_outcome.setObjectName(u"add_category_outcome")
        self.add_category_outcome.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        self.add_category_outcome.setIcon(icon4)

        self.gridLayout_3.addWidget(self.add_category_outcome, 0, 4, 1, 1)

        self.outcome_transactions = QTableWidget(self.layoutWidget1)
        self.outcome_transactions.setObjectName(u"outcome_transactions")
        self.outcome_transactions.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"color:white;")

        self.gridLayout_3.addWidget(self.outcome_transactions, 1, 1, 1, 6)

        icon6 = QIcon()
        icon6.addFile(u":/icons2/icons/payments_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.overview_3, icon6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.layoutWidget2 = QWidget(self.tab_5)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 10, 1341, 921))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.income_overall = QLineEdit(self.layoutWidget2)
        self.income_overall.setObjectName(u"income_overall")
        self.income_overall.setEnabled(False)
        self.income_overall.setFont(font1)
        self.income_overall.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"\n"
"}")

        self.gridLayout_4.addWidget(self.income_overall, 0, 0, 1, 1)

        self.income = QPushButton(self.layoutWidget2)
        self.income.setObjectName(u"income")
        self.income.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        self.income.setIcon(icon4)
        self.income.setIconSize(QSize(15, 15))
        self.income.setCheckable(False)

        self.gridLayout_4.addWidget(self.income, 0, 1, 1, 1)

        self.edit_income = QPushButton(self.layoutWidget2)
        self.edit_income.setObjectName(u"edit_income")
        self.edit_income.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"")
        self.edit_income.setIcon(icon1)
        self.edit_income.setIconSize(QSize(15, 15))
        self.edit_income.setCheckable(False)

        self.gridLayout_4.addWidget(self.edit_income, 0, 2, 1, 1)

        self.delete_income = QPushButton(self.layoutWidget2)
        self.delete_income.setObjectName(u"delete_income")
        self.delete_income.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        self.delete_income.setIcon(icon5)
        self.delete_income.setIconSize(QSize(15, 15))
        self.delete_income.setCheckable(False)

        self.gridLayout_4.addWidget(self.delete_income, 0, 3, 1, 1)

        self.add_category_income = QPushButton(self.layoutWidget2)
        self.add_category_income.setObjectName(u"add_category_income")
        self.add_category_income.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        self.add_category_income.setIcon(icon4)

        self.gridLayout_4.addWidget(self.add_category_income, 0, 4, 1, 1)

        self.income_transactions = QTableWidget(self.layoutWidget2)
        self.income_transactions.setObjectName(u"income_transactions")
        self.income_transactions.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"color:white;")

        self.gridLayout_4.addWidget(self.income_transactions, 1, 1, 1, 6)

        self.search_button_income = QPushButton(self.layoutWidget2)
        self.search_button_income.setObjectName(u"search_button_income")
        self.search_button_income.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"")

        self.gridLayout_4.addWidget(self.search_button_income, 0, 6, 1, 1)

        self.income_categories = QPlainTextEdit(self.layoutWidget2)
        self.income_categories.setObjectName(u"income_categories")
        self.income_categories.setEnabled(False)
        self.income_categories.setToolTipDuration(2)
        self.income_categories.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"color:white;")

        self.gridLayout_4.addWidget(self.income_categories, 1, 0, 1, 1)

        self.Search_by_id_income = QLineEdit(self.layoutWidget2)
        self.Search_by_id_income.setObjectName(u"Search_by_id_income")
        self.Search_by_id_income.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"\n"
"}")

        self.gridLayout_4.addWidget(self.Search_by_id_income, 0, 5, 1, 1)

        icon7 = QIcon()
        icon7.addFile(u":/icons2/icons/cash.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.tab_5, icon7, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.layoutWidget3 = QWidget(self.tab_6)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 10, 1341, 921))
        self.gridLayout_5 = QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.edit_duty = QPushButton(self.layoutWidget3)
        self.edit_duty.setObjectName(u"edit_duty")
        self.edit_duty.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"")
        self.edit_duty.setIcon(icon1)
        self.edit_duty.setIconSize(QSize(15, 15))
        self.edit_duty.setCheckable(False)

        self.gridLayout_5.addWidget(self.edit_duty, 0, 2, 1, 1)

        self.add_category_duty = QPushButton(self.layoutWidget3)
        self.add_category_duty.setObjectName(u"add_category_duty")
        self.add_category_duty.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        self.add_category_duty.setIcon(icon4)

        self.gridLayout_5.addWidget(self.add_category_duty, 0, 4, 1, 1)

        self.search_button_duty = QPushButton(self.layoutWidget3)
        self.search_button_duty.setObjectName(u"search_button_duty")
        self.search_button_duty.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"")

        self.gridLayout_5.addWidget(self.search_button_duty, 0, 6, 1, 1)

        self.duty_categories = QPlainTextEdit(self.layoutWidget3)
        self.duty_categories.setObjectName(u"duty_categories")
        self.duty_categories.setEnabled(False)
        self.duty_categories.setToolTipDuration(2)
        self.duty_categories.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"color:white;")

        self.gridLayout_5.addWidget(self.duty_categories, 1, 0, 1, 1)

        self.all_duty = QLineEdit(self.layoutWidget3)
        self.all_duty.setObjectName(u"all_duty")
        self.all_duty.setEnabled(False)
        self.all_duty.setFont(font1)
        self.all_duty.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"\n"
"}")

        self.gridLayout_5.addWidget(self.all_duty, 0, 0, 1, 1)

        self.duty = QPushButton(self.layoutWidget3)
        self.duty.setObjectName(u"duty")
        self.duty.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        self.duty.setIcon(icon4)
        self.duty.setIconSize(QSize(15, 15))
        self.duty.setCheckable(False)

        self.gridLayout_5.addWidget(self.duty, 0, 1, 1, 1)

        self.delete_duty = QPushButton(self.layoutWidget3)
        self.delete_duty.setObjectName(u"delete_duty")
        self.delete_duty.setStyleSheet(u"QPushButton{\n"
"\n"
"color: white;\n"
"\n"
"border-color:rgbrgb(177, 177, 177);\n"
"border-radius: 8px;\n"
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
"\n"
"\n"
"")
        self.delete_duty.setIcon(icon5)
        self.delete_duty.setIconSize(QSize(15, 15))
        self.delete_duty.setCheckable(False)

        self.gridLayout_5.addWidget(self.delete_duty, 0, 3, 1, 1)

        self.duty_transactions = QTableWidget(self.layoutWidget3)
        self.duty_transactions.setObjectName(u"duty_transactions")
        self.duty_transactions.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"color:white;")

        self.gridLayout_5.addWidget(self.duty_transactions, 1, 1, 1, 6)

        self.Search_by_id_duty = QLineEdit(self.layoutWidget3)
        self.Search_by_id_duty.setObjectName(u"Search_by_id_duty")
        self.Search_by_id_duty.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"\n"
"}")

        self.gridLayout_5.addWidget(self.Search_by_id_duty, 0, 5, 1, 1)

        icon8 = QIcon()
        icon8.addFile(u":/icons2/icons/tax-credit.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.tab_6, icon8, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.layoutWidget4 = QWidget(self.tab_7)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(270, 290, 771, 211))
        self.gridLayout_2 = QGridLayout(self.layoutWidget4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)
        self.label_3.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.file_directory_line = QLineEdit(self.layoutWidget4)
        self.file_directory_line.setObjectName(u"file_directory_line")
        self.file_directory_line.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.file_directory_line, 1, 0, 1, 1)

        self.choose_directory = QPushButton(self.layoutWidget4)
        self.choose_directory.setObjectName(u"choose_directory")
        self.choose_directory.setStyleSheet(u"QPushButton{\n"
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
"\n"
"\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/folder_open_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.choose_directory.setIcon(icon9)

        self.gridLayout_2.addWidget(self.choose_directory, 1, 2, 1, 1)

        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        self.label_4.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.file_name_line = QLineEdit(self.layoutWidget4)
        self.file_name_line.setObjectName(u"file_name_line")
        self.file_name_line.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.file_name_line, 3, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setStyleSheet(u"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.file_extension_combo = QComboBox(self.layoutWidget4)
        self.file_extension_combo.addItem("")
        self.file_extension_combo.addItem("")
        self.file_extension_combo.addItem("")
        self.file_extension_combo.setObjectName(u"file_extension_combo")
        self.file_extension_combo.setStyleSheet(u"\n"
"background-color:rgb(30, 30, 30);\n"
"border:2px solid;\n"
"border-color:rgb(85, 85, 85);\n"
"color:rgb(161, 161, 161);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.file_extension_combo, 4, 1, 1, 1)

        self.save_button = QPushButton(self.layoutWidget4)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_2.addWidget(self.save_button, 5, 0, 1, 1)

        icon10 = QIcon()
        icon10.addFile(u":/icons2/icons/diskette.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.tab_7, icon10, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.user_information_button.clicked["bool"].connect(self.user_menu.setVisible)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0438 \u0444\u0438\u043d\u0430\u043d\u0441\u044b", None))
        self.all_incomes.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b:", None))
        self.all_outcomes.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b:", None))
        self.all_categories.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438:", None))
        self.user_information_button.setText("")
        self.edit_account.setText("")
        self.done_button.setText("")
        self.username_inmenu.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserName: user", None))
        self.hello_label_main.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439, user!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.outcome.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.edit_outcome.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.outcomes.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e: ", None))
        self.Search_by_id_outcome.setText("")
        self.Search_by_id_outcome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e ID", None))
        self.search_button_outcome.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a!", None))
        self.delete_outcome.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.add_category_outcome.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overview_3), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        self.income_overall.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e: ", None))
        self.income.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.edit_income.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.delete_income.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.add_category_income.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.search_button_income.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a!", None))
        self.Search_by_id_income.setText("")
        self.Search_by_id_income.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        self.edit_duty.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.add_category_duty.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.search_button_duty.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a!", None))
        self.all_duty.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e: ", None))
        self.duty.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_duty.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.Search_by_id_duty.setText("")
        self.Search_by_id_duty.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u043f\u043a\u0443 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f:", None))
        self.file_directory_line.setText("")
        self.file_directory_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\", None))
        self.choose_directory.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430:", None))
        self.file_name_line.setText("")
        self.file_name_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u0435:", None))
        self.file_extension_combo.setItemText(0, QCoreApplication.translate("MainWindow", u".txt", None))
        self.file_extension_combo.setItemText(1, QCoreApplication.translate("MainWindow", u".dat", None))
        self.file_extension_combo.setItemText(2, QCoreApplication.translate("MainWindow", u".ini", None))

        self.save_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

