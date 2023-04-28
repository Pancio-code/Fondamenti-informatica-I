from tester import tester_fun

def A_Ex4(fileName):
    f=open(fileName, "r", encoding="UTF-8")
    f.readline()
    r1=set() #insieme con materie per le quali c'è almeno un 29
    r2=set()
    for riga in f:
        l=riga.strip().split(",")
        materia = l[2].strip() # elimino eventuali spazi prima e dopo la materia
        voto=int(l[1])
        if voto>=29:
            if materia in r1:
                r2.add(materia)
            else:
                r1.add(materia)
    f.close()
    return r2 

###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ["esami1.csv"], {'Fisica'})
counter_test_positivi += tester_fun(A_Ex4, ["esami2.csv"], set())
counter_test_positivi += tester_fun(A_Ex4, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
counter_test_positivi += tester_fun(A_Ex4, ["esami4.csv"], {'Basi di Dati'})
counter_test_positivi += tester_fun(A_Ex4, ["esami5.csv"], set())


print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

