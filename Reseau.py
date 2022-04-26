from Lignes import *
from Arret import *
import Method as md
from math import inf

class Reseau:
    def __init__(self,lignes):
        self.lignes=lignes

    #renvoie une liste des lignes comprenant l'arrret stop
    def Lignesfor1Arret(self,arret):
        res=[]
        for e in self.lignes:
            if e.isInLigne(arret):
                res.append(e)
        return res

    def getAllArrets(self):
        res=[]
        for e in self.lignes:
            stop=e.ArretDepart
            while stop!=None:
                res.append(stop)
                stop=stop.get_arret_suivant(e)
        return res

    def initDicShort(self):
        res={}
        for e in self.getAllArrets():
            res[e]=inf
        return res
    
    
    def shortestDijkstra(self,start,end):

        #init
        dg = {}
        for elem in self.getAllArrets():
            dic = {}
            for e in elem.get_lst_arrets_suivant():
                if dic != {}:
                    dic = md.merge_two_dicts(dg.get(elem.get_nom()),{e.get_nom() : 1})
                else:
                    dic = {e.get_nom() : 1}
                dg[elem.get_nom()] = dic

        s_connu ={start.get_nom() : [0, [start.get_nom()]]}
        s_inconnu = {k : [inf,""] for k in dg if k != start.get_nom()}
        for suivant in dg[start.get_nom()]:
            s_inconnu[suivant] = [dg[start.get_nom()][suivant],start.get_nom()]
        
        #recherche

        while s_inconnu and any(s_inconnu[k][0] < inf for k in s_inconnu):
            u = min(s_inconnu, key = s_inconnu.get)
            
            longueur_u, precedent_u = s_inconnu[u]
            for v in dg[u]:
                if v in s_inconnu:
                    d = longueur_u + dg[u][v]
                    if d < s_inconnu[v][0]:
                        s_inconnu[v] = [d,u]
            s_connu[u] = [longueur_u, s_connu[precedent_u][1] + [u]]
            del s_inconnu[u]
            if u == end.get_nom():
                break

        return s_connu[end.get_nom()]
    