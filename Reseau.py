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
            if arret in e.lst_Arret:
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

    def fastestDijkstra(self,start,end,periode,heure):

        #init
        dg = {}
        init = 0
        heure = Method.hdigit2min(heure)
        for elem in self.getAllArrets():
            dic = {}
            for e in elem.get_lst_arrets_suivant():
                poids = 0
                i = 0
                if len(self.Lignesfor1Arret(elem)) != 1:
                    
                    for line in self.Lignesfor1Arret(elem):
                        if e in line.lst_Arret:
                            ligne = self.Lignesfor1Arret(e)[i]
                            i += 1
                else:
                    ligne = self.Lignesfor1Arret(e)[i]

                for line in self.Lignesfor1Arret(elem):
                    if e in line.lst_Arret:
                        if elem.get_arret_suivant(line) == e:
                            new_periode = periode + "_" + line.direction

                if(elem == start):
                    poids = ligne.time_between_arrets(heure,elem,e,new_periode)
                    init = 1
                elif(init > 0):
                    poids = ligne.time_between_arrets(heure,elem,e,new_periode)

                if dic != {}:
                    dic = md.merge_two_dicts(dg.get(elem.get_nom()),{e.get_nom() : poids})
                else:
                    dic = {e.get_nom() : poids}
                dg[elem.get_nom()] = dic
            heure += poids

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


    def foremostDijkstra(self,start,end,periode,initheure):

        #init
        dg = {}
        init = 0
        initheure = Method.hdigit2min(initheure)
        heure = initheure
        for elem in self.getAllArrets():
            dic = {}
            for e in elem.get_lst_arrets_suivant():
                poids = 0

                i = 0
                if len(self.Lignesfor1Arret(elem)) != 1:
                    
                    for line in self.Lignesfor1Arret(elem):
                        if e in line.lst_Arret:
                            ligne = self.Lignesfor1Arret(e)[i]
                            i += 1
                else:
                    ligne = self.Lignesfor1Arret(e)[i]

                for line in self.Lignesfor1Arret(elem):
                    if e in line.lst_Arret:
                        if elem.get_arret_suivant(line) == e:
                            new_periode = periode + "_" + line.direction

                if(elem == start):
                    poids = (ligne.time_between_arrets(heure,elem,e,new_periode) + (ligne.nextBus(start,initheure,new_periode) + initheure))
                    init = 1
                if(init > 0):
                    poids = ligne.time_between_arrets(heure,elem,e,new_periode)

                if dic != {}:
                    print(ligne.nextBus(start,initheure,new_periode))
                    dic = md.merge_two_dicts(dg.get(elem.get_nom()),{e.get_nom() : poids})
                else:
                    dic = {e.get_nom() : poids}
                
                dg[elem.get_nom()] = dic
            heure += poids

 
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
    