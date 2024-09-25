"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 06
Numéro d'équipe :  06
Noms et matricules : Portapia (2404203), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

import csv

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






########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

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







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






