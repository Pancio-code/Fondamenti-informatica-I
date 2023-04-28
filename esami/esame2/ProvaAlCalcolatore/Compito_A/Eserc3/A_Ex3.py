from tester import tester_fun

def A_Ex3(file):
    f=open(file,'r',encoding='UTF-8')
    cont=0
    diz={}
    for r in f:
        max=0
        cont+=1
        pulita=r.strip()
        parz=[]
        for lett in pulita:
            if lett in 'AEIOUaeiou ':
                continue
            if pulita.count(lett)>max:
                parz=[lett]
                max=pulita.count(lett)
                continue
            elif lett not in parz and pulita.count(lett)==max:
                parz.append(lett)
        for l in parz:
            lista=diz.get(l,[])
            if lista==[]:
                diz[l]=[cont]
            else:
                lista.append(cont)
                diz[l]=lista
    return diz
                
            
                          
###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['file1.txt'],{'c': [1], 'z': [1], 'n': [2, 3]}  )
counter_test_positivi += tester_fun(A_Ex3, ['file2.txt'],{'c': [1, 5], 'z': [1], 'n': [2, 5], 't': [3, 6], 'l': [4], 's': [4], 'r': [5], 'v': [5], 'd': [5]} )
counter_test_positivi += tester_fun(A_Ex3, ['file3.txt'], {'n': [1], 'l': [2], 't': [3]})
counter_test_positivi += tester_fun(A_Ex3, ['file4.txt'],{'n': [1, 4, 5], 'l': [2, 5, 6], 't': [3], 'p': [5], 'z': [6]} )
counter_test_positivi += tester_fun(A_Ex3, ['file5.txt'],{'n': [1, 4, 5], 'l': [2, 5, 6, 8, 9], 't': [3, 7], 'p': [5], 'z': [6]})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
