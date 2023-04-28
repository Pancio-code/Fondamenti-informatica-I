from tester import tester_fun

def A_Ex2(m):
    ris=[]
    if len(m) and len(m[0])<=2:
        return ris
    for riga in range(1,len(m)-1):
        for colonna in range(1,len(m[0])-1):
            if m[riga][colonna]<m[riga][colonna+1] and m[riga][colonna]<m[riga][colonna-1]:
                if m[riga][colonna]>m[riga+1][colonna] and m[riga][colonna]>m[riga-1][colonna]:
                    ris.append(m[riga][colonna])
            elif m[riga][colonna]>m[riga][colonna+1] and m[riga][colonna]>m[riga][colonna-1]:
                if m[riga][colonna]<m[riga+1][colonna] and m[riga][colonna]<m[riga-1][colonna]:
                    ris.append(m[riga][colonna])
    return sorted(ris)
                
            
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[3,2,1,5],[2,10,3,4],[4,5,2,4]]] ,[3])
counter_test_positivi += tester_fun(A_Ex2, [[[3, 2, 1, 5], [2, 10, 3, 4], [4, 5, 2, 4],[2, 10, 3, 4]]] ,[3,5])
counter_test_positivi += tester_fun(A_Ex2, [[[3, 2, 1, 5, 3], [2, 10, 3, 4, 2], [4, 5, 2, 4, 4],[2, 10, 3, 4, 0]]] ,[3,5])
counter_test_positivi += tester_fun(A_Ex2, [[[3, 2, 1, 5, 3], [2, 10, 3, 4, 2], [4, 5, 2, 5, 4],[2, 10, 3, 4, 0]]] ,[3,4,5])
counter_test_positivi += tester_fun(A_Ex2, [[[3, 2, 1, 5, 3], [2, 10, 3, 4, 2], [4, 5, 2, 4, 4],[2, 10, 3, 4, 0], [3, 2, 1, 5, 3]]] ,[3,3,5])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
