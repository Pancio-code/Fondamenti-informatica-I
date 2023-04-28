from tester import tester_fun

def A_Ex3(file,n):
    f=open(file,'r',encoding='UTF-8')
    cont=0
    diz={}
    for r in f:
        parz=[]
        cont+=1
        ins=set()
        r1=r.strip().lower()
        for l in r1:
            if r1.count(l)>=n and l.isalpha()==True:
                parz.append(l)
        for i in sorted(list(set(parz))):
            if i not in diz:
                diz[i]=[cont]
            else:
                diz[i].append(cont)
    return diz
                
                
                          
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['file1.txt',3],{'a': [1, 2, 3], 'i': [1, 2, 3], 'e': [2], 'n': [2, 3], 'o': [2, 3], 's': [2]})
counter_test_positivi += tester_fun(A_Ex3, ['file2.txt',3],{'a': [1, 2, 3, 4, 5, 6], 'i': [1, 2, 3, 4, 6], 'e': [2, 4, 6], 'n': [2, 3], 'o': [2, 3, 4, 6], 's': [2, 4], 't': [3, 6], 'd': [4], 'l': [4], 'p': [6], 'v': [6]})
counter_test_positivi += tester_fun(A_Ex3, ['file3.txt',2],{'a': [1, 2, 3], 'c': [1, 2, 3], 'd': [1, 2, 3], 'e': [1, 2, 3], 'i': [1, 2, 3], 'n': [1, 2, 3], 'o': [1, 2, 3], 'p': [1, 2, 3], 'r': [1, 2, 3], 's': [1, 2, 3], 't': [1, 2, 3], 'v': [1, 3], 'z': [1], 'g': [2], 'l': [2, 3], 'm': [2], 'u': [3]})
counter_test_positivi += tester_fun(A_Ex3, ['file4.txt',4],{'a': [1, 2, 3, 4, 5, 6], 'c': [1], 'e': [1, 2, 3], 'i': [1, 2, 3, 4, 5, 6], 'n': [1, 2, 3, 4], 'o': [1, 2, 3, 4, 6], 's': [1, 2], 'd': [2, 3], 'l': [2, 6], 't': [2, 3, 4], 'p': [3], 'r': [3], 'v': [3], 'z': [6]})
counter_test_positivi += tester_fun(A_Ex3, ['file5.txt',4],{'a': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'c': [1, 7], 'e': [1, 2, 3, 7, 9], 'i': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'n': [1, 2, 3, 4, 7, 8], 'o': [1, 2, 3, 4, 6, 7, 8, 9], 's': [1, 2, 7], 'd': [2, 3, 7], 'l': [2, 6, 7, 8, 9], 't': [2, 3, 4, 7], 'p': [3, 7], 'r': [3, 8], 'v': [3], 'z': [6], 'm': [7], 'u': [7]})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
