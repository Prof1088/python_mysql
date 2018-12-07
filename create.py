from mysql.connector import connect

db = connect(host='localhost', user='root', password='', database='python_db')

cursor = db.cursor()

sql = "select * from students where id=50"

cursor.execute(sql)
data = cursor.fetchone()

print(data)

print(data[1])
# printing one item by the data the above name

print(data[4])