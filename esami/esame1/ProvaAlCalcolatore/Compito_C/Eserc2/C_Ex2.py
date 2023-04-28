from tester import tester_fun

def C_Ex2(m):
    tot=0
    for r in range(len(m)):
        for c in range(len(m[0])):
            if r!=c and m[r][c]!=0:
                return -1
            else:
                tot+=m[r][c]
    return tot
            
 
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0],[0,5,0],[0,0,1]]],6)
counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0],[1,5,0],[0,0,1]]],-1)
counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0,0],[0,5,0,0],[0,0,1,0],[0,0,0,2]]],8)
counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0,0],[0,5,0,0],[0,0,1,0],[0,0,1,2]]],-1)
counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0,0],[0,2,0,0],[0,0,-2,0],[0,0,0,-1]]],-1)

print('La funzione',C_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

