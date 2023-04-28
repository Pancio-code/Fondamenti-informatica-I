from tester import tester_fun

def Ex6(file):
    f=open(file,'r')
    mat1=[]
    cont=0
    for riga in f:
        cont+=1
        pulita=riga.strip().split()
        mat=[]
        for elem in pulita:
            if elem in mat:
                return False
            else:
                mat.append(elem)
        mat1.append(mat)
    if len(mat1)!=9 and len(mat1[0])!= 9:
        return False
    for l in range(len(mat1[0])):
        mat3=[]
        for i in range(len(mat1)):
            if mat1[i][l] in mat3:
                return False
            else:
                mat3.append(mat1[i][l])
    # verifica sottogriglia
    for bigI in range(3):
        for bigJ in range(3):
            elementi_sottogriglia = []
            for i in range(3):
                for j in range(3):
                    elem = mat1[i+bigI*3][j+bigJ*3]
                    if elem not in elementi_sottogriglia:
                        elementi_sottogriglia.append(elem)
                    else:
                        return False
    
            
        
    f.close()
    return True
     
    
        
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 3

counter_test_positivi += tester_fun(Ex6, ['sudoku1.txt'], False)
counter_test_positivi += tester_fun(Ex6, ['sudoku3.txt'], True)
counter_test_positivi += tester_fun(Ex6, ['sudoku4.txt'], False)

print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
