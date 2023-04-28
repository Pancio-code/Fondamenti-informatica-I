#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione che prende in ingresso due stringhe
della stessa lunghezza e restituisce la
stringa composta dai caratteri alternati delle due stringhe
"""

from tester import tester_fun

def funzione2(s1,s2):
    t=''
    for i in range(len(s1)):
        t=t+s1[i]+s2[i]
    return t
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
    
    
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 4

counter_test_positivi += tester_fun(funzione2, ['casa','mora'] ,'cmaosraa')
counter_test_positivi += tester_fun(funzione2, ['il','la'] ,'illa')
counter_test_positivi += tester_fun(funzione2, ['a','a'] ,'aa')
counter_test_positivi += tester_fun(funzione2, ['',''] ,'')

print('La funzione',funzione2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
