from Arret import Arret
from Lignes import Lignes
import data2py as data
import data2py2 as data2

lst_arret = []
lst_arret2 = []
dic = {}
dic2 = {}
Ligne_lst_Arret = []
Ligne2_lst_Arret = []

def creation_arrets():

    #Creation première ligne
    lst_arret = get_arret_ligne(data.regular_date_go)

    for i in range(0,len(lst_arret)):

        if lst_arret[i] not in dic :
            dic[lst_arret[i]] = Arret(lst_arret[i])
            Ligne_lst_Arret.append(dic[lst_arret[i]])

    for i in range(0,len(lst_arret)):

        dic.get(lst_arret[i]).add_horaire(data.regular_date_go.get(lst_arret[i]),data.regular_date_back.get(lst_arret[i]),
                                        data.we_holidays_date_go.get(lst_arret[i]),data.we_holidays_date_back.get(lst_arret[i]))

        if i+1 < len(lst_arret) :
            dic.get(lst_arret[i]).add_lst_arret_suivant(dic.get(lst_arret[i+1]))
    

    #Creation de la seconde ligne
    lst_arret2 = get_arret_ligne(data2.regular_date_go)

    for i in range(0,len(lst_arret2)):
            
        if lst_arret2[i] not in dic :
            dic2[lst_arret2[i]] = Arret(lst_arret2[i])
            Ligne2_lst_Arret.append(dic2[lst_arret2[i]])
        else:
            dic2[lst_arret2[i]] = dic.get(lst_arret2[i])
            Ligne2_lst_Arret.append(dic[lst_arret2[i]])
            
    for i in range(0,len(lst_arret2)):
        
        dic2.get(lst_arret2[i]).add_horaire(data2.regular_date_go.get(lst_arret2[i]),data2.regular_date_back.get(lst_arret2[i]),
                                        data2.we_holidays_date_go.get(lst_arret2[i]),data2.we_holidays_date_back.get(lst_arret2[i]))

        if i+1 < len(lst_arret2) :
            dic2.get(lst_arret2[i]).add_lst_arret_suivant(dic2.get(lst_arret2[i+1]))

    #Creation de du dictionnaire contenant tous les arrets de toutes les lignes
    dic_arret = merge_two_dicts(dic,dic2)
    return dic_arret


def creation_lignes():
    dic_ligne = {}
    dic_ligne["Ligne1"] = Lignes(dic.get(get_arret_ligne(data.regular_date_go)[0]),Ligne_lst_Arret)
    dic_ligne["Ligne2"] = Lignes(dic.get(get_arret_ligne(data.regular_date_go)[0]),Ligne2_lst_Arret)
    return dic_ligne


#Retourne la liste de tout les arrets de la ligne selon la période
def get_arret_ligne(donnees):
    liste_arret = []
    for item in donnees.keys() :
        liste_arret.append(item)
    return liste_arret


#Fusionne deux dictionnaires
def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z