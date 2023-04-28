from tester import tester_fun

def E_Ex3(s1,s2,n):
    ris=[]
    for c in s1:
        if c in s2 and (s1.count(c) + s2.count(c)) <= n and c not in ris:
            ris.append(c)
    ris.sort()
    return ris


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(E_Ex3, ["casa bella","casa al mare",2],['c', 'e', 's'])
counter_test_positivi += tester_fun(E_Ex3, ["sara osso rotto","asar ooss",1],[])
counter_test_positivi += tester_fun(E_Ex3, ["sara","rasata",2],['r', 's'])
counter_test_positivi += tester_fun(E_Ex3, ["a","ba",2],["a"])
counter_test_positivi += tester_fun(E_Ex3, ["a","A",2],[])

print('La funzione',E_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

