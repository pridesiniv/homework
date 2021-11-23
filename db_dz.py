import sqlite3 as sql
import random


class DBWorker:
    def __init__(self, db_name):
        self.cur_db = sql.connect(db_name)
        self.cursor = None
        self.result = None

    def connect_db(self):
        self.cursor = self.cur_db.cursor()

    def use_query(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.cur_db.commit()

    def use_query1(self, query, a):
        self.cursor.execute(query, a)
        self.result = self.cursor.fetchall()
        self.cur_db.commit()

    def return_result(self):
        return self.result


my_db = DBWorker('slovo.db')
my_db1 = DBWorker('chuslo.db')
my_db.connect_db()
my_db1.connect_db()
my_db.use_query('''CREATE TABLE  tab_2(col_1 TEXT)''')
my_db1.use_query('''CREATE TABLE tab_3(col_1 INTEGER)''')
my_list = [1, 'asdasd', 212, 23, 4, 5, 67, 8, 'asd', 'fhhh', 'vjhher', 3, 'asd']
for i in my_list:
    if type(i) is str:
        a = len(i)
        my_db.use_query1('INSERT INTO tab_2(col_1) VALUES (?)', (i,))
        my_db1.use_query1('INSERT INTO tab_3(col_1) VALUES (?)', (a,))
    else:
        if i % 2 == 0:
            my_db1.use_query1('INSERT INTO tab_3(col_1) VALUES (?)', (i,))
        else:
            my_db.use_query('INSERT INTO tab_2(col_1) VALUES ("нечётное")')

my_db1.use_query('SELECT*FROM tab_3')
k = my_db1.result
if len(k) > 5:
    t = random.randint(1,5)
    my_db.use_query1('DELETE FROM tab_2 WHERE col_1 = (?)',(t,))
else:
    h = random.randint(1,5)
    my_db.use_query1('UPDATE tab_2 SET col_1 = "hello" WHERE id=?',(h,))
my_db.use_query('SELECT*FROM tab_2')
a1 = my_db.return_result()
a2 = my_db1.return_result()
print(a1)
print(a2)
