from tester import tester_fun

def Ex3(file):
    f=open(file,'r',encoding='UTF-8')
    prima=f.readline().strip().split()
    num=0
    totale=0
    if len(prima)<1:
        return 'errore'
    righe=int(prima[0])
    colonne=int(prima[1])
    mat=[[0 for i in range(colonne)]for l in range(righe)]
    for riga in range(righe):
        line=f.readline().strip().split()
        cont=0
        for colonna in range(colonne):
            mat[riga][colonna]=line[cont]
            cont+=1
    for riga in range(righe):
        parz=0
        for colonna in range(colonne):
            if int(mat[riga][colonna])<0:
                parz+=1
        if parz>=totale:
            totale=parz
            indice=num
        num+=1
    return indice
            
        
            

 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, ["matrice1.txt"] , 3)
counter_test_positivi += tester_fun(Ex3, ["matrice2.txt"] , 0)
counter_test_positivi += tester_fun(Ex3, ["matrice3.txt"] , 1)
counter_test_positivi += tester_fun(Ex3, ["matrice4.txt"] , 3)
counter_test_positivi += tester_fun(Ex3, ["matrice5.txt"] , 4)

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
