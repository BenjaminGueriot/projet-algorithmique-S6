#-*-coding:utf-8-*-
import CreateArret as CA
from Arret import Arret
from Lignes import Lignes
import data2py as data
import data2py2 as data2


dic_arret = CA.creation_arrets()
dic_ligne = CA.creation_lignes()

#print(((dic_arret.get("GARE")).get_lst_arret_suivant()[0]).get_nom())
#print(((dic_arret.get("GARE")).get_lst_arret_suivant()[1]).get_nom())
#print(dic_arret.get("GARE").get_horaire("special_go",1))
#print(dic_arret.get("GARE").get_horaire("regular_go",1))
#print(dic_arret.get("GARE").get_horaire("regular_go",2))

#print(dic_ligne.get("Ligne1").get_Lst_Arret()[11].is_leaf())




