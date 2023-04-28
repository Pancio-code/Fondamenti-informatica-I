from tester import tester_fun

def A_Ex3(l):
    s=set()
    for i in l:
        for l in i:
            if i.count(l)>1:
                s.add(l)
    return s
    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, [['casa', 'albero', 'bello']] , {'a','l'})
counter_test_positivi += tester_fun(A_Ex3, [['ciao', 'ciao']] , set())
counter_test_positivi += tester_fun(A_Ex3, [['aa','aa','hghjklhl']] , {'a','h','l'})
counter_test_positivi += tester_fun(A_Ex3, [[]] , set())
counter_test_positivi += tester_fun(A_Ex3, [['cogito', 'ergo', 'sum']] , {'o'})


print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
