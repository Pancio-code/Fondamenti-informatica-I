from tester import tester_fun

def A_Ex3(l,c):
    ris = ''
    for s in l:
        if len(s) > len(ris) and s[-1] == c:
            ris = s
        elif len(s) == len(ris) and s[-1] == c and s > ris:
            ris = s
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, [["palla", "casa", "pera", "casta"], 'a'] ,"palla")
counter_test_positivi += tester_fun(A_Ex3, [["pallone", "casta", "pero", "cassa"], 'a']  ,"casta")
counter_test_positivi += tester_fun(A_Ex3, [["pallone", "cassate", "casta", "pero", "cassa"], 'e'] ,"pallone")
counter_test_positivi += tester_fun(A_Ex3, [["pallone", "cassate", "casta", "pero", "cassa","palco"],'o'] ,"palco")
counter_test_positivi += tester_fun(A_Ex3, [["pallone", "cassate", "casta", "pero", "cassa","palco"],'u'] ,'')

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

