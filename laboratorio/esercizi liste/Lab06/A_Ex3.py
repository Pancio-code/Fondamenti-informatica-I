from tester import tester_fun

def A_Ex3(l,n):
    l1=''
    for i in range(len(l)):
        if n>=len(l[i]):
            l1=l1+'!'
        else:
            s1=l[i]
            l1=l1+s1[n]
    return l1
            




###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo'], 3], 't!!t!d')
counter_test_positivi += tester_fun(A_Ex3, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo', 'che', 'ci', 'lascia', 'lo', 'zampino'], 4], 'o!!a!o!!i!i')
counter_test_positivi += tester_fun(A_Ex3, [['nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita', 'mi', 'ritrovai'], 6], '!!!!!!!!a')
counter_test_positivi += tester_fun(A_Ex3, [['nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita', 'mi', 'ritrovai'], 0], 'nmdcdnvmr')
counter_test_positivi += tester_fun(A_Ex3, [[], 0],'')

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
