import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from ui_main import Ui_MainWindow
from new_transaction import Ui_Dialog
from connection import Data

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()

        self.reload_data()
        self.view_data()

        self.ui.btn_new_transaction.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_edit_transaction.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_delete_transaction.clicked.connect(self.delete_current_transaction)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('expenses')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def reload_data(self):
        self.ui.balance.setText(self.conn.total_balance())
        self.ui.income.setText(self.conn.total_income())
        self.ui.outcome.setText(self.conn.total_outcome())
        self.ui.auto_2.setText(self.conn.total_auto())
        self.ui.groceries.setText(self.conn.total_groceries())
        self.ui.entertainment.setText(self.conn.total_entertainment())
        self.ui.other.setText(self.conn.total_other())

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()

        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        sender = self.sender()

        if sender.text() == "New Transaction":
            self.ui_window.btn_new_transaction.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.btn_new_transaction.clicked.connect(self.edit_current_transaction)

    def add_new_transaction(self):
        date = self.ui_window.lbl_date.text()
        category = self.ui_window.cb_category.currentText()
        description = self.ui_window.lbl_description.text()
        balance = self.ui_window.lbl_balance.text()
        status = self.ui_window.cb_2.currentText()

        self.conn.add_new_transaction(date, category, description, balance if status == "Income" else "-" +balance, status)

        self.reload_data()
        self.view_data()
        self.new_window.close()

    def edit_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        date = self.ui_window.lbl_date.text()
        category = self.ui_window.cb_category.currentText()
        description = self.ui_window.lbl_description.text()
        balance = self.ui_window.lbl_balance.text()
        status = self.ui_window.cb_2.currentText()

        self.conn.edit_transaction(date, category, description, balance, status, id)

        self.reload_data()
        self.view_data()
        self.new_window.close()

    def delete_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.conn.delete_transaction(id)
        self.reload_data()
        self.view_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())

