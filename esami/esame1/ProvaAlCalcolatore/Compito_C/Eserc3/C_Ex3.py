from tester import tester_fun

def C_Ex3(l1,l2):
    i=0
    ris=[]
    for p in l1:
        lista=[]
        cont=0
        for l in p:
            if l in l2[i] and l not in lista:
                cont+=1
                lista.append(l)
        ris.append(p)
        ris.append(cont)
        i+=1
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex3, [["mamma", "asso", "re", "pluto"],["mare", "lago", "fante", "barba"]] ,["mamma", 2, "asso", 2, "re", 1, "pluto", 0])
counter_test_positivi += tester_fun(C_Ex3, [["","aaa"],["regina","fante"]] ,["",0,"aaa",1])
counter_test_positivi += tester_fun(C_Ex3, [["re","regina","cavallo"],["re","cavallo","regina"]] ,["re",2,"regina",1,"cavallo",1])
counter_test_positivi += tester_fun(C_Ex3, [["","aaa"],["","aaa"]] ,["",0,"aaa",1])
counter_test_positivi += tester_fun(C_Ex3, [["Marea"],["marea"]],["Marea",3])

print('La funzione',C_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

