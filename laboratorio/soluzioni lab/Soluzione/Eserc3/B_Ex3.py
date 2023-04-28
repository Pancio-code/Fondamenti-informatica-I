from tester import tester_fun
import re

def B_Ex3(file):
    lista=[]
    f=open(file,'r',encoding='UTF-8')
    for r in f:
        r1=r.strip()
        pattern=r'\b[A-Za-z][a-z]*([A-Z])[a-z]*[A-Za-z]\b'
        m=re.finditer(pattern,r1)
        if m:
            for i in m:
                lista.append(i.group(1))
    f.close()
    return sorted(list(set(lista)))
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""Dati di test forniti in aula"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['testo1.txt'] ,['M'])
counter_test_positivi += tester_fun(B_Ex3, ['testo2.txt'] ,['L', 'M'])
counter_test_positivi += tester_fun(B_Ex3, ['testo3.txt'] ,['A', 'L', 'M', 'S'])
counter_test_positivi += tester_fun(B_Ex3, ['testo4.txt'] ,['A', 'E', 'U'])
counter_test_positivi += tester_fun(B_Ex3, ['testo5.txt'] ,['N', 'P', 'R', 'T'])

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

"""Dati di test NASCOSTI"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['testo6.txt'] ,['A', 'M'])
counter_test_positivi += tester_fun(B_Ex3, ['testo7.txt'] ,['I', 'L', 'M', 'R'])
counter_test_positivi += tester_fun(B_Ex3, ['testo8.txt'] ,['A', 'L', 'M', 'O', 'S'])
counter_test_positivi += tester_fun(B_Ex3, ['testo9.txt'] ,['A', 'E', 'M', 'O', 'U'])
counter_test_positivi += tester_fun(B_Ex3, ['testo10.txt'] ,['N', 'P', 'R', 'T'])

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
