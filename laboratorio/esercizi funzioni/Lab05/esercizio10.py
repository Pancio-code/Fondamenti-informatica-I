#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione che prende in ingresso una stringa s
ed un intero n e verifica se nella stringa
compaiono 2 lettere uguali a distanza esattamente n.
"""

from tester import tester_fun

def funzione7(s,n):
    c=n
    t=False
    if s!='':
        for i in range(len(s)):
            if c<len(s):
                if s[i]==s[c]:
                    t=True
                    break
            c=c+1
    return t
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    



###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 3

counter_test_positivi += tester_fun(funzione7, ['casa',2] , True)
counter_test_positivi += tester_fun(funzione7, ['cassa',1] , True)
counter_test_positivi += tester_fun(funzione7, ['ornato',5] , True)

print('La funzione',funzione7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
