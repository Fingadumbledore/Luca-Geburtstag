from mysql.connector import connect, Error
from getpass import getpass

try:
    with connect(
        host="localhost",
        user=input("Username> "),
        password=getpass("Password>"),
    ) as connection:
        print(connection)
except Error as e:
    print(e)