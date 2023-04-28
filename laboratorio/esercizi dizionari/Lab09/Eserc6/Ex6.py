from tester import tester_fun

def Ex6(file):
    s={}
    f=open(file,'r',encoding='UTF-8')
    f.readline()
    f1=f.readline().split(',')
    while len(f1)==4:
        if int(f1[2])>int(f1[3]):
            if f1[0] not in s:
                s[f1[0]]=[f1[1]]
            else:
                a=s.get(f1[0])
                a.append(f1[1])
                s[f1[0]]=a
        if int(f1[2])<int(f1[3]):
            if f1[1] not in s:
                s[f1[1]]=[f1[0]]
            else:
                a=s.get(f1[1])
                a.append(f1[0])
                s[f1[1]]=a
        f1=f.readline().split(',')
    f.close()
    i=0
    while i<len(s):
        battute=list(s.keys())
        squadre=s.get(battute[i])
        l=0
        while l<len(squadre):
            avversari=s.get(squadre[l],[])
            attuale=squadre[l]
            if battute[i] in avversari:
                squadre.remove(squadre[l])
                avversari.remove(battute[i])
                s[battute[i]]=squadre
                s[attuale]=avversari
            else:
                l+=1
                if avversari==[]:
                    s[attuale]=[]
        i+=1
    return s

##    f = open(file,'r',encoding='UTF-8')
##    d = {}
##    f.readline()
##    for partita in f:
##        ris = partita.strip().split(',')
##        s1 = ris[0].strip()
##        s2 = ris[1].strip()
##        if s1 not in d:
##            d[s1]=[]
##        if s2 not in d:
##            d[s2]=[]
##        gol1 = int(ris[2])
##        gol2 = int(ris[3])
##        b=False
##        if gol1 > gol2:
##            team1=s1
##            team2=s2
##            b=True
##        elif gol1 < gol2:
##            team1=s2
##            team2=s1
##            b=True
##        if b==True:
##            if team1 not in d[team2]:
##                d[team1].append(team2)
##            else:
##                d[team2].remove(team1)
##    f.close()
##    return d
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
