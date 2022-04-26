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
        self.lst_arret_suivant = {}

    def get_nom(self):
        return self.nom
    
    def get_lst_arrets_suivant(self):
        for i in range(0,len(self.lst_arret_suivant.keys())):
            if self.lst_arret_suivant.values():
                list(self.lst_arret_suivant.values())
        return list(self.lst_arret_suivant.values())

    def get_dic_arrets_suivant(self):
        return self.lst_arret_suivant

    def get_arret_suivant(self,ligne):

        if ligne.direction == "back":
            
            arret = self.lst_arret_suivant.get(str((ligne.numero))+"_back")
            return arret

        if ligne.direction == "go":
            
            arret = self.lst_arret_suivant.get(str((ligne.numero)))
            return arret
        

    def add_lst_arret_suivant(self,Arret,ligne):
        self.lst_arret_suivant[ligne] = Arret

    def add_horaire(self,h_regular_go,h_regular_back,h_special_go,h_special_back,nb_ligne):
        self.dic_horaire[("Ligne" + str(nb_ligne))] = { "regular_go" : h_regular_go, 
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
            print(self.dic_horaire.get("Ligne"+ str(ligne)).get("special_back"))
            return self.dic_horaire.get("Ligne"+ str(ligne)).get("special_back")

        return None
    
    def father(self,Ligne):

        for n in Ligne.Lst_Arret:
            if self in n.lst_arret_suivant  :
                return n
        return None

    def is_leaf(self,ligne):

        lst_arrets = []
        if ligne.direction == "back":
            for i in range(0,len(self.lst_arret_suivant.keys())):
                if self.lst_arret_suivant.get(str((ligne.numero+i))+"_back"):
                    lst_arrets.append(self.lst_arret_suivant.get(str((ligne.numero+i))+"_back"))
            if lst_arrets == []:
                return True
            else:
                return False

        if ligne.direction == "go":
            for i in range(0,len(self.lst_arret_suivant.keys())):
                if self.lst_arret_suivant.get(str((ligne.numero+i))):
                    lst_arrets.append(self.lst_arret_suivant.get(str((ligne.numero+i))))
            if lst_arrets == []:
                return True
            else:
                return False