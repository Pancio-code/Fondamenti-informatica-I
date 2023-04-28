from tester import tester_fun

def A_Ex1(l):
    ris=[]
    for i in range(len(l)):
        parola=l[i]
        if (i+2)%2==0:
            for lett in range(0,len(parola),2):
                ris.append(parola[lett])
        else:
            for lett in range(1,len(parola),2):
                ris.append(parola[lett])
    return sorted(list(set(ris)))
            

###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, [["mamma","sola","casa"]],["a", "c", "m", "o", "s"])
counter_test_positivi += tester_fun(A_Ex1, [["mamma","sole","casa","sacco"]],["a", "c", "e", "m", "o", "s"])
counter_test_positivi += tester_fun(A_Ex1, [["pippo","castello","se"]],["a","l","o","p","s","t"])
counter_test_positivi += tester_fun(A_Ex1, [[]],[])
counter_test_positivi += tester_fun(A_Ex1, [["assolo",""]],["a","l","s"])


print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
