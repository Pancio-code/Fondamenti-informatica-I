from tester import tester_fun

def B_Ex3(l,c):
    '''Inserisci qui la tua soluzione'''

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, [["palla", "casa", "pera", "casta"], 'p'] ,"palla")
counter_test_positivi += tester_fun(B_Ex3, [["palla", "casta", "pera", "cassa"], 'c']  ,"cassa")
counter_test_positivi += tester_fun(B_Ex3, [["palla", "cassata", "casta", "pera", "cassa"], 'c'] ,"cassata")
counter_test_positivi += tester_fun(B_Ex3, [["palla", "cassata", "casta", "pera", "cassa","palco"],'p'] ,"palco")
counter_test_positivi += tester_fun(B_Ex3, [["palla", "cassata", "casta", "pera", "cassa"],'z'] ,'')

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

