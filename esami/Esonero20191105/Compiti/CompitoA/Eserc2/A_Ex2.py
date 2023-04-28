from tester import tester_fun

def A_Ex2(s):
    '''Inserisci qui la tua soluzione'''
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, ['12-123-45-6-78'] ,123)
counter_test_positivi += tester_fun(A_Ex2, ['11-12-12'] ,12)
counter_test_positivi += tester_fun(A_Ex2, ['80-40-80-40'] ,80)
counter_test_positivi += tester_fun(A_Ex2, ['10'] ,10)
counter_test_positivi += tester_fun(A_Ex2, ['1-2-3-4-5'] ,5)

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
