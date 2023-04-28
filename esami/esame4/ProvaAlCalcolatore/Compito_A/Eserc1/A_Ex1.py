from tester import tester_fun

def A_Ex1(s1,s2):
    ds=0
    cont=0
    if len(s1)==len(s2):
        i=0
        for l in s1:
            if s2[i]!=l:
                cont+=1
            i+=1
        ds=cont
    if len(s1)>len(s2):
        i=0
        for l in s2:
            if s1[i]!=l:
                cont+=1
            i+=1
        ds=cont+(len(s1)-len(s2))
    if len(s1)<len(s2):
        i=0
        for l in s1:
            if s2[i]!=l:
                cont+=1
            i+=1
        ds=cont+(len(s2)-len(s1))
    return ds
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["aceto","aceto"],0)
counter_test_positivi += tester_fun(A_Ex1, ["pippo","pappa"],2)
counter_test_positivi += tester_fun(A_Ex1, ["aceto","ace"],2)
counter_test_positivi += tester_fun(A_Ex1, ["alba","albino"],3)
counter_test_positivi += tester_fun(A_Ex1, ["","pippo"],5)


print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
