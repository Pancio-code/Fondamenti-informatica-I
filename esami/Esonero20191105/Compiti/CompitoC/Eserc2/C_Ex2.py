from tester import tester_fun

def C_Ex2(b1,b2):
    '''Inserisci qui la tua soluzione'''

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex2, ['1011','100'],'1000')
counter_test_positivi += tester_fun(C_Ex2, ['','111'],'000')
counter_test_positivi += tester_fun(C_Ex2, ['1','1'],'1')
counter_test_positivi += tester_fun(C_Ex2, ['111','10'],'100')
counter_test_positivi += tester_fun(C_Ex2, ['1010',''],'0000')

print('La funzione',C_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


