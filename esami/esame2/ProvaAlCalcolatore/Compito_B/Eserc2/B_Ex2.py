from tester import tester_fun

def B_Ex2(m):
    tot=0
    for r in range(len(m)):
        parz1=0
        for c in range(len(m[0])):
            parz1+=m[r][c]
        for c1 in range(len(m[0])):
            parz=0
            for r1 in range(len(m)):
                parz+=m[r1][c1]
            if parz==parz1:
                tot+=1
    return tot
            
            

###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,3,4,2],[1,7,3,3]]] ,2)
counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,3,4,2],[1,7,3,3],[10,0,0,5]]] ,4)
counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,5,4,2],[1,7,3,3]]] ,0)
counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,3,4,2],[1,7,5,3],[8,0,0,5]]] ,4)
counter_test_positivi += tester_fun(B_Ex2, [[[1,1,1],[1,1,1],[1,1,1]]] ,9)

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
