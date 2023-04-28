from tester import tester_fun

def A_Ex4(file):
    f=open(file,'r',encoding='UTF-8')
    diz={}
    for r in f:
        r1=r.strip().split(',')
        partita=int(r1[0])
        scomessa=r1[1]
        importo=int(r1[2])
        quota=int(r1[3])
        if partita not in diz:
            if scomessa=='1':
                diz[partita]=[importo,importo*quota,0,0]
            elif scomessa=='X':
                diz[partita]=[importo,0,importo*quota,0]
            elif scomessa=='2':
                diz[partita]=[importo,0,0,importo*quota]
        else:
            lista=diz.get(partita)
            lista[0]+=importo
            if scomessa=='1':
                lista[1]+=importo*quota
                diz[partita]=lista
            elif scomessa=='X':
                lista[2]+=importo*quota
                diz[partita]=lista
            elif scomessa=='2':
                lista[3]+=importo*quota
                diz[partita]=lista
    f.close()
    return diz
            

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['performance1.csv'],{12: [27, 20, 10, 36]})
counter_test_positivi += tester_fun(A_Ex4, ['performance2.csv'],{12: [27, 20, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance3.csv'],{12: [37, 50, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance4.csv'],{12: [49, 50, 34, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance5.csv'],{12: [69, 110, 34, 36], 10: [37, 20, 24, 45]})



print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
