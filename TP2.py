"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 06
Numéro d'équipe :  06
Noms et matricules : Portapia Astrid (2404203), Fortas_Rym (2385101)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

import csv

print("-----------------PARTIE 1----------------------")

#Ouverture du fichier
csvfile = open('collection_bibliotheque.csv', newline='')
#Positionnement du curseur de lecture au début du fichier
curs = csv.reader(csvfile)

bibliotheque = dict()
for row in curs:  #On parcourt toutes les lignes du fichier csv ouvert
    key = row[3]
    title = row[0]
    author = row[1]
    date = row[2]
    val = {"titre":title, "auteur":author, "date_parution":date}   #On choisit un dict pour représenter la value car on veut y accéder en faisant ["tire"] par exemple
    bibliotheque[key] = val

bibliotheque.pop("cote_rangement")  #On enlève la première clé qui était "cote_rangement" : (titre,auteur,date)

print(f' \n Bibliotheque initiale : {bibliotheque} \n')

#Fermeture du fichier après traitement
csvfile.close()




########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

#Ouverture du fichier
csvfile = open('nouvelle_collection.csv', newline='')
#Positionnement du curseur de lecture au début du fichier
curs = csv.reader(csvfile)

print("-----------------PARTIE 2----------------------")

for row in curs:  #On parcourt toutes les lignes du fichier csv ouvert
    key = row[3]
    title = row[0]
    author = row[1]
    date = row[2]
    
    if key != "cote_rangement" :
        if key not in bibliotheque.keys():
            val = {"titre":title, "auteur":author, "date_parution":date}
            bibliotheque[key] = val
            print(f"Le livre {key} ---- {title} par {author} ---- a été ajouté avec succès")
        else:
            print(f"Le livre {key} ---- {title} par {author} ---- est déjà présent dans la bibliothèque")

print(f' \n Bibliotheque mise à jour : {bibliotheque} \n')

#Fermeture du fichier après traitement
csvfile.close()






# ########################################################################################################## 
# # PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
# ########################################################################################################## 

print("-----------------PARTIE 3----------------------")

S = []  #Liste qui va contenir toutes les clés qui ont pour auteur Shakespeare de bibliotheque
for (k,v) in bibliotheque.items():
    if v["auteur"]=="William Shakespeare":
        S.append(k)    #on parcourt tous le dictionnaire pour récupérer toutes les clés qui correspondent à un livre de W.S.

if len(S)!=0:    #Si la liste S n'est pas vide : s'il existe des clés correspondant a un livre de W.S
    for k in S:
        val = bibliotheque[k]
        new_k = "WS"+k[1:]    #On met "WS" à la place de "S" avant les chiffres de la cote
        bibliotheque.pop(k)
        bibliotheque[new_k]=val
else:
    print('Pas de livre de William Shakespeare!')
print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')







# ########################################################################################################## 
# # PARTIE 4 : Emprunts et retours de livres
# ########################################################################################################## 

 # TODO : Écrire votre code ici
import csv
csvfile_3 = open('emprunts.csv', newline='')
h = csv.reader(csvfile_3)

print("-----------------PARTIE 4----------------------")

livres_empruntes = {}
for row in h :                   #On crée un dictionnaire avec que les livres empruntés
    date_emprunt= row[1]
    cote_rangement= row[0]
    livres_empruntes[cote_rangement] = date_emprunt

for (key, valeur) in bibliotheque.items():  #Pour chaque livre de la bibibliotheque
    for (key_1, valeur_1)in livres_empruntes.items():   #On va regarder s'il est emprunté
        if key == key_1:    #Si la cote du livre est dans livres_empruntes, on rajoute les clés "emprunt" et date_emprunt" a la valeur associéeau livre dans bibliotheque
            valeur['emprunt'] = "emprunté"
            valeur["date_emprunt"] = valeur_1
            break
        else:
             valeur['emprunt'] = "disponible"
print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')


# ########################################################################################################## 
# # PARTIE 5 : Livres en retard 
# ########################################################################################################## 

# TODO : Écrire votre code ici

import datetime
durée_emprunt_max = 30
frais_retard = 2
frais_max = 100

print("-----------------PARTIE 5----------------------")

for (key, valeur) in bibliotheque.items():
    if valeur['emprunt'] == "emprunté":
        valeur['livre perdu']= False
        valeur['Frais_retard'] = 0
        durée_emprunt = datetime.date.today() - datetime.datetime.strptime(valeur["date_emprunt"], "%Y-%m-%d").date()  #On récupère le nombre de jours entre le jour meeme
        jours_retard= (durée_emprunt - datetime.timedelta(days=30)).days
        if jours_retard > 0:
            if jours_retard*2 < frais_max:
                valeur['Frais_retard'] = int(jours_retard) * frais_retard
            else:
                valeur['Frais_retard'] = frais_max
        if jours_retard > 335:         #Livre perdu un an après la date d'emprunt, donc quand il y a plus de 335 jours de retard
            valeur['livre perdu']= True
            
print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')

for k,v in bibliotheque.items():
    if v["emprunt"]=="emprunté":     #on ne regarde que les livres qui sont empruntés
        if v["Frais_retard"]>0 and not v["livre perdu"]:      #si en retard et pas perdu
            print(f"Le livre \'{v['titre']}\' est emprunté et a ${v['Frais_retard']} de frais de retard")
        elif v["livre perdu"]:      #si perdu
            print(f"ATTENTION : le livre \'{v['titre']}\' est perdu !")




