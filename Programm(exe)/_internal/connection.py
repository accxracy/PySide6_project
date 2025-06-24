import sqlite3 as sq

# основной класс со всеми методами
class Data:
    def __init__(self):
        # создание БД
        with sq.connect('Expence.db') as con:
            self.cur = con.cursor()

            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS expenses( 
                   ID integer primary key AUTOINCREMENT, 
                   Date VARCHAR(20), 
                   Category VARCHAR(20), 
                   Description VARCHAR(20), 
                   Summa REAL,
                   Status VARCHAR(20)
            )""")
            # таблица с операциями


            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS categories(
                category_name VARCHAR(20)
                
                ) 
            """)
            # таблица с категориями

            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS user(
            username VARCHAR(20))""")

            # таблица с юзернеймами

    # основной метод для работы с БД, он получает сам запрос к БД и данные, которые нужно передать в БД
    def execute_with_params(self, sql_query, query_values=None):
        with sq.connect('Expence.db') as con:
            cur = con.cursor()
            cur.execute(sql_query, query_values)

    # добавляем категорию в БД
    def new_category_creation(self, category_name):
        self.execute_with_params('INSERT INTO categories(category_name) VALUES(?)',(category_name,))

    # возвращаем список категорий для комбобокса
    def get_categories(self):
        with sq.connect('Expence.db') as con:
            cur = con.cursor()
            cur.execute("SELECT DISTINCT category_name FROM categories")
            res = cur.fetchall()
            return res

    # создаем транзакцию
    def create_transaction_all(self, date, category, summa, status, description='no description'):
        sql_query = 'INSERT INTO expenses(Date, Category, Description, Summa, Status) VALUES(?, ?, ?, ?, ?);'
        data_tuple = (date, category, description, summa, status)
        self.execute_with_params(sql_query, data_tuple)

    # возвращаем категории для виджетов
    def get_categories_for_plain(self, operation):
        with sq.connect('Expence.db') as con:
            cur = con.cursor()
            req = f"""SELECT category, SUM(SUMMA) FROM expenses WHERE Status = ? GROUP BY category """
            return cur.execute(req, (operation, )).fetchall()

    # возвращаем сумму расходов
    def outcomes(self):
        with sq.connect('Expence.db') as con:
            cur = con.cursor()
            x = cur.execute("""SELECT SUM(Summa) from expenses where Status = 'outcome'""").fetchall()[0][0]
            if x:
                return x
            return 0

    # возвращаем сумму доходов
    def incomes(self):
        with sq.connect('Expence.db') as con:
            cur = con.cursor()
            x = cur.execute("""SELECT SUM(Summa) from expenses where Status = 'income'""").fetchall()[0][0]
            if x:
                return x
            return 0

    # возвращаем сумму долгов
    def duties(self):
        with sq.connect('Expence.db') as con:
            cur = con.cursor()
            x = cur.execute("""SELECT SUM(Summa) from expenses where Status = 'duty'""").fetchall()[0][0]
            if x:
                return x
            return 0

    # удаляем транзакцию из БД
    def delete_transaction(self, id):
        req = """DELETE FROM expenses WHERE ID = ?"""
        values = (id, )
        self.execute_with_params(req, values)

    # изменяем транзакцию в БД
    def edit_transaction(self, date, category, summa, id_to_edit, description='no description'):
        req = """UPDATE expenses SET Date = ?, Category = ?, Description = ?, Summa = ? WHERE ID = ?"""
        values = (date, category, description, summa, id_to_edit)
        self.execute_with_params(req, values)

    # добавляем новый никнейм в БД
    def nickname_change(self, newnickname):
        with sq.connect('Expence.db') as con:
            cur = con.cursor()
            req = """INSERT INTO user VALUES(?)"""
            values = (newnickname, )
            cur.execute(req, values)

    # возвращаем никнейм
    def get_nickname(self):
        with sq.connect('Expence.db') as con:
            cur = con.cursor()
            if cur.execute("""SELECT username FROM user""").fetchall():
                return cur.execute("""SELECT username FROM user""").fetchall()[-1][0]
            return 'user'

    # возвращаем данные для таблицы, функция получает операцию (расход, доход или долг) и id(по умолчанию None)
    def data_all(self, operation, id=None):
        with sq.connect('Expence.db') as con:
            if id:
                cur = con.cursor()
                req = """SELECT ID, Date, Category, Description, Summa FROM expenses WHERE Status = ? AND ID = ?"""
                values = (operation, id)
                x = cur.execute(req, values).fetchall()

            else:
                cur = con.cursor()
                req = """SELECT ID, Date, Category, Description, Summa FROM expenses WHERE Status = ?"""
                values = (operation,)
                x = cur.execute(req, values).fetchall()
            return x