#-*-coding:utf-8-*-
from datetime import datetime
import Method
import CreateArret as CA
from Arret import Arret
from Lignes import Lignes


dic_arret = CA.creation_arrets()
dic_ligne = CA.creation_lignes()

#print(((dic_arret.get("GARE")).get_lst_arret_suivant()[0]).get_nom())
#print(((dic_arret.get("GARE")).get_lst_arret_suivant()[1]).get_nom())
#print(dic_arret.get("GARE").get_horaire("special_go",1))
#print(dic_arret.get("GARE").get_horaire("regular_go",1))
#print(dic_arret.get("GARE").get_horaire("regular_go",2))

"""
for arret in dic_ligne.get("Ligne2").get_Lst_Arret():
    print(arret.get_nom())
"""

#print(dic_ligne.get("Ligne1").get_Lst_Arret().is_leaf())
#print(dic_ligne.get("Ligne1").get_Lst_Arret()[1].father(dic_ligne.get("Ligne1")).get_nom())


#date = int(str(datetime.date(datetime.now()))[5:7] + str(datetime.date(datetime.now()))[8:10])
#print(Method.is_holiday(date))

dic_ligne.get("Ligne1").display_depth(dic_ligne,dic_arret.get("Chorus"),dic_arret.get("Ponchy"))