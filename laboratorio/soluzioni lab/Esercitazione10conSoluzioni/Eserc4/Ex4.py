from tester import tester_fun

def Ex4(file):
    f = open(file,'r',encoding='utf-8')
    d = {}
    f.readline() #legge la prima riga
    
    for relazione in f:
        riga = relazione.strip().split(',')
        nome1 = riga[0].strip()
        if nome1 not in d:
            d[nome1] = []
        nome2 = riga[1].strip()
        if nome2 not in d:
            d[nome2] = []
        rel = riga[2].strip()
        if rel == 'amici':
            if nome1 not in d[nome2]:
                d[nome2].append(nome1)
                d[nome2].sort()
            if nome2 not in d[nome1]:
                d[nome1].append(nome2)
                d[nome1].sort()
        else:
            if nome1 in d[nome2]:
                d[nome2].remove(nome1)
            if nome2 in d[nome1]:
                d[nome1].remove(nome2)
    return d   
 
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
