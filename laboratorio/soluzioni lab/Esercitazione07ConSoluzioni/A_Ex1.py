from tester import tester_fun

def A_Ex1(s):
    maxDistanza=0
    for i in range(len(s)-1):
        d=s.rfind(s[i])-i
        if d>maxDistanza:
            maxDistanza=d
    return maxDistanza


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["agfhjskieaha"] , 11)
counter_test_positivi += tester_fun(A_Ex1, ["abcd"] , 0)
counter_test_positivi += tester_fun(A_Ex1, ["casale"] , 2)
counter_test_positivi += tester_fun(A_Ex1, ["abaco"] , 2)
counter_test_positivi += tester_fun(A_Ex1, ["alle"] , 1)


print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
