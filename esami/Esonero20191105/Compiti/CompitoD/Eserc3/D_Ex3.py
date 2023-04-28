from tester import tester_fun

def D_Ex3(l):
    '''Inserisci qui la tua soluzione'''
    
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex3, [[5,7,6,8,4,9]] ,7)
counter_test_positivi += tester_fun(D_Ex3, [[5,7,7,8,8,4,9,0,0]] ,9)
counter_test_positivi += tester_fun(D_Ex3, [[5,3,7,7,8,4,9,0,1]] ,8)
counter_test_positivi += tester_fun(D_Ex3, [[5,2]] ,100)
counter_test_positivi += tester_fun(D_Ex3, [[7,8,9,10]],100)

print('La funzione',D_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

