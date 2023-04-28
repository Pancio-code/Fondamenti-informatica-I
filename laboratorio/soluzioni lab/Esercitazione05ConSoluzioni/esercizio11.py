#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione che prende in ingresso una stringa s e calcola la più lunga distanza tra 2
caratteri uguali. Se nessun carattere si ripete allora il risultato deve essere 0. Ad esempio, se s=
‘agfhjskieaha’ la più lunga distanza è tra la prima e l’ultima ‘a’ ed è 11 (la prima volta è in posizione
0 e l’ultima in posizione 11). Consiglio, usate la funzione rfind
"""

from tester import tester_fun

def funzione8(s):
    maxDistanza=0
    for i in range(len(s)-1):
        d=s.rfind(s[i])-i
        if d>maxDistanza:
            maxDistanza=d
    return maxDistanza


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(funzione8, ["agfhjskieaha"] , 11)
counter_test_positivi += tester_fun(funzione8, ["abcd"] , 0)
counter_test_positivi += tester_fun(funzione8, ["casale"] , 2)
counter_test_positivi += tester_fun(funzione8, ["abaco"] , 2)
counter_test_positivi += tester_fun(funzione8, ["alle"] , 1)


print('La funzione',funzione8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
