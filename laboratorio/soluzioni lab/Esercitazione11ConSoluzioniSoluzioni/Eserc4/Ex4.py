from tester import tester_fun

def Ex4(file):
    f = open(file,'r',encoding='utf-8')
    d = {}
    f.readline() #legge la prima riga
    for prestito in f:
        lista = prestito.strip().split(',')
        oggetto = lista[0].strip()
        personaDa = lista[1].strip()
        personaA = lista[2].strip()
        if oggetto not in d:
            d[oggetto] = [personaDa,personaA]
        elif d[oggetto][1] == personaDa:
            d[oggetto][1] = personaA
    return d 
    
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex4, ["eredita1.csv"] , {'Anello_di_smeraldi': ['Maria', 'Giorgia'], 'Signore_Degli_Anelli': ['Silvia', 'Paolo']})
counter_test_positivi += tester_fun(Ex4, ["eredita2.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio']})
counter_test_positivi += tester_fun(Ex4, ["eredita3.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Anna', 'Sergio']})
counter_test_positivi += tester_fun(Ex4, ["eredita4.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Giorgio'], 'Vaso': ['Anna', 'Anna']})
counter_test_positivi += tester_fun(Ex4, ["eredita5.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Sergio', 'Anna']})

print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
