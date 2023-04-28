from tester import tester_fun

def A_Ex5(s1,s2):                           #CON IL CICLO WHILE
    s=''                                    #i=0
    for i in range(min(len(s1),len(s2))):   #while i < len(s1) and i <len(s2) and s1[i]==s2[i]:
        if s1[i]!=s2[i]:                    #s=s+s1[i]
             break                          #i=i-1
        s=s+s1[i]
    return s

    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 6

counter_test_positivi += tester_fun(A_Ex5, ['amaca','amaranto'], 'ama')
counter_test_positivi += tester_fun(A_Ex5, ['asso','assolato'], 'asso')
counter_test_positivi += tester_fun(A_Ex5, ['','stringa'], '')
counter_test_positivi += tester_fun(A_Ex5, ['stringa',''], '')
counter_test_positivi += tester_fun(A_Ex5, ['ciao mamma','ciao '], 'ciao ')
counter_test_positivi += tester_fun(A_Ex5, ['ciao mamma','bar '], '')

print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
