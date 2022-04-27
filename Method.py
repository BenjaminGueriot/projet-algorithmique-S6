from datetime import datetime,weekday

lst_date_holidays = [1019,1104,1221,1231,101,106,222,309,418,504,704,901]
                    #Vacances toussaint, noel partie decembre,noel partie janvier, hiver , printemps,Ete

#Fonction ayant une date en argument et retourne un booleen qui indique si la date est un jour de vacances ou non
def is_holiday(date):
    j = 0
    for i in range(0,len(lst_date_holidays)):
        if date > lst_date_holidays[j] and date < lst_date_holidays[j+1]:
            return True
        if j+2 != len(lst_date_holidays):
            j += 2

    date2 = datetime.today()

    if (date2.weekend() == True):
        return True
    
    return False

def hdigit2min(heure):
    if len(heure) == 5:
        heurefin = heure[0] + heure[1]
        minfin = heure[3:]
    else:
        heurefin = heure[0]
        minfin = heure[2:]
    return 60*int(heurefin) + int(minfin)

def min2hdigit(minutes):
    heure = int(minutes/60)
    minutes = minutes%60
    if minutes < 10:
        return str(heure) + ":0" + str(minutes)
    else:
        return str(heure) + ":" + str(minutes)

def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z