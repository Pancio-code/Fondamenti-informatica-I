from tester import tester_fun

def B_Ex2(m,s):
    dp=''
    ds=''
    i=1
    for r in range(len(m)):
        for c in range(len(m[0])):
            if r==c:
                dp=dp+m[r][c]
            if c==(len(m[0])-i):
                ds=ds+m[r][c]
        i+=1
    print(ds,dp)
    if s in ds or s in dp:
        return True
    return False

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[['a','m','o','r'],['r','i','o','y'],['i','s','a','x'],['a','s','t','a']],'rosa'],True)
counter_test_positivi += tester_fun(B_Ex2, [[['a','m','o','r'],['r','i','o','y'],['i','s','a','x'],['a','s','t','a']],'aia'],True)
counter_test_positivi += tester_fun(B_Ex2, [[['a','m','o','r'],['r','i','o','y'],['i','s','a','x'],['a','s','t','a']],'rosato'],False)
counter_test_positivi += tester_fun(B_Ex2, [[['a','m'],['a','m']],'ma'],True)
counter_test_positivi += tester_fun(B_Ex2, [[['a']],'b'],False)


print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
