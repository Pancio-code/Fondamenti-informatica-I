from tester import tester_fun

def B_Ex1(l):
    lista=set()
    for p in range(len(l)):
        if (p+2)%2==0:
            for lett in range(1,len(l[p]),2):
                lista.add(l[p][lett])
        else:
            for lett in range(0,len(l[p]),2):
                lista.add(l[p][lett])
    return sorted(list(lista))
            
        

###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, [["mamma","sole","casa"]],['a', 'l', 'm', 's'])
counter_test_positivi += tester_fun(B_Ex1, [["mamma","sole","casa","sacco"]],['a', 'c', 'l', 'm', 'o', 's'])
counter_test_positivi += tester_fun(B_Ex1, [["pippo","castello","se"]],['c', 'e', 'i', 'l', 'p', 's'])
counter_test_positivi += tester_fun(B_Ex1, [[]],[])
counter_test_positivi += tester_fun(B_Ex1, [["assolo",""]],['o', 's'])


print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
