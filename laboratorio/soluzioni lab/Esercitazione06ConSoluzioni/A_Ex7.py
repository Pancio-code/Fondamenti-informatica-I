from tester import tester_fun

def A_Ex7(a, b):
    c=set()
    for e in a:
        if e not in b:
            c.add(e)
    return c



###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 6

counter_test_positivi += tester_fun(A_Ex7, [{1, 'a', 2}, set()], {1, 'a', 2})
counter_test_positivi += tester_fun(A_Ex7, [{1, 'a', 2}, {1, 'a', 2}], set())
counter_test_positivi += tester_fun(A_Ex7, [{1, 'a', 2}, {2}], {1, 'a'})
counter_test_positivi += tester_fun(A_Ex7, [set(), set()], set())
counter_test_positivi += tester_fun(A_Ex7, [set(), {1,'c'}], set())
counter_test_positivi += tester_fun(A_Ex7, [{1, 'a', 2}, {1, 2}], {'a'})

print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
