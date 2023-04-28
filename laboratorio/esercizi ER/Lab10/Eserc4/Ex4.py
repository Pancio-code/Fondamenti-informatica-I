from tester import tester_fun

def Ex4(file):
    f=open(file,'r',encoding='UTF-8')
    f.readline()
    diz={}
    for riga in f:
        nuova=riga.strip().split(',')
        valore=[]
        valore1=[]
        if nuova[2]=='amici':
            valore.extend(diz.get(nuova[0],[nuova[1]]))
            valore1.extend(diz.get(nuova[1],[nuova[0]]))
            if nuova[1] not in valore:
                valore.extend([nuova[1]])
            if nuova[0] not in valore1:
                valore1.extend([nuova[0]])
            valore.sort()
            valore1.sort()
            diz[nuova[0]]=valore
            diz[nuova[1]]=valore1
        else:
            vl=diz.get(nuova[0],[])
            vl1=diz.get(nuova[1],[])
            if nuova[0] in vl1:
                vl1.remove(nuova[0])
                diz[nuova[1]]=vl1
            if nuova[1] in vl:
                vl.remove(nuova[1])
                diz[nuova[0]]=vl
    f.close()
    return diz
                
                
            
            
        
    
    
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex4, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
counter_test_positivi += tester_fun(Ex4, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
counter_test_positivi += tester_fun(Ex4, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
counter_test_positivi += tester_fun(Ex4, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
counter_test_positivi += tester_fun(Ex4, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
