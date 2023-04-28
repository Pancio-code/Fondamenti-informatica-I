#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione che prende in input una stringa s
e restituisce il carattere che compare più
spesso. Se più caratteri compaiono lo stesso numero di
volte deve restituire il primo carattere in ordine.
"""

from tester import tester_fun

def funzione3(s):
    if s!='':
        c=0
        t=s[c]
        for i in range(1,len(s)):
            if s.count(s[i])>s.count(s[c]):
                t=s[i]
                c=c+1
    else:
        t=''
    return t



"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
    
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(funzione3, ['partecipazione'] ,'p')
counter_test_positivi += tester_fun(funzione3, ['cassetto'] ,'s')
counter_test_positivi += tester_fun(funzione3, ['pari'] ,'p')
counter_test_positivi += tester_fun(funzione3, ['a'] ,'a')
counter_test_positivi += tester_fun(funzione3, [''] ,'')

print('La funzione',funzione3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
