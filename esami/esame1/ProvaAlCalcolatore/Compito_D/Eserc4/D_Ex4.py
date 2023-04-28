from tester import tester_fun

def D_Ex4(file,ore,minuto):
    f=open(file,'r',encoding='UTF-8')
    diz={}
    lista=[]
    for riga in f:
        f1=riga.strip().split(',')
        codice=f1[0]
        ora=f1[1]
        if ora[0] not in'+-':
            minuti=f1[2]
            diz[codice]=[int(ora),int(minuti)]
        else:
            minuti=f1[1]
            treno=diz.get(codice)
            nuovo=int(minuti)+treno[1]
            if nuovo>=60:
                treno[1]=nuovo-60
                treno[0]+=1
            elif nuovo<0:
                if abs(nuovo)<60:
                    treno[1]=abs(nuovo)
                    treno[0]-=1
                else:
                    treno[1]=abs(nuovo)-60
                    treno[0]-=2
            else:
                treno[1]=nuovo
            diz[codice]=treno
    print(diz)
    for key in diz:
        val=diz.get(key)
        if val[0]<ore:
            lista.append(key)
        elif val[0]==ore:
            if val[1]<=minuto:
                lista.append(key)
    return sorted(lista)          
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex4, ['ritardi1.csv',12,20] ,['54200','6310'])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi2.csv',12,20] ,['54200', '6310', '79001'])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi1.csv',10,20] ,[])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi2.csv',11,40] ,['54200'] )
counter_test_positivi += tester_fun(D_Ex4, ['ritardi3.csv',14,20] ,['54200', '6310', '6550', '79001'])

print('La funzione',D_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
