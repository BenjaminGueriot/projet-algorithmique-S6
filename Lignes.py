#-*-coding:utf-8-*-

from Arret import Arret

class Lignes:
    
    def __init__(self, ArretDepart,Lst_Arret):
        
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

    def display_depth(self,dic_ligne,arretDebut,arretFin):
        
        """
        Méthode pour réaliser une recherche en profondeur 
        
        Parameters
        ----------
        forest : RTree[]
            Arborescences qu'il reste à explorer
        nodes : Node[]
            Noeuds trouvés
            
        Returns
        ----------
        nodes : Node[]
        """

        count_route = 0
        dic_route = {}
        start = 0
        lst_routes = []

        def dfs(forest,dic_ligne,count_route,arretDebut,arretFin,start,lst_routes):
            if forest:
                ligne = forest[0]
                if(ligne.ArretDepart == arretDebut):
                    start = 1
                if ligne.ArretDepart != arretFin and ligne.ArretDepart.is_leaf():
                    new_forest = forest[1:]
                    dfs(new_forest,dic_ligne,count_route,arretDebut,arretFin,start,lst_routes)
                else :
                    if start == 1:
                        lst_routes.append(ligne.ArretDepart.nom)

                    if ligne.ArretDepart == arretFin:
                        count_route += 1
                        dic_route["Route"+str(count_route)] = lst_routes
                        lst_routes = []
                        new_forest = forest[1:]
                    else :
                        new_forest = [Lignes(arret, self.Lst_Arret) for arret in ligne.ArretDepart.get_lst_arret_suivant()] + forest[1:]

                    dfs(new_forest,dic_ligne,count_route,arretDebut,arretFin,start,lst_routes)

        dfs([self],dic_ligne,count_route,arretDebut,arretFin,start,lst_routes)
        print(dic_route)
        return dic_route