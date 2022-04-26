#-*-coding:utf-8-*-
from datetime import datetime
import data2py as d2p
import Method
import CreateArret as CA
from Arret import Arret
from Lignes import Lignes
from Reseau import *

lst_files = ['1_Poisy-ParcDesGlaisins.txt','2_Piscine-Patinoire_Campus.txt']

dic_arret ={}
nb_ligne = 0
for files in lst_files:
    nb_ligne += 1
    data = d2p.read_data(files)
    dic = CA.creation_arrets(data, dic_arret,nb_ligne)
    dic_arret = dic["dic_arret"]
    dic_ligne = dic["dic_ligne"]



#print((dic_arret.get("GARE")).get_lst_arrets_suivant().get("1_back").get_nom())

#print((dic_arret.get("GARE")).get_arret_suivant(dic_ligne.get("Ligne2_back")).get_nom())

#print(dic_arret.get("GARE").get_horaire("special_go",1))
#print(dic_arret.get("GARE").get_horaire("regular_go",1))
#print(Method.hdigit2min(dic_arret.get("GARE").get_horaire("regular_go",2)[5]))

"""
for arret in dic_ligne.get("Ligne2_back").get_Lst_Arret():
    print(arret.get_nom())
"""

#print(dic_ligne)

#print(dic_ligne.get("Ligne1").get_Lst_Arret()[0].is_leaf(dic_ligne.get("Ligne1")))


#date = int(str(datetime.date(datetime.now()))[5:7] + str(datetime.date(datetime.now()))[8:10])
#print(Method.is_holiday(date))

#dic_ligne.get("Ligne2").get_all_path(dic_ligne,dic_arret.get("Courier"),dic_arret.get("Ponchy"))


#print(dic_ligne.get("Ligne1").time_between_arret(406,dic_arret.get("Vernod"),"regular_back"))

Sybra = Reseau(list(dic_ligne.values()))

#dico = Sybra.shortestDijkstra(dic_arret.get("GARE"),dic_arret.get("VIGNIÃˆRES"))
dico = Sybra.fastestDijkstra(dic_arret.get("GARE"),dic_arret.get("VIGNIÃˆRES"),"special","7:10")

print(dico[1])


