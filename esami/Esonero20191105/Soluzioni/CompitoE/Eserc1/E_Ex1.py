from tester import tester_fun

def E_Ex1(s1, s2):
        count=0
        for i in range(min(len(s1),len(s2))):
                if s1[i]==s2[i] and s1[i].isalpha():
                        count=count+1
        return count
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(E_Ex1, ['ha^h', 'hb^hlp1'], 2)
counter_test_positivi += tester_fun(E_Ex1, ['', ''], 0)
counter_test_positivi += tester_fun(E_Ex1, ['hb^hlp1', 'ha^h'], 2)
counter_test_positivi += tester_fun(E_Ex1, ['stri&ng', 'stri&ng'], 6)
counter_test_positivi += tester_fun(E_Ex1, ['ciaom', 'oaiclp'], 0)

print('La funzione',E_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
