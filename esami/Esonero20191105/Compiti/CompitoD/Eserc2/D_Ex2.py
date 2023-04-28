from tester import tester_fun

def D_Ex2(b1,b2):
    '''Inserisci qui la tua soluzione'''

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(D_Ex2, ['100','0011'],'1011')
counter_test_positivi += tester_fun(D_Ex2, ['101','',],'101')
counter_test_positivi += tester_fun(D_Ex2, ['111','00'],'111')
counter_test_positivi += tester_fun(D_Ex2, ['','1010'],'1010')
counter_test_positivi += tester_fun(D_Ex2, ['1','0'],'1')

print('La funzione',D_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
