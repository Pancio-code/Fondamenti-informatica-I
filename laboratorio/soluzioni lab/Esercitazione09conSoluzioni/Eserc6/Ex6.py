from tester import tester_fun

def Ex6(file):
    f = open(file,'r',encoding='UTF-8')
    d = {}
    f.readline()
    for partita in f:
        ris = partita.strip().split(',')
        s1 = ris[0].strip()
        s2 = ris[1].strip()
        if s1 not in d:
            d[s1]=[]
        if s2 not in d:
            d[s2]=[]
        gol1 = int(ris[2])
        gol2 = int(ris[3])
        b=False
        if gol1 > gol2:
            team1=s1
            team2=s2
            b=True
        elif gol1 < gol2:
            team1=s2
            team2=s1
            b=True
        if b==True:
            if team1 not in d[team2]:
                d[team1].append(team2)
            else:
                d[team2].remove(team1)
    f.close()
    return d
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex6, ["partite1.csv"] , {'Chelsea': [], 'Everton': ['Tottenham'], 'Arsenal': ['Chelsea'], 'Tottenham': []})
counter_test_positivi += tester_fun(Ex6, ["partite2.csv"] , {'Chelsea': ['Everton'], 'Everton': ['Tottenham', 'Arsenal'], 'Arsenal': ['Chelsea'], 'Tottenham': []})
counter_test_positivi += tester_fun(Ex6, ["partite3.csv"] , {'Bayern': ['Schalke'], 'Schalke': ['Stoccarda'], 'Amburgo': ['Werder'], 'Werder': [], 'Stoccarda': [], 'Colonia': ['Stoccarda']})
counter_test_positivi += tester_fun(Ex6, ["partite4.csv"] , {'Bayern': ['Schalke', 'Schalke'], 'Schalke': ['Stoccarda', 'Stoccarda'], 'Amburgo': ['Werder', 'Werder'], 'Werder': [], 'Stoccarda': [], 'Colonia': ['Stoccarda', 'Stoccarda']})
counter_test_positivi += tester_fun(Ex6, ["partite5.csv"] , {'Bayern': [], 'Schalke': [], 'Amburgo': [], 'Werder': [], 'Stoccarda': [], 'Colonia': []})

print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
