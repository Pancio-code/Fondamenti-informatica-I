from tester import tester_fun

def F_Ex1(s1, s2):
        count=0
        minimo=min(len(s1),len(s2))
        for i in range(minimo):
                if s1[i]!=s2[i]:
                        count=count+1
        return count+max(len(s1),len(s2))-minimo
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(F_Ex1, ['ha^h', 'hb^hlp1e'], 5)
counter_test_positivi += tester_fun(F_Ex1, ['', ''], 0)
counter_test_positivi += tester_fun(F_Ex1, ['hb^hlp1', 'ha^h'], 4)
counter_test_positivi += tester_fun(F_Ex1, ['stri&ng', 'stri&ng'], 0)
counter_test_positivi += tester_fun(F_Ex1, ['ciaom', 'oaiclp'], 6)

print('La funzione',F_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
