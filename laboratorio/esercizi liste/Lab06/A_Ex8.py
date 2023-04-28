from tester import tester_fun

def A_Ex8(s):
        l=[]
        for i in range(len(s)):
                if s[i].isalpha()==True and s[i].isupper()==True:
                        l.append(s[i])
        return set(l)
                        
	



###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 6

counter_test_positivi += tester_fun(A_Ex8, ['3219'], set())
counter_test_positivi += tester_fun(A_Ex8, ['aG2Hl'], {'G', 'H'})
counter_test_positivi += tester_fun(A_Ex8, ['&/&90'], set())
counter_test_positivi += tester_fun(A_Ex8, [''], set())
counter_test_positivi += tester_fun(A_Ex8, ['ABN'], {'A', 'B', 'N'})
counter_test_positivi += tester_fun(A_Ex8, ['KKK&%LL'], {'K', 'L'})

print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
