from tester import tester_fun

def D_Ex2(b1,b2):
    L=min(len(b1),len(b2))
    ris=''
    for i in range(L):
        ris=ris+str(int(b1[i]) or int(b2[i]))
    if len(b1)>len(b2):
        ris=ris+b1[len(b2):len(b1)]
    elif len(b2)>len(b1):
        ris=ris+b2[len(b1):len(b2)]
    return ris
###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(D_Ex2, ['100','0011'],'1011')
counter_test_positivi += tester_fun(D_Ex2, ['101','',],'101')
counter_test_positivi += tester_fun(D_Ex2, ['111','00'],'111')
counter_test_positivi += tester_fun(D_Ex2, ['','1010'],'1010')
counter_test_positivi += tester_fun(D_Ex2, ['1','0'],'1')

print('La funzione',D_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
