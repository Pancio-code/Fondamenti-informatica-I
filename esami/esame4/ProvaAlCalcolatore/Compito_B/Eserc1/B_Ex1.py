from tester import tester_fun

def B_Ex1(s1,s2):
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ["mago","lago"],3)
counter_test_positivi += tester_fun(B_Ex1, ["cavallo","cavallo"],7)
counter_test_positivi += tester_fun(B_Ex1, ["acetone","acero"],2)
counter_test_positivi += tester_fun(B_Ex1, ["alba","albino"],1)
counter_test_positivi += tester_fun(B_Ex1, ["","pippo"],-5)



print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
