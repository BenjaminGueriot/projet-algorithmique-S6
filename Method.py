
lst_date_holidays = [1019,1104,1221,1231,101,106,222,309,418,504,704,901]
                    #Vacances toussaint, noel partie decembre,noel partie janvier, hiver , printemps,Ete

#Fonction ayant une date en argument et retourne un booleen qui indique si la date est un jour de vacances ou non
def is_holiday(date):
    j = 0
    for i in range(0,len(lst_date_holidays)):
        if date > lst_date_holidays[j] and date < lst_date_holidays[j+1]:
            print(lst_date_holidays[j])
            print(lst_date_holidays[j+1])
            return True
        if j+2 != len(lst_date_holidays):
            j += 2
    
    return False

def hdigit2min(heure):
    if len(heure) == 5:
        heurefin = heure[0] + heure[1]
        minfin = heure[3:]
    else:
        heurefin = heure[0]
        minfin = heure[2:]
    
    return int(60*int(heurefin) + int(minfin))

def shortest_path(dic_routes):
    for e in dic_routes.keys():
        dic_routes.get(e)