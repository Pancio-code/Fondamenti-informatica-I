from tester import tester_fun

def A_Ex3(file):
    f=open(file,'r',encoding='UTF-8')
    diz={}
    for r in f:
        r1=r.strip().split(',')
        for p in r1:
            if p not in diz:
                diz[p]=1
            else:
                diz[p]+=1
        
            

                          
###############################################################################


"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['file1.txt'],'albero')
counter_test_positivi += tester_fun(A_Ex3, ['file2.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex3, ['file3.txt'],'casolare')
counter_test_positivi += tester_fun(A_Ex3, ['file4.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex3, ['file5.txt'],'')

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
