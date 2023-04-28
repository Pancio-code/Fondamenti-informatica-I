from tester import tester_fun

def A_Ex1(l1, l2):
    ris=[]
    for i in range(len(l1)):
        ris.append(l1[i]+l2[i])
    if len(l1)<len(l2):
        for i in range(len(l1),len(l2)):
            ris.append(l2[i])
    return ris



###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 6

counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4,9]] , [6, 10, 9])
counter_test_positivi += tester_fun(A_Ex1, [[],[3,4,9]] , [3, 4, 9])
counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4]] ,[6, 10])
counter_test_positivi += tester_fun(A_Ex1, [[1],[9]] ,[10])
counter_test_positivi += tester_fun(A_Ex1, [[],[9]] ,[9])
counter_test_positivi += tester_fun(A_Ex1, [[],[]] ,[])

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)