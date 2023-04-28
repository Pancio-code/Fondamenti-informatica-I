from tester import tester_fun
import re

def Ex3(file):
    testo=open(file,"r",encoding="UTF-8").read()
    regex = '([^a-z]|^)([a-z])[a-z]*([a-z])\\3[a-z]*\\2([^a-z]|$)'
    # il primo gruppo serve solo per esprimere l'opzionalità
    # fra inizio file e inizio parola non all'inizio del file
    # il secondo gruppo ha un funzionamenoto analogo rispetto alla
    # fine del file
    ris = re.findall(regex,testo,re.IGNORECASE)
    print(ris)
    return len(ris)

 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, ["file1.txt"] , 3)
counter_test_positivi += tester_fun(Ex3, ["file2.txt"] , 3)
counter_test_positivi += tester_fun(Ex3, ["file3.txt"] , 2)
counter_test_positivi += tester_fun(Ex3, ["file4.txt"] , 2)
counter_test_positivi += tester_fun(Ex3, ["file5.txt"] , 3)

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
