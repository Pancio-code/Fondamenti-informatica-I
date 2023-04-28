from tester import tester_fun

def A_Ex2(start,n):
    somma=0
    for i in range(start,2*n):
        print(i)
        if i%2!=0:
            somma=somma+i
        print(somma)
    return somma



counter_test_positivi = 0
total_tests = 9

counter_test_positivi += tester_fun(A_Ex2, [4,3], 21)
counter_test_positivi += tester_fun(A_Ex2, [4,1], 5)
counter_test_positivi += tester_fun(A_Ex2, [4,4], 32)
counter_test_positivi += tester_fun(A_Ex2, [4,0], 0)
counter_test_positivi += tester_fun(A_Ex2, [5,5], 45)
counter_test_positivi += tester_fun(A_Ex2, [7,3], 27)
counter_test_positivi += tester_fun(A_Ex2, [5,7], 67)
counter_test_positivi += tester_fun(A_Ex2, [20,3], 69)
counter_test_positivi += tester_fun(A_Ex2, [70,3], 219)

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

