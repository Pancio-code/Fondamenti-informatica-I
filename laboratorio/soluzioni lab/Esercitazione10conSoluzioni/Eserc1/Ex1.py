from tester import tester_fun
import re

def Ex1(file):
    testo=open(file,"r",encoding="UTF-8").read()
    regex = r'([^a-z]|^)([a-z])[a-z]*([a-z])[a-z]*([a-z])[^a-z]+\2[a-z]*\3[a-z]*\4([^a-z]|$)'
    ris = re.finditer(regex,testo,re.IGNORECASE)
    i = 0
    for m in ris:
        i += 1
    return i

## Python ammette in verità anche l'uso nelle espressioni regolari della
## sequenza speciale \b, che collima con la stringa vuota, ma solo se
## questa si trova all'inizio o alla fine di una parola (cioè di una
## sequenza di caratteri alfanumerici, quelli che collimano con \w -
## incluso l'underscore). In altri termini, \b indica il "confine" (boundary)
## di una parola, che tecnicamente è quello che si trova fra un carattere \w
## ed un carattere \W (o vice-versa) o fra \w e l'inizio/fine della stringa
##
## Nella funzione precedente quindi possiamo anche usare la seguente espressione regolare
##
## regex = r'\b([a-z])[a-z]*([a-z])[a-z]*([a-z])[^a-z]+\1[a-z]*\2[a-z]*\3\b'
##
## notate che in questo modo siamo in grado anche di catturare due sequenze che rispettano la regola
## indicata nell'esercizio anche se sono separate da un solo carattere non alfabetico.

 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 6

counter_test_positivi += tester_fun(Ex1, ["file1.txt"] , 2)
##counter_test_positivi += tester_fun(Ex1, ["file2.txt"] , 2)
##counter_test_positivi += tester_fun(Ex1, ["file3.txt"] , 3)
##counter_test_positivi += tester_fun(Ex1, ["file4.txt"] , 2)
##counter_test_positivi += tester_fun(Ex1, ["IMalavogliaNoAccenti.txt"] , 394)
##counter_test_positivi += tester_fun(Ex1, ["IMalavogliaNoAccenti_50.txt"] , 15)

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
