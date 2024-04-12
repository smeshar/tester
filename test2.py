from PySide6 import QtWidgets, QtSql


class Data():
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expenses_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database!", "Click cancel to exit",
                                           QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Category VARCHAR(20), Description VARCHAR(20), Balance REAL, Status VARCHAR(20))")

        return True

    def execute_query_with_params(self, sql_query, query_vals=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_vals is not None:
            for query_val in query_vals:
                query.addBindValue(query_val)

        query.exec()
        return query
    def add_new_transaction(self, date, category, description, balance, status):
        sql_query = "INSERT INTO expenses (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status])

    def edit_transaction(self, date, category, description, balance, status, id):
        sql_query = "UPDATE expenses SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status, id])

    def delete_transaction(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM ({column}) FROM expenses"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_vals = []
        if value is not None:
            query_vals.append(value)

        query = self.execute_query_with_params(sql_query, query_vals)

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_balance(self):
        return self.get_total(column="Balance")

    def total_income(self):
        return self.get_total(column="Balance", filter="Status", value="Income")

    def total_outcome(self):
        return self.get_total(column="Balance", filter="Status", value="Outcome")[1:]

    def total_groceries(self):
        return self.get_total(column="Balance", filter="Category", value="Groceries")

    def total_auto(self):
        return self.get_total(column="Balance", filter="Category", value="Auto")

    def total_entertainment(self):
        return self.get_total(column="Balance", filter="Category", value="Entertainment")

    def total_other(self):
        return self.get_total(column="Balance", filter="Category", value="Other")
