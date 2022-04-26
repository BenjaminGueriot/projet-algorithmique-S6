#-*-coding:utf-8-*-
from math import inf
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
        time = 0
        if arret != None:
            inittime = arret.get_horaire(periode,self.numero)[0]
            while inittime == "-":
                i += 1
                inittime = arret.get_horaire(periode,self.numero)[i]
            
            time = Method.hdigit2min(inittime)
            while time < timeDeparture or count > len(arret.get_horaire(periode,self.numero)) or time == "-":
                count += 1
                if(arret.get_horaire(periode,self.numero)[count] != "-"):
                    time = Method.hdigit2min(arret.get_horaire(periode,self.numero)[count])

        return time


    def time_between_arret(self,heure,arret1,periode):
       
        arret2 = arret1.get_arret_suivant(self)
        time = self.nextBus(arret2,self.nextBus(arret1,heure,periode),periode) - self.nextBus(arret1,heure,periode)
        
        return time
