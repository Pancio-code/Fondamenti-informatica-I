from tester import tester_fun

def A_Ex2(m,s):
    for r in range(len(m)):
        cont=''
        for c in range(len(m[0])):
            cont+=m[r][c]
        if s in cont:
            return True
    for c1 in range(len(m[0])):
        cont=''
        for r1 in range(len(m)):
            cont+=m[r1][c1]
        if s in cont:
            return True
    return False
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'amo'],True)
counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'aria'],True)
counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'aia'],True)
counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'amore'],False)
counter_test_positivi += tester_fun(A_Ex2, [[['a']],'c'],False)

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
