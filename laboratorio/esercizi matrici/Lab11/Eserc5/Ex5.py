from tester import tester_fun

def Ex5(file):
    f=open(file,'r')
    mat1=[]
    cont=0
    for riga in f:
        cont+=1
        pulita=riga.strip()
        mat=[]
        for elem in pulita:
            if elem in mat:
                return False
            else:
                mat.append(elem)
        mat1.append(mat)
    if len(mat1)!=len(mat1[0]):
        return False
    for l in range(len(mat1[0])):
        mat3=[]
        for i in range(len(mat1)):
            if mat1[i][l] in mat3:
                return False
            else:
                mat3.append(mat1[i][l])
        print(mat3)   
    f.close()
    return True

##def Ex5(file):
##    # soluzione con liste di liste
##    f = open(file,'r',encoding = 'UTF-8')
##    riga = f.readline().strip()
##    dim = len(riga) #calcola numero elementi prima riga
##    simboli = [] #lista dei simboli usati nella prima riga
##    for elem in riga:
##        if elem not in simboli:
##            simboli.append(elem)
##        else:
##            return False
##    m = [list(riga)] #crea la matrice, inizializza con prima riga
##    numRighe = 1
##    for riga in f:
##        if len(riga.strip()) != dim: # Check matrice quadrata
##            return False
##        m.append(list(riga.strip()))
##        numRighe += 1
##    f.close()
##    if numRighe != dim:
##        return False
##    # verifica per righe
##    for i in range(1,len(m)):
##        elementi_riga = []
##        for elem in m[i]:
##            if elem not in elementi_riga and elem in simboli:
##                elementi_riga.append(elem)
##            else:
##                return False
##        
##    # verifica per colonne
##    for j in range(0,len(m)):
##        colonna = [m[i][j] for i in range(len(m))]
##        elementi_colonna = []
##        for elem in colonna:
##            if elem not in elementi_colonna and elem in simboli:
##                elementi_colonna.append(elem)
##            else:
##                return False
##            
##    return True  
    
    
            
    
 
    
        
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex5, ['file1.txt'] , True)
counter_test_positivi += tester_fun(Ex5, ['file2.txt'] , False)
counter_test_positivi += tester_fun(Ex5, ['file3.txt'] , False)
counter_test_positivi += tester_fun(Ex5, ['file4.txt'] , False)
counter_test_positivi += tester_fun(Ex5, ['file5.txt'] , False)

print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
