import mysql.connector
from mysql.connector import Error
from mysql.connector import connection



import os #si jamais ya un probleme avec BaseMap aller dans le chemin generalement dans programData: Anaconda3/Lib/site-packages/mpl_toolkits/basemap ensuite cree un dossier data puis mettre "epsg" dans ce dossier (sur discord)
os.environ['PROJ_LIB'] = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\mpl_toolkits\\basemap\\data'

import matplotlib.animation as animation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from folium import plugins


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
        
        fichier = open("test.csv","w") #récuperer les données de la bdd et les mettres dans un fichier .csv (si jamais on arrive pas a utiliser les donnees a partir d'une bdd alors on met les donnees de la bdd dans un fichier, c'est plus facile a manier enfin mon avis)
        fichier.write("id;lat_dep;lng_dep;adresse_dep;lat_arr;lng_arr;adresse_arr;date_heur;id_user;etat\n")
        for row in rows:
            fichier.write(str(row[0])+";")
            fichier.write(str(row[1])+";")
            fichier.write(str(row[2])+";")
            fichier.write(str(row[3])+";")
            fichier.write(str(row[4])+";")
            fichier.write(str(row[5])+";")
            fichier.write(str(row[6])+";")
            fichier.write(str(row[7])+";")
            fichier.write(str(row[8])+";")
            fichier.write(str(row[9])+"\n")
            #Affichage de la table trouver
            print("L'id de la personne : {0},\nPlace départ -> coordonnée départ: [{1};{2}]-> {3}.\nPlace trouvée -> coordonnée arrivée: [{4};{5}]-> {6} à {7}\n".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            
        fichier.close()#fermer le fichier sinon le reste du coup ne fonctionnera pas       
        
        #lire le ficher .csv et mettre dans la variable df
        df = pd.read_csv("test.csv", sep=';', encoding='latin-1') 
        #Voir ce que contient df
        print(df)

        
        
        # on met les coordonnées de depart (pour test)
        points = (df.lat_dep.fillna(0),df.lng_dep.fillna(0))
        coordinates =[]
        # On met les coordonnées de dep
        lat = points[0]
        long = points[1]
        # Map de paris
        m = folium.Map(location=[48.860419, 2.345341], tiles="cartodbpositron", zoom_start=12, width=900, height=600)
        #la ici ça doit l'afficher mais ça le fait pas (jsp encore pq)
        m
        # lat_dep et lng_dep de la bdd test pour faire des points
        for la,lo in zip(lat,long):
            coordinates.append([la,lo])

        m.add_child(plugins.FastMarkerCluster(coordinates[0:40000])) #ici pour que les points qu'on a ajouté soit en forme de marqueur
        m #pareille ça doit afficher mais ca fait rien
        m.save('index.html') #du coup je save en html et j'ouvre l'html

except Error as e:
    print("Probleme de connexion à la base de données.", e)

if connection.is_connected():
    cursor.close()
    connection.close()
    print("Connection à la base de données fermée.")