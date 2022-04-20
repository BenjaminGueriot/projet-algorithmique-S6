#-*-coding:utf-8-*-

class Arret :
    
    def __init__(self, nom):
        
        """
        Constructeur de la classe Arret
        
        Parameters
        ----------
        nom : string
            nom de l'arret
        lst_arret_suivant : Arret[]
            Liste d'arret suivant        
        """

        self.nom = nom
        self.lst_arret_suivant = []

    def get_nom(self):
        return self.nom
    
    def get_lst_arret_suivant(self):
        return self.lst_arret_suivant

    def add_lst_arret_suivant(self,Arret):
        self.lst_arret_suivant.append(Arret)

    def father(self,Ligne):

        for n in Ligne.Lst_Arret:
            if self in n.lst_arret_suivant  :
                return n
        return None

    def is_leaf(self):
        return not self.lst_arret_suivant

