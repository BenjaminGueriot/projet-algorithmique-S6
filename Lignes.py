#-*-coding:utf-8-*-

from Arret import Arret

class Lignes:
    
    def __init__(self, ArretDepart, Lst_Arret):
        
        """
        Constructeur de la classe ArbreArret
        
        Parameters
        ----------
        ArretDepart : Arret
            Depart de l'abre
        Lst_Arret : Arret[] 
            Liste des Arret de l'arbre      
        """
        self.ArretDepart = ArretDepart
        self.Lst_Arret = Lst_Arret

    def get_depart(self):
        return self.ArretDepart

    def get_Lst_Arret(self):
        return self.Lst_Arret

    def add_Lst_Arret(self,Arret):
        self.Lst_Arret.append(Arret)

    
