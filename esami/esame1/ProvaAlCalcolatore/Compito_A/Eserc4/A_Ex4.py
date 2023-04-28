from tester import tester_fun

def A_Ex4(file):
    diz={}
    diz1={}
    lista=[]
    f=open(file,'r',encoding='UTF-8')
    f.readline()
    for riga in f:
        pulita=riga.strip().split(',')
        acquirente=pulita[0]
        venditore=pulita[1]
        pittore=pulita[2]
        if venditore=='':
            opere=diz1.get(acquirente,[])
            opere.append(pittore)
            diz[acquirente]=diz.get(acquirente,0)+1
            diz1[acquirente]=opere
        else:
            opere=diz1.get(acquirente,[])
            opere1=diz1.get(venditore,[])
            if pittore not in opere1:
                continue
            else:
                opere.append(pittore)
                opere1.remove(pittore)
                diz[acquirente]=diz.get(acquirente,0)+1
                diz[venditore]=diz.get(venditore,0)-1
                diz1[acquirente]=opere
                diz1[venditore]=opere1
        print(diz)
        print(diz1)
    massimo=max(diz.values())
    for f in diz:
        if diz.get(f)==massimo:
            lista.append(f)
    return sorted(lista)
            
            
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['vendite1.csv'] ,['Mario'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite2.csv'] ,['Gianni', 'Mario', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite3.csv'] ,['Gianni', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite4.csv'] ,['Gianni', 'Maria', 'Paolo'] )
counter_test_positivi += tester_fun(A_Ex4, ['vendite5.csv'] ,['Paolo'] )

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
