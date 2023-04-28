from tester import tester_fun

def C_Ex1(s):
        '''Inserisci qui la tua soluzione'''
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex1, ['aHa^^&^HH'], 3)
counter_test_positivi += tester_fun(C_Ex1, [''], 0)
counter_test_positivi += tester_fun(C_Ex1, ['&&YH&Y'], 2)
counter_test_positivi += tester_fun(C_Ex1, ['stri%$p'], 0)
counter_test_positivi += tester_fun(C_Ex1, ['CIAO'], 1)

print('La funzione',C_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
