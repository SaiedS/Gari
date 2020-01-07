import mysql.connector
from mysql.connector import Error
from mysql.connector import connection



import os #si jamais ya un probleme avec BaseMap aller dans le chemin generalement dans programData: Anaconda3/Lib/site-packages/mpl_toolkits/basemap ensuite cree un dossier data puis mettre "epsg" dans ce dossier (sur discord)
#os.environ['PROJ_LIB'] = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\mpl_toolkits\\basemap\\data'

import pandas as pd
import numpy as np
import folium
from folium import plugins #pour utiliser des librairies GJSON de folium (l'animation)
from folium.plugins import FloatImage
from datetime import datetime
import time

def decoupTab(tab): # pour decouper en plusieurs tableau
    i = 0
    tailleN = len(tab)
    tabF = []
    temp = []
    while(i<tailleN):
        if i % 2 == 0:
            temp.append(tab[i])
            tabF.append(temp)
        else :
            temp.append(tab[i])
            temp = []
        i+=1
    return(tabF)

def decoupTab2(tab): # pour decouper en plusieurs tableau
    i = 0
    tabF = []

    temp = []
    while i<len(tab):
        temp.append(tab[i])

        if len(temp)==5:
            tabF.append(temp)
            temp = []
        i+=1
    return(tabF)

def coord_dep(): # recupere les coordonnées de depart
    cursor.execute("SELECT lng_dep,lat_dep FROM trouver")
    rows = cursor.fetchall()
    coord_dep = []
    for row in rows:
        coord_dep.append(float("{0}".format(row[1])))
        coord_dep.append(float("{0}".format(row[0])))
    coord_dep = decoupTab(coord_dep)
    return coord_dep

def coord_arr(): # recupere les coordonnées d'arrivées'
    cursor.execute("SELECT lng_arr,lat_arr FROM trouver")
    rows = cursor.fetchall()
    coord_arr = []
    for row in rows:
        coord_arr.append(float("{0}".format(row[1])))
        coord_arr.append(float("{0}".format(row[0])))
    coord_arr = decoupTab(coord_arr)
    return coord_arr

def date(): # recupere la date ou la personne à trouver sa place
    cursor.execute("SELECT date_heur FROM trouver")
    rows = cursor.fetchall()
    date = []
    for row in rows:
        date.append(str("{0}".format(row[0])))
    return date

def coord_depEtArr(tabDep, tabArr): # rassemblement coordonnee dep et arr
    tab = []
    i = 0
    taille = len(tabDep)
    while(i<taille):
        tab.append(tabDep[i])
        tab.append(tabArr[i])
        i+=1
    return tab

def cara():
    cursor.execute("SELECT marque,modele,couleur,matricule,type FROM voitures,donner where voitures.id = donner.id")
    rows = cursor.fetchall()
    voiture = []
    for row in rows :
        voiture.append(str("{0}".format(row[0])))
        voiture.append(str("{0}".format(row[1])))
        voiture.append(str("{0}".format(row[2])))
        voiture.append(str("{0}".format(row[3])))
        voiture.append(str("{0}".format(row[4])))
    voiture = decoupTab2(voiture)

    return voiture
def caraStr(tab):
    str = ""
    i = 0
    while i < len(tab):
        str = str + tab[i] + "\n"
        i = i + 1
    return str

