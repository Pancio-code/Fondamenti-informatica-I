from tester import tester_fun

def A_Ex7(l):
    s=[]
    for i in l:
        for c in i:
            s.append(c)
    f=0
    s1=[]
    for f in s:
        if s.count(f)==1:
            s1.append(f)
                
    return set(s1)
        
        
    

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
