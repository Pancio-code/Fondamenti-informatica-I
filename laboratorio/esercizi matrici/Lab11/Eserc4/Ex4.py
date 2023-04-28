from tester import tester_fun

def Ex4(file):
    f=open(file)
    f.readline()
    diz={}
    for riga in f:
        p=riga.strip().split(',')
        antenato=p[1].strip()
        erede=p[2].strip()
        prop=p[0].strip()
        if prop not in diz:
            diz[prop] = [antenato,erede]
        elif diz[prop][1] == antenato:
            diz[prop][1] = erede  
    f.close()
    return diz
    
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex4, ["eredita1.csv"] , {'bracelet': ['Maria', 'Giorgia'], 'book': ['Silvia', 'Paolo']})
counter_test_positivi += tester_fun(Ex4, ["eredita2.csv"] , {'bracelet': ['Marco', 'Giorgio'], 'ring': ['Silvia', 'Sergio']})
counter_test_positivi += tester_fun(Ex4, ["eredita3.csv"] , {'bracelet': ['Marco', 'Giorgio'], 'ring': ['Silvia', 'Sergio'], 'vase': ['Anna', 'Sergio']})
counter_test_positivi += tester_fun(Ex4, ["eredita4.csv"] , {'bracelet': ['Marco', 'Giorgio'], 'ring': ['Silvia', 'Giorgio'], 'vase': ['Anna', 'Anna']})
counter_test_positivi += tester_fun(Ex4, ["eredita5.csv"] , {'bracelet': ['Marco', 'Giorgio'], 'ring': ['Silvia', 'Sergio'], 'vase': ['Sergio', 'Anna']})

print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
