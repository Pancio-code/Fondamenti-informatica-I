from tester import tester_fun
import re

def Ex1(file):
        f=open(file,'r',encoding='UTF-8')
        testo=f.read().strip()
        pattern=r'([^a-z]|^)([a-z])[a-z]*([a-z])[a-z]*([a-z])[^a-z]+\2[a-z]*\3[a-z]*\4([^a-z]|$)'
        giusto=re.findall(pattern,testo,re.IGNORECASE)
        f.close()
        return len(giusto)


 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 6

counter_test_positivi += tester_fun(Ex1, ["file1.txt"] , 1)
counter_test_positivi += tester_fun(Ex1, ["file2.txt"] , 2)
counter_test_positivi += tester_fun(Ex1, ["file3.txt"] , 3)
counter_test_positivi += tester_fun(Ex1, ["file4.txt"] , 2)
counter_test_positivi += tester_fun(Ex1, ["IMalavogliaNoAccenti.txt"] , 394)
counter_test_positivi += tester_fun(Ex1, ["IMalavogliaNoAccenti_50.txt"] , 15)

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
