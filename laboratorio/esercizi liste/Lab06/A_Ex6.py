from tester import tester_fun

def A_Ex6(l):
        l1=[]
        for i in range(len(l)):
                s1=l[i]
                s=0
                for c in range(len(s1)):
                         k=ord(s1[c])
                         s=s+k
                l1.append(s)
        return l1
    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex6, [["ama","ma","amaca"]], [303,206,499])
counter_test_positivi += tester_fun(A_Ex6, [[]], [])
counter_test_positivi += tester_fun(A_Ex6, [["c"]], [99])
counter_test_positivi += tester_fun(A_Ex6, [["ciao",""]], [412,0])
counter_test_positivi += tester_fun(A_Ex6, [["",""]], [0,0])

print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
