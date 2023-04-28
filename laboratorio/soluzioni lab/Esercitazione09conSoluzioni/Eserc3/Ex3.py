from tester import tester_fun

def Ex3(file):
    f = open(file,'r',encoding='utf-8')
    d = {}
    f.readline()
    for partita in f:
        ris = partita.strip().split(',')
        team1 = ris[0].strip()
        team2 = ris[1].strip()
        gol1 = int(ris[2])
        gol2 = int(ris[3])
        if gol1 > gol2:
            d[team1] = d.get(team1,0) + 3
            d[team2] = d.get(team2,0) + 0
        elif gol1 == gol2:
            d[team1] = d.get(team1,0) + 1
            d[team2] = d.get(team2,0) + 1
        else:
            d[team2] = d.get(team2,0) + 3
            d[team1] = d.get(team1,0) + 0
    f.close()
    return d
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, ["partite1.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})
counter_test_positivi += tester_fun(Ex3, ["partite2.csv"] , {'Chelsea': 4, 'Everton': 6, 'Arsenal': 4, 'Tottenham': 2})
counter_test_positivi += tester_fun(Ex3, ["partite3.csv"] , {'Bayern': 4, 'Schalke': 3, 'Amburgo': 4, 'Werder': 1, 'Colonia': 4, 'Stoccarda': 0})
counter_test_positivi += tester_fun(Ex3, ["partite4.csv"] , {'Bayern': 8, 'Schalke': 6, 'Amburgo': 8, 'Werder': 2, 'Colonia': 8, 'Stoccarda': 0})
counter_test_positivi += tester_fun(Ex3, ["partite5.csv"] , {'Bayern': 5, 'Schalke': 6, 'Amburgo': 5, 'Werder': 5, 'Colonia': 5, 'Stoccarda': 6})

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
