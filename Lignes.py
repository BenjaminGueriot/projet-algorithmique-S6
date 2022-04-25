#-*-coding:utf-8-*-

from Arret import Arret
import Method

class Lignes:
    
    def __init__(self, ArretDepart,Lst_Arret,numero,direction):
        
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
        self.direction = direction

    def get_depart(self):
        return self.ArretDepart

    def get_Lst_Arret(self):
        return self.Lst_Arret

    def add_Lst_Arret(self,Arret):
        self.Lst_Arret.append(Arret)
    """
    def get_all_path(self,dic_ligne,arretDebut,arretFin):

        count_route = 0
        dic_route = {}
        start = 0
        lst_routes = []

        def sub(forest,dic_ligne,count_route,arretDebut,arretFin,start,lst_routes):
            if forest:
                ligne = forest[0]
                
                if(ligne.ArretDepart == arretDebut):
                    start = 1
                if (ligne.ArretDepart != arretFin) and (ligne.ArretDepart.is_leaf(ligne)):
                    new_forest = forest[1:]
                    sub(new_forest,dic_ligne,count_route,arretDebut,arretFin,start,lst_routes)
                else :
                    if start == 1:
                        lst_routes.append(ligne.ArretDepart.get_nom())

                    if ligne.ArretDepart == arretFin:
                        count_route += 1
                        dic_route["Route"+str(count_route)] = lst_routes
                        lst_routes = []
                        new_forest = forest[1:]
                    else :
                        new_forest = [Lignes(arret, self.Lst_Arret,ligne.numero,ligne.direction) for arret in ligne.ArretDepart.get_lst_arret_suivant(ligne)] + forest[1:]
                        if len(ligne.ArretDepart.get_lst_arret_suivant(ligne)) > 1:
                            pass

                    sub(new_forest,dic_ligne,count_route,arretDebut,arretFin,start,lst_routes)

        sub([self],dic_ligne,count_route,arretDebut,arretFin,start,lst_routes)
        print(dic_route)
        return dic_route
    """

    def nextBus(self,arret,timeDeparture,periode):
            
        count = 0
        time = Method.hdigit2min(arret.get_horaire(periode,self.numero)[0])
        while time < timeDeparture or count > len(arret.get_horaire(periode,self.numero)):
            count += 1
            time = Method.hdigit2min(arret.get_horaire(periode,self.numero)[count])
        return Method.hdigit2min(arret.get_horaire(periode,self.numero)[count])


    def time_between_arret(self,heure,arret1,periode):
       
        
        arret2 = arret1.get_arret_suivant(self)

        print(self.nextBus(arret1,heure,periode))

        time = self.nextBus(arret2,self.nextBus(arret1,heure,periode)+1,periode) - self.nextBus(arret1,heure,periode)
        
        return time

    def findArret(self,arret):
        res=self.ArretDepart
        try:
            while res != arret:
                res = res.get_arret_suivant(self)
            return res
        except AttributeError:
            return None

    def isInLigne(self,arret):
        try:
             ifarret = self.findArret(arret)
             return True
        except:
            return False
    