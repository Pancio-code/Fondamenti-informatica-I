from tester import tester_fun

def E_Ex2(s,c):
    con=0
    for i in range(len(s)):
        if i==0 and s[i]==c:
            con=con+1
        elif i!=0 and s[i]==c:
            if s[i-1]!=c:
                con=con+1
    return con   
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(E_Ex2, ['bcaadeaaafaho','a'] , 3)
counter_test_positivi += tester_fun(E_Ex2, ['cdeefgr','e'] , 1)
counter_test_positivi += tester_fun(E_Ex2, ['e','e'] , 1)
counter_test_positivi += tester_fun(E_Ex2, ['pippo','e'] , 0)
counter_test_positivi += tester_fun(E_Ex2, ['','a'] , 0)

print('La funzione',E_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
