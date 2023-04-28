from tester import tester_fun

def A_Ex5(l):
    r=[]
    for elem1 in l:
        cont=0
        for elem2 in l:
            if len(elem1)==len(elem2):
                cont=cont+1
        r.append((elem1,cont))
    return r

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex5, [['jkl', 'h', 'plqa', 'a', 'xkj']] , [('jkl', 2), ('h', 2), ('plqa', 1), ('a', 2), ('xkj', 2)] )
counter_test_positivi += tester_fun(A_Ex5, [[]] , [])
counter_test_positivi += tester_fun(A_Ex5, [['a', 'ab', 'abc']] , [('a', 1), ('ab', 1), ('abc', 1)])
counter_test_positivi += tester_fun(A_Ex5, [['e', 'a', 'lp', 'ql', 'cl']] ,  [('e', 2), ('a', 2), ('lp', 3), ('ql', 3), ('cl', 3)] )
counter_test_positivi += tester_fun(A_Ex5, [['hjkl', 'hjkp']] , [('hjkl', 2), ('hjkp', 2)])


print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
