from mysql.connector import connect

db = connect(host='localhost', user='root', password='', database='python_db')

cursor = db.cursor()

sql = "SELECT names,height FROM students WHERE height < ( SELECT AVG(height) FROM students)"

cursor.execute(sql)
data = cursor.fetchall()

for item in data:
    print(item[0],item[1])