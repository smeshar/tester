import sys

import testlist
import vopros1
import vopros2
import vopros3
import vopros4
import result
import teacher1
import teacher2

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtSql import QSqlTableModel

from mainwindow import Ui_MainWindow
from register2 import Ui_Dialog

from con import Data
import sqlite3
# from new_transaction import Ui_Dialog
# from connection import Data

class Tester(QMainWindow):
    def __init__(self):
        super(Tester, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.student.clicked.connect(self.open_dialog)
        self.ui.teacher.clicked.connect(self.open_dialog)

        self.student_mode = True

        self.user_login = ""
        self.user_pass = ""

        self.conn = Data()

    #def add_test(self):

    def teacher3(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = teacher2.Ui_Dialog()

        self.ui_window.setupUi(self.new_window)
        self.ui_window.label.setText("Вопрос 2")
        self.new_window.show()



    def teacher2(self):
        self.close()

        self.new_window = QtWidgets.QDialog()
        self.ui_window = teacher2.Ui_Dialog()

        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        self.ui_window.buttonBox.accepted.connect(self.teacher3)

    def teacher1(self):
        self.close()

        self.new_window = QtWidgets.QDialog()
        self.ui_window = teacher1.Ui_Dialog()

        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        self.ui_window.buttonBox.accepted.connect(self.teacher2)

    def list_problems(self):
        self.listui = testlist.Ui_MainWindow()
        self.listui.setupUi(self)

        l = self.conn.list_tests()

        for i in range(len(l)):
            if i == 0: self.listui.label_1.setText(l[i])
            if i == 1: self.listui.label_2.setText(l[i])
            if i == 2: self.listui.label_3.setText(l[i])
            if i == 3: self.listui.label_4.setText(l[i])
            if i == 4: self.listui.label_5.setText(l[i])
            if i == 5: self.listui.label_6.setText(l[i])
            if i == 6: self.listui.label_7.setText(l[i])
            if i == 7: self.listui.label_8.setText(l[i])
            if i == 8: self.listui.label_9.setText(l[i])
            if i == 9: self.listui.label_10.setText(l[i])
            if i == 10: self.listui.label_11.setText(l[i])

        self.listui.test1btn.clicked.connect(self.vopros1)

    def result(self):
        self.listui = testlist.Ui_MainWindow()
        self.listui.setupUi(self)

        self.close()

        self.new_window = QtWidgets.QDialog()
        self.ui_window = result.Ui_Dialog()

        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def vopros4(self):
        self.uitest = vopros4.Ui_MainWindow()
        self.uitest.setupUi(self)

        self.showFullScreen()
        self.uitest.pushButton.clicked.connect(self.result)

    def vopros3(self):
        self.uitest = vopros3.Ui_MainWindow()
        self.uitest.setupUi(self)

        self.showFullScreen()
        self.uitest.pushButton.clicked.connect(self.vopros4)

    def vopros2(self):
        self.uitest = vopros2.Ui_MainWindow()
        self.uitest.setupUi(self)

        self.showFullScreen()
        self.uitest.pushButton.clicked.connect(self.vopros3)

    def vopros1(self):
        self.uitest = vopros1.Ui_MainWindow()
        self.uitest.setupUi(self)

        self.showFullScreen()
        self.uitest.pushButton.clicked.connect(self.vopros2)

    def open_dialog(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()

        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        sender = self.sender()
        #print(sender)

        login = self.ui_window.login_label.text()
        #print(login)

        if sender.text() == "Учитель":
            self.student_mode = False
        else:
            self.student_mode = True

        self.ui_window.reg_btn.clicked.connect(self.register)
        self.ui_window.join_btn.clicked.connect(self.login)

    def register(self):
        login = self.ui_window.login_label.text()
        password = self.ui_window.pass_label.text()

        #print(login, password)

        if self.student_mode:
            if self.conn.register_student(login, password):
                self.ui_window.login_label.setText("Успешно!")
                self.ui_window.pass_label.setText("Успешно!")

                self.user_login = login
                self.user_pass = password
            else:
                self.ui_window.login_label.setText("Ошибка!")
                self.ui_window.pass_label.setText("Ошибка!")
        else:
            if self.conn.register_teacher(login, password):
                self.ui_window.login_label.setText("Успешно!")
                self.ui_window.pass_label.setText("Успешно!")

                self.user_login = login
                self.user_pass = password
            else:
                self.ui_window.login_label.setText("Ошибка!")
                self.ui_window.pass_label.setText("Ошибка!")

    def login(self):
        login = self.ui_window.login_label.text()
        password = self.ui_window.pass_label.text()

        # print(login, password)

        if self.student_mode:
            if self.conn.login_student(login, password):
                self.ui_window.login_label.setText("Успешно!")
                self.ui_window.pass_label.setText("Успешно!")

                self.user_login = login
                self.user_pass = password

                self.new_window.close()
                self.list_problems()
            else:
                self.ui_window.login_label.setText("Ошибка!")
                self.ui_window.pass_label.setText("Ошибка!")
        else:
            if self.conn.login_teacher(login, password):
                self.ui_window.login_label.setText("Успешно!")
                self.ui_window.pass_label.setText("Успешно!")

                self.user_login = login
                self.user_pass = password

                self.new_window.close()
                self.teacher1()
            else:
                self.ui_window.login_label.setText("Ошибка!")
                self.ui_window.pass_label.setText("Ошибка!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Tester()
    window.show()

    sys.exit(app.exec())

