from tester import tester_fun

def C_Ex1(s):
        massimo=0
        for c in s:
                count=s.count(c)
                if c.isalpha() and c.isupper() and count > massimo:
                        massimo=count
        return massimo
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex1, ['aHa^^&^HH'], 3)
counter_test_positivi += tester_fun(C_Ex1, [''], 0)
counter_test_positivi += tester_fun(C_Ex1, ['&&YH&Y'], 2)
counter_test_positivi += tester_fun(C_Ex1, ['stri%$p'], 0)
counter_test_positivi += tester_fun(C_Ex1, ['CIAO'], 1)

print('La funzione',C_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
