#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione booleana che prende come parametro una
stringa e restituisce True se nella
stringa c’è almeno un carattere che compare
più di una volta, False altrimenti.
"""

from tester import tester_fun

def funzione1(s):
    for c in s:
        if s.count(c)>1:
            return True
    return False



###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(funzione1, ['casa'] ,True)
counter_test_positivi += tester_fun(funzione1, ['tre'] ,False)
counter_test_positivi += tester_fun(funzione1, [''] ,False)
counter_test_positivi += tester_fun(funzione1, ['  '] ,True)
counter_test_positivi += tester_fun(funzione1, ['pallonata'] ,True)

print('La funzione',funzione1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
