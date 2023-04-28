from tester import tester_fun
import re

def Ex2(file):
    testo=open(file,"r",encoding="UTF-8").read()
    regex = r'[a-z]*([a-z])[a-z]*([a-z])[a-z]*[^a-z][a-z]*\2[a-z]*\1[a-z]*[^a-z]'
    ris = re.findall(regex,testo,re.IGNORECASE)
    return len(ris)

 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2, ["file1.txt"] , 2)
counter_test_positivi += tester_fun(Ex2, ["file2.txt"] , 3)
counter_test_positivi += tester_fun(Ex2, ["file3.txt"] , 4)
counter_test_positivi += tester_fun(Ex2, ["file4.txt"] , 3)
counter_test_positivi += tester_fun(Ex2, ["file5.txt"] , 4)


print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
