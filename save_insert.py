from mysql.connector import connect

db = connect(host='localhost', user='root', password='', database='python_db')

cursor = db.cursor()
# sql injection
data = ('','Edwin Wanyoike','cgazzard1@imdb.com','1997-06-15','Male',2.00)

sql = "insert into students values(%s,%s,%s,%s,%s,%s)"

# dynamic binding mitigates sql injection
cursor.execute(sql, data)

db.commit()