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
        self.dic_horaire = {}
        self.lst_arret_suivant = []
        self.nb_ligne = 0

    def get_nom(self):
        return self.nom
    
    def get_lst_arret_suivant(self):
        return self.lst_arret_suivant

    def add_lst_arret_suivant(self,Arret):
        self.lst_arret_suivant.append(Arret)

    def add_horaire(self,h_regular_go,h_regular_back,h_special_go,h_special_back):
        self.nb_ligne += 1
        self.dic_horaire[("Ligne" + str(self.nb_ligne))] = { "regular_go" : h_regular_go, 
                                                                "regular_back" : h_regular_back, 
                                                                "special_go" : h_special_go, 
                                                                "special_back" : h_special_back }

    def get_horaire(self,periode,ligne):
        if(periode == "regular_go"):
            return self.dic_horaire.get("Ligne"+ str(ligne)).get("regular_go")
        if(periode == "regular_back"):
            return self.dic_horaire.get("Ligne"+ str(ligne)).get("regular_back")
        if(periode == "special_go"):
            return self.dic_horaire.get("Ligne"+ str(ligne)).get("special_go")
        if(periode == "special_back"):
            return self.dic_horaire.get("Ligne"+ str(ligne)).get("special_back")


        
        return self.dic_horaire
    
    def father(self,Ligne):

        for n in Ligne.Lst_Arret:
            if self in n.lst_arret_suivant  :
                return n
        return None

    def is_leaf(self):
        return not self.lst_arret_suivant

