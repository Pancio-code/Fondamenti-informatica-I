from tester import tester_fun

def D_Ex2(m):
    righe=len(m)
    colonne=len(m[0])
    simm=True
    tot=-1
    for r in range(righe):
        for c in range(colonne):
            if r!=c and m[r][c]!=m[c][r]:
                simm=False
    if simm==False:
        return tot
    tot=0
    for r in range(righe):
        for c in range(colonne):
            if r!=c and m[r][c]>0:
                tot+=m[r][c]
    return tot
    
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(D_Ex2, [[[0,-1,3],[-1,5,5],[3,5,0]]] , 16)
counter_test_positivi += tester_fun(D_Ex2, [[[0,-1,3],[-1,5,5],[3,-5,0]]] , -1)
counter_test_positivi += tester_fun(D_Ex2, [[[0,-1,3,3],[-1,5,5,2],[3,5,0,1],[3,5,0,1]]] , -1)
counter_test_positivi += tester_fun(D_Ex2, [[[1,1],[1,1]]] , 2)
counter_test_positivi += tester_fun(D_Ex2, [[[1]]] , 0)

print('La funzione',D_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
