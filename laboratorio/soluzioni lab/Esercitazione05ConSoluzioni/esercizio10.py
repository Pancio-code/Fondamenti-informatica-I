#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione che prende in ingresso una stringa s
ed un intero n e verifica se nella stringa
compaiono 2 lettere uguali a distanza esattamente n.
"""

from tester import tester_fun

def funzione7(s,n):
    for i in range(len(s)-n):
        if s[i]==s[i+n]:
            return True
    return False 
    



###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 3

counter_test_positivi += tester_fun(funzione7, ['casa',2] , True)
counter_test_positivi += tester_fun(funzione7, ['cassa',1] , True)
counter_test_positivi += tester_fun(funzione7, ['ornato',5] , True)

print('La funzione',funzione7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
