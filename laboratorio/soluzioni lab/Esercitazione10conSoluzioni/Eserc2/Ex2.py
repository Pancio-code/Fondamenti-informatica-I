from tester import tester_fun
import re

def Ex2(file):
    f=open(file,"r",encoding="UTF-8")
    regex = '[a-z]*([a-z])\\1[a-z]*[^a-z]+[a-z]*\\1\\1[a-z]*[^a-z]+[a-z]*\\1\\1[a-z]*'
    i = 0
    for riga in f:
        it = re.finditer(regex,riga,re.IGNORECASE)
        for m in it:
            i += 1
    return i
   
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2, ["file1.txt"] , 1)
counter_test_positivi += tester_fun(Ex2, ["file2.txt"] , 2)
counter_test_positivi += tester_fun(Ex2, ["file3.txt"] , 3)
counter_test_positivi += tester_fun(Ex2, ["IMalavogliaNoAccenti.txt"] , 18)
counter_test_positivi += tester_fun(Ex2, ["IMalavogliaNoAccenti_50.txt"] , 1)


print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
