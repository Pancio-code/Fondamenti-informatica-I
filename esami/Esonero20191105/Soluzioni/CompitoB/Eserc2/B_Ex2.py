from tester import tester_fun

def B_Ex2(s):
    somma = 0
    num=''
    for c in s:
        if c!='-':
            num=num+c
        else:
            if int(num)>10:
                somma=somma+int(num)
            num=''
    if int(num)>10:
        somma=somma+int(num)
    return somma
            
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, ['2-123-45-6-78'] ,246)
counter_test_positivi += tester_fun(B_Ex2, ['7-5-10'] ,0)
counter_test_positivi += tester_fun(B_Ex2, ['90-4-90-4'] ,180)
counter_test_positivi += tester_fun(B_Ex2, ['19'] ,19)
counter_test_positivi += tester_fun(B_Ex2, ['11-2-3-11'] ,22)

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
