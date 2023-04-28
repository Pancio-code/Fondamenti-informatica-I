from tester import tester_fun

def A_Ex3(fileName):
    f1=open(fileName,'r',encoding='UTF-8')
    r=f1.readline()
    s=[]
    r=f1.readline().strip().split(',')
    while len(r)==3:
        if int(r[1])>=18:
            l=(r[0].strip(),r[2].strip())
            s.append(l)
        r=f1.readline().strip().split(',')
    f1.close()
    return s
            
        
        

###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], [('1345','Fisica'),('1346','Analisi'),('1896','Geometria'),('1753','Fisica')])
counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], [('1346','Analisi')])
counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], [])
counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], [])
counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], [('1345','Fisica'),('1987','Fondamenti'),('1346','Analisi'),('1896','Geometria')])


print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
