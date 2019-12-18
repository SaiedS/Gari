import mysql.connector
from mysql.connector import Error
from mysql.connector import connection

try:
    connection = mysql.connector.connect(host="localhost",user="root",password="123456789", database="gari")
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute("SELECT * FROM trouver")
        rows = cursor.fetchall()
        for row in rows:
            print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

except Error as e:
    print("Probleme de connexion à la base de données.", e)

if connection.is_connected():
    cursor.close()
    connection.close()
    print("Connection à la base de données est fermé.")
