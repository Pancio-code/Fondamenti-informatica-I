from tester import tester_fun

def F_Ex2(s):
    con=0
    for i in range(len(s)):
        if i==0 and s[i]=='b':
            con=con+1
        elif i!=0 and s[i]=='b':
            if s[i-1]!='b':
                con=con+1
    return s.count('b')-con 

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(F_Ex2, ['acbbdebbbfbho'],3)
counter_test_positivi += tester_fun(F_Ex2, ['b'],0)
counter_test_positivi += tester_fun(F_Ex2, [''],0)
counter_test_positivi += tester_fun(F_Ex2, ['cdbbfgbbr'],2)
counter_test_positivi += tester_fun(F_Ex2, ['fabbricabile'],1)

print('La funzione',F_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


