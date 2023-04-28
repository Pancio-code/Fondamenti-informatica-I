from tester import tester_fun

def Ex4(file):
    f=open(file,"r",encoding="UTF-8")
    d = {}
    for riga in f:
        lista = riga.strip().split(',')
        for i in range(4):
            giocatore = lista[i].strip().split(' ')
            nome = giocatore[0].strip()
            vincita = int(giocatore[1])
            if nome in d:
                d[nome][0] += 1
                d[nome][1] += vincita
            else:
                d[nome] = [1, vincita] 
    f.close()
    return d

 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex4, ['partite1.csv'] , {'Paolo': [2, 15], 'Mario': [1, -5], 'Anna': [2, 3], 'Giorgio': [1, 0], 'Stefano': [1, -10], 'Paola': [1, -3]})
counter_test_positivi += tester_fun(Ex4, ['partite2.csv'] , {'Paolo': [4, 20], 'Mario': [2, 0], 'Anna': [4, 16], 'Giorgio': [3, -8], 'Stefano': [2, -20], 'Paola': [1, -3]})
counter_test_positivi += tester_fun(Ex4, ['partite3.csv'] , {'Paolo': [4, 20], 'Mario': [4, 16], 'Anna': [4, -20], 'Giorgio': [4, -11]})
counter_test_positivi += tester_fun(Ex4, ['partite4.csv'] , {'Paolo': [4, 20], 'Mario': [4, 16], 'Anna': [4, -20], 'Giorgio': [4, -11], 'Fabio': [1, 10], 'Carlo': [1, 10], 'Maria': [1, -12], 'Simona': [1, -8]})
counter_test_positivi += tester_fun(Ex4, ['partite5.csv'] , {})

print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
