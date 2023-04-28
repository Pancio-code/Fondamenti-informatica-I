from tester import tester_fun

def Ex1(l):
    s={}
    for elem in l:
      s[elem] = s.get(elem,0) + 1
    return s
    
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex1, [['casa','orso','cane','casa','orso','casa']] , {'casa': 3, 'orso': 2, 'cane': 1})
counter_test_positivi += tester_fun(Ex1, [['casa','casa','casa']] , {'casa': 3})
counter_test_positivi += tester_fun(Ex1, [['casa','orso','cane','cassa','osso','casta']] , {'casa': 1, 'orso': 1, 'cane': 1, 'cassa': 1, 'osso': 1, 'casta': 1})
counter_test_positivi += tester_fun(Ex1, [['casa']] , {'casa': 1})
counter_test_positivi += tester_fun(Ex1, [[]] , {})

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
