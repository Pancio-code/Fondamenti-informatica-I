from tester import tester_fun

def A_Ex5(s1,s2):
    ris = ''
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        ris = ris + s1[i]
        i = i+1
    return ris


    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex5, ['amaca','amaranto'], 'ama')
counter_test_positivi += tester_fun(A_Ex5, ['asso','assolato'], 'asso')
counter_test_positivi += tester_fun(A_Ex5, ['','stringa'], '')
counter_test_positivi += tester_fun(A_Ex5, ['stringa',''], '')
counter_test_positivi += tester_fun(A_Ex5, ['ciao mamma','ciao '], 'ciao ')

print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
