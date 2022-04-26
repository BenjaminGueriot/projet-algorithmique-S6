#-*-coding:utf-8-*-

from Arret import Arret
import Method

class Lignes:
    
    def __init__(self, ArretDepart,lst_Arret,numero,direction):
        
        """
        Constructeur de la classe ArbreArret
        
        Parameters
        ----------
        ArretDepart : Arret
            Depart de l'abre
        Lst_Arret : Arret[]
            Liste des Arret de l'arbre      
        """

        self.numero = numero
        self.ArretDepart = ArretDepart
        self.lst_Arret = lst_Arret
        self.direction = direction

    def get_depart(self):
        return self.ArretDepart

    def nextBus(self,arret,timeDeparture,periode):
            
        count = 0
        i = 0
        inittime = arret.get_horaire(periode,self.numero)[0]
        while inittime == "-":
            i += 1
            inittime = arret.get_horaire(periode,self.numero)[i]
            
        print(timeDeparture)
        time = Method.hdigit2min(inittime)
        while time < timeDeparture or count > len(arret.get_horaire(periode,self.numero)) or time == "-":
            count += 1
            if(arret.get_horaire(periode,self.numero)[count] != "-"):
                time = Method.hdigit2min(arret.get_horaire(periode,self.numero)[count])

            
        return time


    def time_between_arret(self,heure,arret1,periode):
       
        arret2 = arret1.get_arret_suivant(self)
        print(arret2)

        print(self.nextBus(arret1,heure,periode))
        print(self.nextBus(arret2,self.nextBus(arret1,heure,periode),periode))
        time = self.nextBus(arret2,self.nextBus(arret1,heure,periode),periode) - self.nextBus(arret1,heure,periode)
        
        return time


    def findArret(self,arret):
        res=self.ArretDepart
        try:
            while res != arret:
                res = res.get_arret_suivant(self)
            return res
        except AttributeError:
            return None
"""
    def isInLigne(self,arret):
        try:
             ifarret = self.findArret(arret)
             return True
        except:
            return False
"""