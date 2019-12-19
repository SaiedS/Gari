import mysql.connector
from mysql.connector import Error
from mysql.connector import connection

"""from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd"""

import os #si jamais ya un probleme avec BaseMap aller dans le chemin generalement dans programData: Anaconda3/Lib/site-packages/mpl_toolkits/basemap ensuite cree un dossier data puis mettre "epsg" dans ce dossier (sur discord)
os.environ['PROJ_LIB'] = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\mpl_toolkits\\basemap\\data'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.basemap import Basemap


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
        
        #lire le ficher .csv et mettre dans la variable df
        #df = pd.read_csv('test.csv', names=['id', 'lat_dep', 'lng_dep', 'adresse_dep', 'lat_arr', 'lng_arr', 'adresse_arr', 'date_heur', 'id_user', 'etat'])
        
        fig=plt.figure()

        #Initialisation de la map qui faudra mettre en folium au lieu de basemap.
        bmap=Basemap(projection='merc', llcrnrlat=17.5,urcrnrlat=19.,llcrnrlon=-67.5, urcrnrlon=-65, epsg=4139)
        bmap.arcgisimage(service='World_Shaded_Relief', xpixels = 2000)
        plt.title("Test animation avec une map en background")

        #Generer 100 points
        N = 100
        lon = np.linspace(-64, -68, N)
        lat = np.linspace(17, 19.5, N)

        #convertir pour avoir des points de coordonnées    
        x,y = bmap(lon, lat)

        #generer une ligne d'origine avec un seulement point 
        line, = bmap.plot(x[0], y[0], linewidth = 1, color = 'm')

        def animate(i):
            #A chaque fois que cette fonctione Animate est appelé la ligne s'actualise point par point
            line.set_data(x[:i],y[:i])  
            return line
        #pour l'animation
        anim=animation.FuncAnimation(fig, animate, frames=N, interval=N)
        #afficher la map et les points
        plt.show()

except Error as e:
    print("Probleme de connexion à la base de données.", e)

if connection.is_connected():
    cursor.close()
    connection.close()
    print("Connection à la base de données fermée.")