def tabMatch(): # recupere les coordonnées d'arrivées'
    #cursor.execute("SELECT lng_arr,lat_arr,lng_dep,lat_dep FROM trouver")
    cursor.execute("SELECT lat_arr,lng_arr,lat_dep,lng_dep FROM trouver")
    rows = cursor.fetchall()
    coord_arr = []

    for row in rows:
        coord_arr.append(float("{0}".format(row[0])))
        coord_arr.append(float("{0}".format(row[1])))
        coord_arr.append(float("{0}".format(row[2])))
        coord_arr.append(float("{0}".format(row[3])))

    coord_arr = decoupTab(coord_arr)
    return coord_arr

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



        """fichier = open("test.csv","w") #récuperer les données de la bdd et les mettres dans un fichier .csv (si jamais on arrive pas a utiliser les donnees a partir d'une bdd alors on met les donnees de la bdd dans un fichier, c'est plus facile a manier enfin mon avis)
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
            fichier.write(str(row[9])+"\n")"""
            #Affichage de la table trouver
            #print("L'id de la personne : {0},\nPlace départ -> coordonnée départ: [{1};{2}]-> {3}.\nPlace trouvée -> coordonnée arrivée: [{4};{5}]-> {6} à {7}\n".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        """fichier.close()#fermer le fichier sinon le reste du coup ne fonctionnera pas
        #lire le ficher .csv et mettre dans la variable df
        df = pd.read_csv("test.csv", sep=';', encoding='latin-1')
        #Voir ce que contient df
        #print(df)"""

        # Map de paris, #location centre de Paris, #tiles format de la map, # zoom_control rajoute des boutons pour zoom
        m = folium.Map(location=[48.860419, 2.345341], tiles="cartodbpositron", zoom_start=12, width=1400, height=800,zoom_control=True)
        url=('https://raw.githubusercontent.com/SECOORA/static_assets/master/maps/img/rose.png')
        FloatImage(url, bottom=5, left=80).add_to(m)

        dep = coord_dep() #recupere les coordonnées de depart
        print(dep)


        match = tabMatch()
        #print(match)
        arr = coord_arr() #recupere les coordonnées d'arrivée
        #print(arr)
        date = date() #recupere les dates enregistrer pour chaque place trouver
        #print(date)

        cara = cara()
        #print(cara)
        coord_depEtArr = coord_depEtArr(dep,arr)#met dans un tab coordonnee de depart et arrive ensemble
        print(coord_depEtArr)
        data = {}
        data["coordonnee"] = coord_depEtArr #on charge le dictionnaire des coordonnees de dep
        data["date"] = date #pareille on mettant les dates
        data["couleur"] = 'red' # la je met uen couleur par defaut
        data["match"] = match
        #print(data)
        lines = [0] #initialise un tab
        lines[0] = data #on met le dict dans le tab
        #print(lines[0])

        i = 0
        nb = i
        nb2 = i
        while i < len(data["coordonnee"]):

            if i%2==0:
                folium.Marker(location=data["coordonnee"][i],popup= caraStr(cara[nb]),icon=folium.map.Icon(color='red',icon='')).add_to(m)
                #a = data["deplacement"][i]

                nb = nb + 1
            else:
                folium.Marker(location=data["coordonnee"][i],popup= caraStr(cara[nb2]),icon=folium.map.Icon(color='green',icon='')).add_to(m)
                #b = data["coordonnee"][i]

                #points_a = [[48.848067, 2.301280], [48.877505, 2.343289]]
                nb2 = nb2 + 1


            i = i + 1

        i = 0
        while i < len(data["match"])-1:
            points_a = [data["match"][i], data["match"][i+1]]
            folium.PolyLine(points_a, color="blue", weight=2.5, opacity=1,).add_to(m)
            i = i + 2



        #points_a = [[48.848067, 2.301280], [48.877505, 2.343289]]
        #folium.PolyLine(points_a, color="blue", weight=2.5, opacity=1).add_to(m)

    #features = [
    #    {
    #        'type': 'Feature',
    #        'geometry': { # pour tracer la ligne
    #            'type': 'LineString',
    #            'coordinates': line['coordonnee'], #trace la ligne par rapport au coordonnee de dep et arr
    #        },
    #        'properties': {
    #            'times': line['date'], # barre en bas de la map pour le temps
    #            'style': {
    #                'color': line['couleur'], #ligne couleur rouge par defaut
    #                'weight': line['taille'] if 'taille' in line else 5 #ici j'ai pas mis de clé 'taille' du coup par defaut le trait sera de taille 5
    #            }
    #        }
    #    }

    #    for line in lines #on parcourt le tableau Lines pour tracer chaque trait selon les parametres juste en dessus
    #    ]

    #    plugins.TimestampedGeoJson({
    #        'type': 'FeatureCollection',
    #        'features': features,
    #    }, period='P1D', add_last_point=True).add_to(m) #ici on met par defaut l'actualisation par jours(P1D pour mettre en heure : PT1H) et on actualise aussie le point dans la map

        m.save('testMapAnimation.html') # on enregistre la map dans un html.

except Error as e:
    print("Probleme de connexion à la base de données.", e)

if connection.is_connected():
    cursor.close()
    connection.close()
    print("Connection à la base de données fermée.")
