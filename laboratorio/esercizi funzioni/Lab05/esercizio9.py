#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione booleana che prende come parametro una stringa
contenente almeno due caratteri e restituisce True se i caratteri
sono tutti in ordine crescente, False altrimenti.
"""

from tester import tester_fun

def funzione6(s):
    c=0
    for i in range(1,len(s)):
        t=True
        if s[i]<s[c]:
            t=False
            break
        c=c+1
    return t
        
            
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""



    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 3

counter_test_positivi += tester_fun(funzione6, ['abcd'] , True)
counter_test_positivi += tester_fun(funzione6, ['casale'] , False)
counter_test_positivi += tester_fun(funzione6, ['abaco'] , False)

print('La funzione',funzione6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
