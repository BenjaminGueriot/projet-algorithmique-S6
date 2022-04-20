from Arret import Arret
from Lignes import Lignes
import data2py as data
import data2py2 as data2

def creation_arret():
    lst_arret = []
    dic = {}

    for item in data.regular_date_go.keys() :
        lst_arret.append(item)

    for i in range(0,len(lst_arret)):

        lst_horaire = []
        lst_arret_suivant = []
        
        lst_horaire = data.regular_date_go.get(lst_arret[i])
        
        if i+1 < len(lst_arret) :
            lst_arret_suivant.append(lst_arret[i+1])
        
        if lst_arret[i] in dic :
            pass
        else :
            dic[lst_arret[i]] = Arret(lst_arret[i])


    for i in range(0,len(lst_arret)):
        lst_arret_suivant = []
        
        if i+1 < len(lst_arret) :
            dic.get(lst_arret[i]).add_lst_arret_suivant(dic.get(lst_arret[i+1]))

    """
    print(lst_arret[0])
    print(lst_horaire[0])
    print(lst_arret_suivant)
    """

    #print(dic.items())

    print((dic.get("LYCÃ‰E_DE_POISY")).get_lst_arret_suivant()[0])