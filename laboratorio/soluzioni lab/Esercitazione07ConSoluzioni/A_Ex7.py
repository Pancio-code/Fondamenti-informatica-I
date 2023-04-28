from tester import tester_fun

def A_Ex7(l):
    r=set()
    for i in l:
        for elem in i:
            prendo=True
            for i2 in l:
                if i2!=i and elem in i2:
                    prendo=False
            if prendo:
                r.add(elem)
    return r

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex7, [[{3,2,90},{2,87,23},{2,23,3}]] , {90,87})
counter_test_positivi += tester_fun(A_Ex7, [[set(),{-10},{2}]] , {-10,2})
counter_test_positivi += tester_fun(A_Ex7, [[set()]] , set())
counter_test_positivi += tester_fun(A_Ex7, [[set(),{10,-2},{10},{-2}]] , set())
counter_test_positivi += tester_fun(A_Ex7, [[set(),{10,-9,4},{4,-5,2},{3,7,4}]] , {10,-9,-5,2,3,7})


print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
