from mysql.connector import connect

db = connect(host='localhost', user='root', password='', database='python_db')

cursor = db.cursor()

sql = "delete from students where id =103 "

cursor.execute(sql)

db.commit()