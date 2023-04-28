from tester import tester_fun

def D_Ex1(s):
        if len(s) == 0:
                return 0
        minimo=s.count(s[0])
        for c in s:
                if s.count(c)<minimo:
                        minimo=s.count(c)
        return minimo
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex1, ['&&a&aa^h^hh&'], 2)
counter_test_positivi += tester_fun(D_Ex1, [''], 0)
counter_test_positivi += tester_fun(D_Ex1, ['hhhh'], 4)
counter_test_positivi += tester_fun(D_Ex1, ['string'], 1)
counter_test_positivi += tester_fun(D_Ex1, ['ciaio'], 1)

print('La funzione',D_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
