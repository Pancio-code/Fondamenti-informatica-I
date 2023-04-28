from tester import tester_fun

def F_Ex3(l1,l2,n):
    ris=[]
    for c in l1:
        if c in l2 and l1.count(c) + l2.count(c) >= n and c not in ris:
            ris.append(c)
    ris.sort()
    return ris


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(F_Ex3, ["casa bella","casa al mare",3],[' ', 'a', 'l'])
counter_test_positivi += tester_fun(F_Ex3, ["sara osso","asar ooss",3],['a', 'o', 's'])
counter_test_positivi += tester_fun(F_Ex3, ["sara","rasa",2],['a', 'r', 's'])
counter_test_positivi += tester_fun(F_Ex3, ["a","a",2],["a"])
counter_test_positivi += tester_fun(F_Ex3, ["a","A",2],[])

print('La funzione',F_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

