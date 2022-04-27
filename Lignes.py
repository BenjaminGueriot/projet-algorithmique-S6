#-*-coding:utf-8-*-
from math import inf
from time import time
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
        if arret.get_horaire(periode,self.numero) != None:
            inittime = arret.get_horaire(periode,self.numero)[0]
            while inittime == "-":
                i += 1
                inittime = arret.get_horaire(periode,self.numero)[i]
            
            time = Method.hdigit2min(inittime)
            while time < timeDeparture or count > len(arret.get_horaire(periode,self.numero)):
                if count == len(arret.get_horaire(periode,self.numero)):
                    break
                
                if arret.get_horaire(periode,self.numero)[count] == "-":
                    time = timeDeparture
                if(arret.get_horaire(periode,self.numero)[count] != "-"):
                    time = Method.hdigit2min(arret.get_horaire(periode,self.numero)[count])
                count += 1

        return time

    def time_between_arrets(self,heure,arret1,arret2,periode):
        
        #print(arret1.get_nom(),arret2.get_nom())
        time1 = self.nextBus(arret1,heure,periode)
        time2 = self.nextBus(arret2,self.nextBus(arret1,heure,periode),periode)

        if time1 == 0:
            time = 0
            return time
        
        time = time2 - time1        
              
        #print(Method.min2hdigit(time2),Method.min2hdigit(time1),time)
        return time
