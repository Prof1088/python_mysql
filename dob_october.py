from mysql.connector import connect

db = connect(host='localhost', user='root', password='', database='python_db')

cursor = db.cursor()

sql = "select names, dob from students where MONTH(dob)=10"

cursor.execute(sql)
data = cursor.fetchall()