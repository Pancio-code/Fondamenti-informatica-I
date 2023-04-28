from tester import tester_fun

def A_Ex1(s, n):
        count=0
        for c in s:
                if ord(c) % n == 0:
                        count=count+1
        return count
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ['ha^h', 2], 3)
counter_test_positivi += tester_fun(A_Ex1, ['', 3], 0)
counter_test_positivi += tester_fun(A_Ex1, ['hhhh', 2], 4)
counter_test_positivi += tester_fun(A_Ex1, ['string', 3], 2)
counter_test_positivi += tester_fun(A_Ex1, ['ciao', 1], 4)

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
