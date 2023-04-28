from tester import tester_fun
import re

def Ex6(file):
    f = open(file,'r', encoding = 'UTF-8')
    regex = '[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    mesi = {'A': ['01',31],'B' : ['02',28],'C': ['03',31],'D' :['04',30],
            'E': ['05',30],'H': ['06',30],'L':['07',31],'M': ['08',31],
            'P': ['09',30],'R': ['10',31],'S': ['11',30],'T':['12',31]}
    lista = []
    for riga in f:
        riga = riga.strip()
        m = re.match(regex,riga)
        if m == None:
            lista.append('Codice errato')
        else:
            anno = int(m.group(1))
            mese = m.group(2)
            giorno = int(m.group(3))
            if anno <= 18:
                anno += 2000
            else:
                anno += 1900
            if mese not in mesi:
                lista.append('Mese errato')
            else:
                maxgiorni = mesi[mese][1]
                mese = mesi[mese][0]
                if giorno > 40:
                    giorno = giorno - 40
                if giorno < 1 or giorno > maxgiorni:
                    lista.append('Giorno errato')
                else:
                    if giorno < 10:
                        giorno = '0'+str(giorno)
                    else:
                        giorno = str(giorno)    
                    lista.append(giorno+'/'+mese+'/'+str(anno))
    return lista

    
##    f=open(file,'r',encoding='UTF-8')
##    lista=[]
##    giusti='ABCDEHLMPRST'
##    for riga in f:
##        riga1=riga.strip()
##        pattern=r'[A-Z]{3}[^A-Z]*[A-Z]{3}[^A-Z]*(\d{2})([A-Z])(\d{2})[^A-Z]*[A-Z]\d{3}[A-Z]'
##        codice=re.search(pattern,riga1)
##        if codice:
##            gg=int(codice.group(3))
##            if codice.group(2) not in giusti:
##                lista.append('Mese errato')
##            elif gg>71 or 31 < gg <41:
##                lista.append('Giorno errato')
##            else:
##                for mese in range(len(giusti)):
##                    if codice.group(2)==giusti[mese]:
##                        if mese<10:
##                            mm='0'+str(mese+1)
##                        else:
##                            mm=str(mese+1)
##                giorno=codice.group(3)
##                anno=codice.group(1)
##                if int(giorno)>40:
##                    giorno=str(int(giorno)-40)   
##                if int(anno)<=18:
##                    anno='20'+anno
##                if int(codice.group(1))>18:
##                    anno='19'+anno
##                if int(giorno)<10:
##                    giorno='0'+giorno
##                if int(giorno)>28 and int(mm)in[2,4,6,9,11]:
##                    if int(giorno)==31 and int(mm)in[4,6,9,11]:
##                        lista.append('Giorno errato')
##                        continue
##                    if int(giorno)>28 and int(mm)==2:
##                        lista.append('Giorno errato')
##                        continue
##                lista.append(giorno+'/'+mm+'/'+anno)
##        else:
##            lista.append('Codice errato')
##    f.close()
##    return lista     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex6, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
counter_test_positivi += tester_fun(Ex6, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
counter_test_positivi += tester_fun(Ex6, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
counter_test_positivi += tester_fun(Ex6, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
counter_test_positivi += tester_fun(Ex6, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
