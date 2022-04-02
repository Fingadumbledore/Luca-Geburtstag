from mysql.connector import connect, Error

mydb = connect(
    host="localhost", user="root",password="password"
)

cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")

for database in cursor:
    print(database)