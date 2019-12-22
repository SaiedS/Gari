import mysql.connector
from mysql.connector import Error
from mysql.connector import connection



import os #si jamais ya un probleme avec BaseMap aller dans le chemin generalement dans programData: Anaconda3/Lib/site-packages/mpl_toolkits/basemap ensuite cree un dossier data puis mettre "epsg" dans ce dossier (sur discord)
#os.environ['PROJ_LIB'] = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\mpl_toolkits\\basemap\\data'

import folium
from folium import plugins #pour utiliser des librairies GJSON de folium (l'animation)
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

def coord_dep(): # recupere les coordonnées de depart 
    cursor.execute("SELECT lng_dep,lat_dep FROM trouver")
    rows = cursor.fetchall()
    coord_dep = []
    for row in rows:
        coord_dep.append(float("{0}".format(row[0])))
        coord_dep.append(float("{0}".format(row[1])))
    coord_dep = decoupTab(coord_dep)     
    return coord_dep

def coord_arr(): # recupere les coordonnées d'arrivées'
    cursor.execute("SELECT lng_arr,lat_arr FROM trouver")
    rows = cursor.fetchall()
    coord_arr = []
    for row in rows:
        coord_arr.append(float("{0}".format(row[0])))
        coord_arr.append(float("{0}".format(row[1])))
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
       
            #Affichage de la table trouver
            #print("L'id de la personne : {0},\nPlace départ -> coordonnée départ: [{1};{2}]-> {3}.\nPlace trouvée -> coordonnée arrivée: [{4};{5}]-> {6} à {7}\n".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        
        # Map de paris, #location centre de Paris, #tiles format de la map, # zoom_control rajoute des boutons pour zoom
        m = folium.Map(location=[48.860419, 2.345341], tiles="cartodbpositron", zoom_start=12, width=900, height=600, zoom_control=True)
        
        dep = coord_dep() #recupere les coordonnées de depart
        #print(dep)
        arr = coord_arr() #recupere les coordonnées d'arrivée
        #print(arr)
        date = date() #recupere les dates enregistrer pour chaque place trouver
        #print(date)
        coord_depEtArr = coord_depEtArr(dep,arr)#met dans un tab coordonnee de depart et arrive ensemble
        #print(coord_depEtArr)
        data = {}
        data["coordonnee"] = coord_depEtArr #on charge le dictionnaire des coordonnees de dep
        data["date"] = date #pareille on mettant les dates 
        data["couleur"] = 'red' # la je met une couleur par defaut
        #print(data)
        lines = [0] #initialise un tab
        lines[0] = data #on met le dict dans le tab
        #print(lines[0])
        boole = False
        changeCoul = 'red'
        features = [
        {
            'type': 'Feature',
            'geometry': { # pour tracer la ligne
                'type': 'LineString',
                'coordinates': line['coordonnee'], #trace la ligne par rapport au coordonnee de dep et arr
            },
            'properties': {
                'times': line['date'], # barre en bas de la map pour le temps
                'style': {
                    'color': line['couleur'], #ligne couleur rouge par defaut
                    'weight': line['taille'] if 'taille' in line else 5 #ici j'ai pas mis de clé 'taille' du coup par defaut le trait sera de taille 5
                },
                'icon': 'circle',
                'iconstyle': {
                    'fillColor': changeCoul,
                    'fillOpacity': 0.6,
                    'stroke': 'false',
                    'radius': 13
                }
            }
        }
        for line in lines #on parcourt le tableau Lines pour tracer chaque trait selon les parametres juste en dessus
        ]

        plugins.TimestampedGeoJson(
        {
            'type': 'FeatureCollection',
            'features': features
        }, 
        period='PT1H',
        add_last_point=True,
        auto_play=True,
        loop=True,
        max_speed=20,
        loop_button=True,
        date_options='DD/MM/YYYY : HH:mm:ss',
        time_slider_drag_update=True,
        duration='P2M').add_to(m) #ici on met par defaut l'actualisation par jours(P1D pour mettre en heure : PT1H) et on actualise aussie le point dans la map

        m.save('testMapAnimation.html') # on enregistre la map dans un html.

except Error as e:
    print("Probleme de connexion à la base de données.", e)

if connection.is_connected():
    cursor.close()
    connection.close()
    print("Connection à la base de données fermée.")