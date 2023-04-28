from tester import tester_fun
from numpy import *

def Ex6(file):
    f = open(file, 'r', encoding = 'UTF-8')
    m = [] 
    righe = 9
    colonne = 9
    for i in range(righe):
        riga = f.readline().split() # leggo una riga
        for j in range(colonne):
            riga[j] = int(riga[j])  # converto le stringhe in numeri
        m.append(riga)            # inserisco la riga nella matrice
    
#    stampa matrice input
    for elem in m:
        print(elem)
    
    # verifica per righe
    for i in range(1,len(m)):
        elementi_riga = []
        for elem in m[i]:
            if elem not in elementi_riga:
                elementi_riga.append(elem)
            else:
                return False
        
    # verifica per colonne
    for j in range(0,len(m)):
        colonna = [m[i][j] for i in range(len(m))]
        elementi_colonna = []
        for elem in colonna:
            if elem not in elementi_colonna:
                elementi_colonna.append(elem)
            else:
                return False
    
    # verifica sottogriglia
    for bigI in range(3):
        for bigJ in range(3):
            elementi_sottogriglia = []
            for i in range(3):
                for j in range(3):
                    elem = m[i+bigI*3][j+bigJ*3]
                    if elem not in elementi_sottogriglia:
                        elementi_sottogriglia.append(elem)
                    else:
                        return False           
            
    return True         
##    #Soluzione con l'utilizzo di Numpy
##    data=loadtxt(file, dtype=str) #crea la matrice da file
##    symbols=['1','2','3','4','5','6','7','8','9']
##    for riga in data:
##        diff=set(symbols)-set(riga)
##        if len(diff)!=0:
##            return False
##    for colonna in data.T:
##        diff=set(symbols)-set(colonna)
##        if len(diff)!=0:
##            return False
##    for i in range(0,9,3):
##        for j in range(0,9,3):
##            diff=set(symbols)-set(data[i:i+3,j:j+3].flatten())
##            if len(diff)!=0:
##                return False
##    return True
        
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 3

counter_test_positivi += tester_fun(Ex6, ['sudoku1.txt'] , False)
counter_test_positivi += tester_fun(Ex6, ['sudoku3.txt'], True)
counter_test_positivi += tester_fun(Ex6, ['sudoku4.txt'], False)

print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
