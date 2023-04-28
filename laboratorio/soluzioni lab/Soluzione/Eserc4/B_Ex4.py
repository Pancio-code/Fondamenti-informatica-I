from tester import tester_fun

def B_Ex4(file):
    f = open(file,'r',encoding='UTF-8')
    diz={}
    for r in f:
        r1=r.strip().split(',')
        treno=r1[0]
        stazione=r1[1]
        viaggio=r1[2]
        if stazione not in diz:
            diz[stazione]=[]
        parz=diz.get(stazione)
        if viaggio=='P':
            parz.append(treno)
            diz[stazione]=sorted(list(set(parz)))
        else:
            if treno in parz:
                parz.remove(treno)
                diz[stazione]=parz
    f.close()
    return diz
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""Dati di test forniti in aula"""

counter_test_positivi = 0
total_tests = 10

counter_test_positivi += tester_fun(B_Ex4, ['treni1.csv'],{'Termini': ['T72', 'T81'], 'Tiburtina': ['T61'], 'Trastevere': []})
counter_test_positivi += tester_fun(B_Ex4, ['treni2.csv'],{'Termini': ['T72', 'T81'], 'Tiburtina': ['T61'], 'Trastevere': ['T53']})
counter_test_positivi += tester_fun(B_Ex4, ['treni3.csv'],{'Termini': ['T72'], 'Tiburtina': ['T61'], 'Trastevere': ['T53', 'T81']})
counter_test_positivi += tester_fun(B_Ex4, ['treni4.csv'],{'Termini': ['T72'], 'Tiburtina': ['T53', 'T61'], 'Trastevere': ['T81']})
counter_test_positivi += tester_fun(B_Ex4, ['treni5.csv'],{'Termini': ['T12', 'T72'], 'Tiburtina': ['T53', 'T61'], 'Trastevere': ['T81'], 'SanPietro': []})
counter_test_positivi += tester_fun(B_Ex4, ['treni6.csv'],{'Tiburtina': ['TT1', 'TT2'], 'Prenestina': ['T61'], 'Trastevere': []})
counter_test_positivi += tester_fun(B_Ex4, ['treni7.csv'],{'Tiburtina': ['TT1', 'TT2'], 'Prenestina': ['T61'], 'Trastevere': ['T53']})
counter_test_positivi += tester_fun(B_Ex4, ['treni8.csv'],{'Tiburtina': ['TT2'], 'Prenestina': ['T61'], 'Trastevere': ['T53', 'TT1']})
counter_test_positivi += tester_fun(B_Ex4, ['treni9.csv'],{'Tiburtina': ['TT2'], 'Prenestina': ['T53', 'T61'], 'Trastevere': ['TT1']})
counter_test_positivi += tester_fun(B_Ex4, ['treni10.csv'],{'Tiburtina': ['T12', 'TT2'], 'Prenestina': ['T53', 'T61'], 'Trastevere': ['TT1'], 'SanPietro': []})

print('La funzione',B_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

