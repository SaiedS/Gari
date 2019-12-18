import mysql.connector
from mysql.connector import Error
from mysql.connector import connection

try:
    connection = mysql.connector.connect(host="localhost",user="root",password="123456789", database="gari")
    if connection.is_connected():
        #db_Info = connection.get_server_info()
        #print("Version de votre logiciel SQL Server :", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Vous êtes connecté à la base de données :", record)
        cursor.execute("SELECT * FROM trouver")
        rows = cursor.fetchall()
        print("\n")
        for row in rows:
            print("L'id de la personne : {0},\nPlace départ -> coordonnée départ: [{1};{2}]-> {3}.\nPlace trouvée -> coordonnée arrivée: [{4};{5}]-> {6} à {7}\n".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

except Error as e:
    print("Probleme de connexion à la base de données.", e)

if connection.is_connected():
    cursor.close()
    connection.close()
    print("Connection à la base de données fermée.")
