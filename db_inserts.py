from mysql.connector import connect

db = connect(host='localhost', user='root', password='', database='python_db')

cursor = db.cursor()

sql = "insert into students values(null,'Edwin Wanyoike', 'cgazzard1@imdb.com','1997-06-15','Male',2.00)"

cursor.execute(sql)

db.commit()
