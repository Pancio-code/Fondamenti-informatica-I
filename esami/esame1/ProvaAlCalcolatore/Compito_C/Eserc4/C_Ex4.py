from tester import tester_fun

def C_Ex4(file):
    diz={}
    f=open(file,'r',encoding='UTF-8')
    f.readline()
    portate={}
    for r in f:
        r1=r.strip().split(',')
        tavolo=int(r1[0])
        clienti=int(r1[1])
        portata=r1[2]
        quantità=int(r1[3])
        prezzo=int(r1[4])
        parz=portate.get(tavolo,[])
        if parz==[]:
            portate[tavolo]=[0,0,0,clienti]
        parz=portate.get(tavolo)
        if portata=='antipasto':
            parz[0]+=quantità
            portate[tavolo]=parz
        if portata=='pizza':
            parz[1]+=quantità
            portate[tavolo]=parz
        if portata=='bevanda':
            parz[2]+=quantità
            portate[tavolo]=parz
        diz[tavolo]=diz.get(tavolo,0)+(quantità*prezzo)
    f.close()
    for key in portate:
        c=portate.get(key)
        for i in c:
            if i>c[3]:
                diz[key]=diz.get(key)-(i-c[3])
    return diz

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex4, ['comande1.csv'],{1:9, 2:6})
counter_test_positivi += tester_fun(C_Ex4, ['comande2.csv'],{1:23, 2:6})
counter_test_positivi += tester_fun(C_Ex4, ['comande3.csv'],{1:23, 2:6, 3:2})
counter_test_positivi += tester_fun(C_Ex4, ['comande4.csv'],{1: 23, 2: 11, 3: 14})
counter_test_positivi += tester_fun(C_Ex4, ['comande5.csv'],{1: 23, 2: 11, 3: 14, 4: 17})

print('La funzione',C_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
