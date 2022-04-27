#-*-coding:utf-8-*-
from datetime import datetime
import data2py as d2p
import Method
import CreateArret as CA
from Arret import Arret
from Lignes import Lignes
from Reseau import *

lst_files = ['1_Poisy-ParcDesGlaisins.txt','2_Piscine-Patinoire_Campus.txt']



def showStops():

    for arret in dic_arret.values():

        print("{}".format(arret.nom))


if __name__ == '__main__':

    dic_arret ={}
    nb_ligne = 0
    for files in lst_files:
        nb_ligne += 1
        data = d2p.read_data(files)
        dic = CA.creation_arrets(data, dic_arret,nb_ligne)
        dic_arret = dic["dic_arret"]
        dic_ligne = dic["dic_ligne"]

    print("Voici la liste des arrêts : ")

    showStops()

    print('Choisissez un arrêt de départ : ')
    arretdebut = input()

    print('Choisissez un arrêt d\'arrivée : ')
    arretfin = input()

    print('Choisissez une heure de départ (format hh:mm): ')
    heure = input()


#date = int(str(datetime.date(datetime.now()))[5:7] + str(datetime.date(datetime.now()))[8:10])
#print(Method.is_holiday(date))

#dic_ligne.get("Ligne2").get_all_path(dic_ligne,dic_arret.get("Courier"),dic_arret.get("Ponchy"))

#print(dic_ligne.get("Ligne1").time_between_arret(406,dic_arret.get("Vernod"),"regular_back"))

Sybra = Reseau(list(dic_ligne.values()))

dico_short = Sybra.shortestDijkstra(dic_arret.get(arretdebut),dic_arret.get(arretfin))
dico_fast = Sybra.fastestDijkstra(dic_arret.get(arretdebut),dic_arret.get(arretfin),"regular",heure)
dico_foremost = Sybra.foremostDijkstra(dic_arret.get(arretdebut),dic_arret.get(arretfin),"regular",heure)

print("shortest path : ",dico_short[1] ,"en ",dico_short[0],"arrets")
print("fastest path : ",dico_fast[1],"en ",dico_fast[0],"minutes")
print("foremost path : ",dico_foremost[1],"en ",dico_foremost[0],"minutes")
