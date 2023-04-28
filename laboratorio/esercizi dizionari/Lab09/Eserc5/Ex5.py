from tester import tester_fun

def Ex5(file):
    s={}
    f=open(file,'r',encoding='UTF-8')
    f1=f.readline().strip().split(',')
    contatore=1
    while f1[0].isdecimal()==True:
        for i in f1:
            if int(i) not in s:
                s[int(i)]={contatore}
            else:
                ins=s.get(int(i))
                ins.add(contatore)
                s[int(i)]=ins
        contatore+=1
        f1=f.readline().strip().split(',')
    f.close()
    return s
##    f=open(file,"r",encoding="UTF-8")
##    d = {}
##    j=1
##    for riga in f:
##        lista = riga.strip().split(',')
##        for i in range(len(lista)):
##            numero = int(lista[i])
##            if numero in d:
##                d[numero].add(j)
##            else:
##                d[numero] = set()
##                d[numero].add(j)
##        j=j+1
##    f.close()
##    return d 
                
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex5, ['numeri1.txt'] , {10: {1,2}, -5: {1,2}, 0: {1}, 8: {2}, -3: {2}})
counter_test_positivi += tester_fun(Ex5, ['numeri2.txt'] , {10: {1,2}, 0: {2}})
counter_test_positivi += tester_fun(Ex5, ['numeri3.txt'] , {3: {1,2}, 4: {1}, 5: {1}, 2: {2,3}, 0: {2,3}})
counter_test_positivi += tester_fun(Ex5, ['numeri4.txt'] , {2: {1,2,3,4,5}, 1: {1,2,6}, 3: {6}})
counter_test_positivi += tester_fun(Ex5, ['numeri5.txt'] , {})

print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
