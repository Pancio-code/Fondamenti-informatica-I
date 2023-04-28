from tester import tester_fun

# soluzione che non fa uso di strutture dati interne per rappresentare matrici

def Ex3(file):
    fin=open(file,encoding='UTF-8')
    indiceRiga=0
    fin.readline()
    numeroMaxNegativi=0
    indice=0
    for riga in fin:
        contaNeg=0
        riga=riga.strip().split()
        for elem in riga:
            if int(elem)<0:
                contaNeg+=1
        if contaNeg >= numeroMaxNegativi:
            numeroMaxNegativi=contaNeg
            indiceRiga=indice
        indice+=1
    return indiceRiga

# soluzione che usa le matrici rappresentate come liste di liste

def Ex3(file):
    fin=open(file,encoding='UTF-8')
    dim=fin.readline().strip().split()
    righe=int(dim[0])
    colonne=int(dim[1])
    mat=[]
    for riga in fin:
        riga=riga.strip().split()
        for i in range(len(riga)): # trasforma in interi
            riga[i]=int(riga[i])
        mat.append(riga)
    numeroMaxNegativi=0
    indiceRiga=0
    for i in range(righe):
        contaNeg=0
        for j in range(colonne):
            if mat[i][j]<0:
                contaNeg+=1
        if contaNeg >= numeroMaxNegativi:
            numeroMaxNegativi=contaNeg
            indiceRiga=i
    return indiceRiga

# soluzione che usa le matrici rappresentate in numpy

import numpy as np

def Ex3(file):
    fin=open(file,encoding='UTF-8')
    dim=fin.readline().strip().split()
    righe=int(dim[0])
    colonne=int(dim[1])
    mat=np.zeros((righe,colonne),dtype=int)
    for i in range(righe):
        r=fin.readline().strip().split()
        for j in range(colonne):
            mat[i,j]=int(r[j])
    numeroMaxNegativi=0
    indiceRiga=0
    matb=mat<0 # genera una matrice di valori booleani, dove True indica che
               # il valore originario in mat è minore di zero
    for i in range(righe):
        contaNeg=list(matb[i]).count(True) #conta quante volte True compare in
                                           #matb[i] (necessita di una trasformazione in lista)
        if contaNeg >= numeroMaxNegativi:
            numeroMaxNegativi=contaNeg
            indiceRiga=i
    return indiceRiga

 
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
