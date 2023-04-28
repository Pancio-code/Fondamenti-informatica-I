from tester import tester_fun

def Ex1(l,c1,c2):
    tot=0
    for elem in l:
        if elem.count(c1+c2)>0 or  elem.count(c2+c1)>0:
        #import re #versione alternativa che fa uso di espressioni regolari
        #if re.search(c1+c2+'|'+c2+c1,elem):
            tot+=1
    return tot
    
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex1, [['palla','pallone','casa','casolare'],'l','a'] , 3)
counter_test_positivi += tester_fun(Ex1, [['palla','pallone','casa','casolare'],'l','l'] , 2)
counter_test_positivi += tester_fun(Ex1, [['palla','pallone','casa','casolare'],'a','p'] , 2)
counter_test_positivi += tester_fun(Ex1, [['palla','pallone','casa','casolare'],'o','n'] , 1)
counter_test_positivi += tester_fun(Ex1, [[],'a','b'] , 0)

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
