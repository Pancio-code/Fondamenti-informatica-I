from tester import tester_fun

def A_Ex4(file,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""          

###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['voli1.csv',3],['Londra','Parigi'])
counter_test_positivi += tester_fun(A_Ex4, ['voli1.csv',5],['Parigi'])
counter_test_positivi += tester_fun(A_Ex4, ['voli2.csv',4],['Londra', 'Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(A_Ex4, ['voli2.csv',7],['Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(A_Ex4, ['voli2.csv',11],[])

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
