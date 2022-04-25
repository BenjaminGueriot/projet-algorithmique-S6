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
        listAllArrets=self.getAllArrets()
        dicShort=self.initDicShort()
        listAllArrets.remove(start)
        dicShort[start]=0

        def DijkstraSub(self,current,end,listAllArrets,dicShort):
            if current == end:
                return dicShort
            dicShort=md.updateDictionaryD(current,dicShort)
            newCurrent=md.getNewCurrent(listAllArrets,dicShort)
            listAllArrets.remove(newCurrent)
            return DijkstraSub(self,newCurrent,end,listAllArrets,dicShort)
            
        return DijkstraSub(self,start,end,listAllArrets,dicShort)