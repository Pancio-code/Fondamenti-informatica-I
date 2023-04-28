from tester import tester_fun

def B_Ex2(m):
    righe = len(m)
    colonne = len(m[0])
    lista = []
    for i in range(1, righe - 1):
        for j in range(1, colonne -1):
           if (m[i][j] < 0 and m[i-1][j] > 0 and m[i+1][j] > 0 and m[i][j-1]>0 and m[i][j+1]>0) or (m[i][j] > 0 and m[i-1][j] < 0 and m[i+1][j] < 0 and m[i][j-1]<0 and m[i][j+1]<0):
               lista += [m[i][j]]
    lista.sort()
    return lista
            
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[[3,2,1,5],[2,-10,3,4],[4,5,2,4]]] ,[-10])
counter_test_positivi += tester_fun(B_Ex2, [[[3, 2, -1, 5], [2, -10, 3,- 4], [4, 5, -2, 4],[2, 10, 3, 4]]] ,[-10,-2,3])
counter_test_positivi += tester_fun(B_Ex2, [[[3, 2, 1, 5, 3], [2, 10, 3, 4, 2], [4, 5, 2, 4, 4],[2, 10, 3, 4, 0]]] ,[])
counter_test_positivi += tester_fun(B_Ex2, [[[3, 2, 1, 5, 3], [2, 10, -3, 4, 2], [4, -5, 2, 5, 4],[2, 10, 3, 4, 0]]] ,[-5,-3])
counter_test_positivi += tester_fun(B_Ex2, [[[3, 2], [2, 10], [4, 5]]],[])

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
