from Arret import Arret
from Lignes import Lignes
import data2py as data


dic_ligne = {}
def creation_arrets(data_file,dic,nb_ligne):
    Ligne_lst_Arret = []
    lst_arret = []

    #Creation première ligne
    lst_arret = get_arret_ligne(data_file["regular_date_go"])
    lst_arret_rv = get_arret_ligne(data_file["regular_date_back"])

    for i in range(0,len(lst_arret)):

        if lst_arret[i] not in dic :
            dic[lst_arret[i]] = Arret(lst_arret[i])
        
        Ligne_lst_Arret.append(dic[lst_arret[i]])

        dic.get(lst_arret[i]).add_horaire(data_file["regular_date_go"].get(lst_arret[i]),data_file["regular_date_back"].get(lst_arret[i]),
                                        data_file["we_holidays_date_go"].get(lst_arret[i]),data_file["we_holidays_date_back"].get(lst_arret[i]),
                                        nb_ligne)

    for i in range(0,len(lst_arret)):

        if i+1 < len(lst_arret) :
            
            dic.get(lst_arret[i]).add_lst_arret_suivant(dic.get(lst_arret[i+1]),str(nb_ligne))

    for i in range(0,len(lst_arret_rv)):

        if i+1 < len(lst_arret) :
            
            dic.get(lst_arret_rv[i]).add_lst_arret_suivant(dic.get(lst_arret_rv[i+1]),str(nb_ligne) + "_back")

    dic_ligne["Ligne" + str(nb_ligne)] = Lignes(dic.get(get_arret_ligne(data_file["regular_date_go"])[0]),Ligne_lst_Arret,nb_ligne,"go")

    Ligne_lst_Arret_rv= list(reversed(Ligne_lst_Arret))

    dic_ligne["Ligne" + str(nb_ligne) +"_back"] = Lignes(dic.get(get_arret_ligne(data_file["regular_date_back"])[0]),Ligne_lst_Arret_rv,nb_ligne,"back")

    return { "dic_arret" : dic,
            "dic_ligne" : dic_ligne
            }

#Retourne la liste de tout les arrets de la ligne selon la période
def get_arret_ligne(donnees):
    liste_arret = []
    for item in donnees.keys() :
        liste_arret.append(item)
    return liste_arret

