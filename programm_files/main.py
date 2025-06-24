from PySide6 import QtCharts
from PySide6.QtGui import QBrush, QColor, QPainter, QPen, Qt

from ui_main import Ui_MainWindow

import sys
import os

import sqlite3

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QAbstractItemView
from PySide6 import QtWidgets
from tkinter import filedialog as fd
import add_category
import res_rc
import new_trans
from connection import Data

# окно новой транзакции
class NewTransaction(QWidget, new_trans.Ui_new_transaction_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # добавление в комбобокс категорий из БД
        self.Data = Data()
        self.all_cat = self.Data.get_categories()
        for i in self.all_cat:
            for j in i:
                self.transaction_category.addItem(j)

# окно новой категории
class NewCategory(QWidget, add_category.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Finances(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # подгрузка дизайна, обновление виджетов для отображения данных
        super().__init__()

        self.Data = Data()
        self.setupUi(self)
        self.setFixedSize(1370, 1003)
        self.user_menu.hide()

        self.user_name = self.Data.get_nickname()
        self.username_inmenu.setPlaceholderText(f"UserName: {self.user_name}")
        self.hello_label_main.setText(f'Здравствуй! {self.user_name}')
        self.search_button_outcome.clicked.connect(self.search)
        self.search_button_income.clicked.connect(self.search)
        self.search_button_duty.clicked.connect(self.search)

        self.refresh()
        self.view_data_in_tables('duty')
        self.view_data_in_tables('income')
        self.view_data_in_tables('outcome')

        self.delete_income.clicked.connect(self.delete)
        self.delete_duty.clicked.connect(self.delete)
        self.delete_outcome.clicked.connect(self.delete)

        self.choose_directory.clicked.connect(self.information_file_function)
        self.save_button.clicked.connect(self.save_raport)

        self.add_category_outcome.clicked.connect(self.open_new_category)
        self.add_category_income.clicked.connect(self.open_new_category)
        self.add_category_duty.clicked.connect(self.open_new_category)
        self.add_category_duty.clicked.connect(self.open_new_category)

        self.outcome.clicked.connect(self.open_new_transaction)
        self.duty.clicked.connect(self.open_new_transaction)
        self.income.clicked.connect(self.open_new_transaction)

        self.edit_account.clicked.connect(self.edit_name)
        self.done_button.clicked.connect(self.confirm_name)

        self.edit_duty.clicked.connect(self.edit_transaction_window)
        self.edit_income.clicked.connect(self.edit_transaction_window)
        self.edit_outcome.clicked.connect(self.edit_transaction_window)

    # выбираем директорию
    def information_file_function(self):
        self.file_d = fd.askdirectory(title="Выберите директорию для загрузки файла")
        if self.file_d:
            self.file_directory_line.setText(self.file_d)

    # запись в файл
    def save_raport(self):

        file_n = self.file_name_line.text()
        if file_n:
            file_e = self.file_extension_combo.currentText()
            file_n = f'{file_n}{file_e}'
            file_path = os.path.join(self.file_d, file_n)

            with open(file_path, 'w') as file:
                print(self.user_name, file=file)
                print(f'Долг:  {self.duty_categories.toPlainText()}', file=file)
                print(f'Доходы:  {self.income_categories.toPlainText()}', file=file)
                print(f'Расходы:  {self.outcomes_categories.toPlainText()}', file=file)

    # открываем окно новой транзакции
    def open_new_transaction(self):
        self.new_trans = NewTransaction()
        self.new_trans.setWindowTitle('Новая транзакция')
        self.new_trans.show()
        sender_for_transaction = self.sender().objectName()
        self.new_trans.make_transaction.clicked.connect(lambda: self.add_new_transaction(sender_for_transaction))


    # добавляем в БД
    def add_new_transaction(self, sender_for_transaction):
        date = self.new_trans.date_transaction.text()
        category = self.new_trans.transaction_category.currentText()
        description = self.new_trans.comment_category.text()
        summa = self.new_trans.money_count.text()
        self.Data.create_transaction_all(date, category, summa, sender_for_transaction, description)
        self.view_data_in_tables(sender_for_transaction)

        self.refresh()
        self.new_trans.close()

    # открываем окно добавления категории
    def open_new_category(self):
        self.new_window_category = NewCategory()
        self.new_window_category.setWindowTitle('Добавить новую категорию')
        self.new_window_category.show()
        self.new_window_category.add_category_button_widget_2.clicked.connect(self.add_new_category)

    # добавляем в БД
    def add_new_category(self):
        category_name = self.new_window_category.lineEdit.text()
        self.Data.new_category_creation(category_name)
        self.refresh()
        self.new_window_category.close()

    # подгружем данные в виджеты из БД
    def refresh(self):
        if self.Data.get_categories():
            self.overview_text.setPlainText('\n'.join(list(zip(*self.Data.get_categories()))[0]))
        if self.Data.get_categories_for_plain('duty'):
            self.duty_categories.setPlainText('\n'.join(f"{item[0]}: {item[1]}" for item in self.Data.get_categories_for_plain('duty')))
        else:
            self.duty_categories.setPlainText('')
        if self.Data.get_categories_for_plain('income'):
            self.income_categories.setPlainText('\n'.join(f"{item[0]}: {item[1]}" for item in self.Data.get_categories_for_plain('income')))
        else:
            self.income_categories.setPlainText('')

        if self.Data.get_categories_for_plain('outcome'):
            self.outcomes_categories.setPlainText('\n'.join(f"{item[0]}: {item[1]}" for item in self.Data.get_categories_for_plain('outcome')))
        else:
            self.outcomes_categories.setPlainText('')


        self.all_duty.setText(f'Всего:  {self.Data.duties()}')
        self.income_overall.setText(f'Всего:  {self.Data.incomes()}')
        self.outcomes.setText(f'Всего:  {self.Data.outcomes()}')

        self.all_outcomes.setText(f'Расходы: {self.Data.outcomes()}')
        self.all_incomes.setText(f'Доходы: {self.Data.incomes()}')

        self.display_chart_info()

    # меняем имя
    def edit_name(self):
        self.username_inmenu.setEnabled(True)

    # применяем имя
    def confirm_name(self):
        self.user_name = self.username_inmenu.text()
        self.username_inmenu.setPlaceholderText(f"UserName: {self.user_name}")
        self.username_inmenu.setText('')
        self.hello_label_main.setText(f'Здравствуй! {self.user_name}')
        self.username_inmenu.setEnabled(False)
        self.Data.nickname_change(self.user_name)

    # отображаем транзакции в табличке
    def view_data_in_tables(self, operation):
        rows = self.Data.data_all(operation)
        if operation == 'duty':
            self.duty_transactions.setRowCount(len(rows))
            self.duty_transactions.setColumnCount(len(rows[0]) if rows else 0)
            self.duty_transactions.setHorizontalHeaderLabels(['ID', 'Date', 'Category', 'Description', 'Amount'])

            for row_idx, row in enumerate(rows):
                for col_idx, item in enumerate(row):
                    self.duty_transactions.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(item)))
            self.duty_transactions.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
            self.duty_transactions.horizontalHeader().setDefaultSectionSize(171)

        elif operation == 'income':
            self.income_transactions.setRowCount(len(rows))
            self.income_transactions.setColumnCount(len(rows[0]) if rows else 0)
            self.income_transactions.setHorizontalHeaderLabels(
                ['ID', 'Date', 'Category', 'Description', 'Amount'])

            for row_idx, row in enumerate(rows):
                for col_idx, item in enumerate(row):
                    self.income_transactions.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(item)))
            self.income_transactions.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
            self.income_transactions.horizontalHeader().setDefaultSectionSize(171)

        else:
            self.outcome_transactions.setRowCount(len(rows))
            self.outcome_transactions.setColumnCount(len(rows[0]) if rows else 0)
            self.outcome_transactions.setHorizontalHeaderLabels(
                ['ID', 'Date', 'Category', 'Description', 'Amount'])

            for row_idx, row in enumerate(rows):
                for col_idx, item in enumerate(row):
                    self.outcome_transactions.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(item)))
            self.outcome_transactions.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
            self.outcome_transactions.horizontalHeader().setDefaultSectionSize(171)

    # удаление
    def delete(self):

        sender = self.sender()
        id_to_delete = 1
        if sender.objectName() == 'delete_outcome':
            current_row = self.outcome_transactions.currentRow()
            if current_row != -1:
                id_to_delete = int(self.outcome_transactions.item(current_row, 0).text())

            self.Data.delete_transaction(id_to_delete)
            self.view_data_in_tables('outcome')
            self.refresh()

        elif sender.objectName() == 'delete_income':
            current_row = self.income_transactions.currentRow()
            if current_row != -1:
                id_to_delete = int(self.income_transactions.item(current_row, 0).text())

            self.Data.delete_transaction(id_to_delete)
            self.view_data_in_tables('income')
            self.refresh()
        else:
            current_row = self.duty_transactions.currentRow()
            if current_row != -1:
                id_to_delete = int(self.duty_transactions.item(current_row, 0).text())

            self.Data.delete_transaction(id_to_delete)
            self.view_data_in_tables('duty')
            self.refresh()

    # поиск по ID
    def search(self):
        sender = self.sender().objectName()
        id_to_search = ''
        operation = ''
        if sender == 'search_button_outcome':
            operation = 'outcome'
            id_to_search = self.Search_by_id_outcome.text()

        elif sender == 'search_button_income':
            operation = 'income'
            id_to_search = self.Search_by_id_income.text()

        else:
            operation = 'duty'
            id_to_search = self.Search_by_id_duty.text()

        rows = self.Data.data_all(operation, id_to_search)
        if operation == 'duty':
            self.duty_transactions.setRowCount(len(rows))
            self.duty_transactions.setColumnCount(len(rows[0]) if rows else 0)
            self.duty_transactions.setHorizontalHeaderLabels(
                ['ID', 'Date', 'Category', 'Description', 'Amount', 'Type'])

            for row_idx, row in enumerate(rows):
                for col_idx, item in enumerate(row):
                    self.duty_transactions.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(item)))

        elif operation == 'income':
            self.income_transactions.setRowCount(len(rows))
            self.income_transactions.setColumnCount(len(rows[0]) if rows else 0)
            self.income_transactions.setHorizontalHeaderLabels(
                ['ID', 'Date', 'Category', 'Description', 'Amount', 'Type'])

            for row_idx, row in enumerate(rows):
                for col_idx, item in enumerate(row):
                    self.income_transactions.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(item)))

        else:
            self.outcome_transactions.setRowCount(len(rows))
            self.outcome_transactions.setColumnCount(len(rows[0]) if rows else 0)
            self.outcome_transactions.setHorizontalHeaderLabels(
                ['ID', 'Date', 'Category', 'Description', 'Amount', 'Type'])

            for row_idx, row in enumerate(rows):
                for col_idx, item in enumerate(row):
                    self.outcome_transactions.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(item)))

    # открываем окно изменения транзакции

    def edit_transaction_window(self):
        self.edittrans = NewTransaction()
        self.edittrans.setWindowTitle('Изменить транзакцию')
        self.edittrans.show()
        sender_for_edit = self.sender().objectName()
        self.edittrans.make_transaction.clicked.connect(lambda: self.edit_transaction(sender_for_edit))

    # изменяем транзакцию
    def edit_transaction(self, sender_for_edit):
        id_to_edit = 1
        operation = ''
        if sender_for_edit == 'edit_duty':
            current_row = self.duty_transactions.currentRow()
            if current_row != -1:
                id_to_edit = int(self.duty_transactions.item(current_row, 0).text())
                operation = 'duty'

        elif sender_for_edit == 'edit_income':
            current_row = self.income_transactions.currentRow()
            if current_row != -1:
                id_to_edit = int(self.income_transactions.item(current_row, 0).text())
                operation = 'income'
        else:
            current_row = self.outcome_transactions.currentRow()
            if current_row != -1:
                id_to_edit = int(self.outcome_transactions.item(current_row, 0).text())
                operation = 'outcome'

        date = self.edittrans.date_transaction.text()
        category = self.edittrans.transaction_category.currentText()
        description = self.edittrans.comment_category.text()
        summa = self.edittrans.money_count.text()

        self.Data.edit_transaction(date, category, summa, id_to_edit, description)
        self.edittrans.close()
        self.view_data_in_tables(operation)
        self.refresh()

    # отображаем диаграммочку
    def display_chart_info(self):
        series = QtCharts.QPieSeries()

        slice_duty = series.append("Долги", self.Data.duties())
        slice_income = series.append("Доходы", self.Data.incomes())
        slice_outcome = series.append("Расходы", self.Data.outcomes())

        slice_duty.setBrush(QColor(255, 0, 0))
        slice_income.setBrush(QColor(0, 255, 0))
        slice_outcome.setBrush(QColor(0, 0, 255))

        chart = QtCharts.QChart()

        for slice in series.slices():
            slice.setPen(QPen(QColor(255, 255, 255, 0)))

        chart.setBackgroundBrush(QBrush(QColor(40, 40, 40)))
        chart.addSeries(series)
        chart.setTitle('Expenses')
        chart.setTitleBrush(QColor(255, 255, 255))

        legend = chart.legend()
        legend.setVisible(True)
        legend.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.graphicsView.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.graphicsView.setChart(chart)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Finances()
    ex.show()
    sys.exit(app.exec())


