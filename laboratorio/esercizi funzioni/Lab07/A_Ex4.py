from tester import tester_fun

def A_Ex4(l):
    s=[]
    for i in l:
        for f in range(len(l)):
            if len(i)==len(l[f]) and i!=l[f]:
                c=(i,l[f])
                s.append(c)
    return s
                
    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, [['jkl', 'h', 'plqa', 'a', 'xkj']] , [('jkl','xkj'), ('h','a'), ('a','h'), ('xkj','jkl')])
counter_test_positivi += tester_fun(A_Ex4, [[]] , [])
counter_test_positivi += tester_fun(A_Ex4, [['a', 'ab', 'abc']] , [])
counter_test_positivi += tester_fun(A_Ex4, [['e', 'a', 'lp', 'ql', 'cl']] ,  [('e', 'a'), ('a', 'e'), ('lp', 'ql'), ('lp', 'cl'), ('ql', 'lp'), ('ql', 'cl'), ('cl', 'lp'), ('cl', 'ql')])
counter_test_positivi += tester_fun(A_Ex4, [['hjkl', 'hjkp']] , [('hjkl', 'hjkp'), ('hjkp', 'hjkl')] )


print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
