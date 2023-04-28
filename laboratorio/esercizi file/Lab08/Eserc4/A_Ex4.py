from tester import tester_fun

def A_Ex4(fileName):
    f=open(fileName,'r',encoding='UTF-8')
    a=[]
    a1=set()
    cont=0
    r=f.readline()
    r=f.readline().strip().split(',')
    while len(r)==3:
        if int(r[1])>=29:
            a.append(r[2].strip())
        r=f.readline().strip().split(',')
    for i in a:
        if a.count(i)>1:
            a1.add(i)
    return a1
            

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

