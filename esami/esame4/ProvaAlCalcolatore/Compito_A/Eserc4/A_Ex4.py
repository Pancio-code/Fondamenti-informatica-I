from tester import tester_fun

def A_Ex4(file):
    diz={}
    f=open(file,'r',encoding='UTF-8')
    giorno=0
    for r in f:
        giorno+=1
        importi=[]
        r1=r.strip().split(';')
        for l in r1:
            ai=l.split('-')
            importi.append(int(ai[1]))
        for i in r1:
            a1=i.split('-')
            if int(a1[1])==max(importi):
                massimo=diz.get(a1[0],[])
                massimo.append(giorno)
                diz[a1[0]]=massimo
            else:
                diz[a1[0]]=diz.get(a1[0],[])
    f.close()
    return diz
            
            

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['performance1.csv'],{'Mario': [1, 2], 'Marco': [], 'Anna': [3,4], 'Aldo': [2], 'Antonio': [5]})
counter_test_positivi += tester_fun(A_Ex4, ['performance2.csv'],{'Mario': [2], 'Marco': [], 'Anna': [1,3,4], 'Aldo':[], 'Antonio':[5]})
counter_test_positivi += tester_fun(A_Ex4, ['performance3.csv'],{'Mario': [], 'Marco': [], 'Anna': [1,2,3,4,5], 'Antonio':[]})
counter_test_positivi += tester_fun(A_Ex4, ['performance4.csv'],{'Mario': [1,4], 'Anna': [2,3,5]})
counter_test_positivi += tester_fun(A_Ex4, ['performance5.csv'],{'Mario': [1,2,4], 'Marco': [1,4], 'Anna': [1,3,4,5], 'Aldo': [2,3], 'Antonio': [5]})



print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
