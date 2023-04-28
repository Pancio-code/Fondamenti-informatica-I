from tester import tester_fun

def B_Ex1(s, n):
        count=0
        for c in s:
                if ord(c) % n != 0:
                        count=count+1
        return count
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ['ha^h', 2], 1)
counter_test_positivi += tester_fun(B_Ex1, ['', 3], 0)
counter_test_positivi += tester_fun(B_Ex1, ['hhhh', 2], 0)
counter_test_positivi += tester_fun(B_Ex1, ['string', 3], 4)
counter_test_positivi += tester_fun(B_Ex1, ['ciao', 1], 0)

print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
