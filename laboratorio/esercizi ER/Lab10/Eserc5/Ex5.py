from tester import tester_fun
import re

def Ex5(file):
    f=open(file,'r',encoding='UTF-8')
    diz={'invalidi': 0, 'domestici': 0, 'altri': 0}
    for riga in f:
        nuovo=riga.strip()
        pattern=r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d*)'
        trov=re.search(pattern,nuovo)
        if trov:
            if int(trov.group(1))<=255 and int(trov.group(2))<=255 and int(trov.group(3))<=255 and int(trov.group(4))<=255 and len(trov.group(4))<4:
                if trov.group(1)=='192' and trov.group(2)=='168':
                    diz['domestici']+=1
                else:
                    diz['altri']+=1
            else:
                diz['invalidi']+=1
        else:
            diz['invalidi']+=1
    f.close()
    return diz

##    altri = 0
##    invalidi = 0
##    domestici = 0
##    regex = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$' #trova solo i validi
##    with open(file) as f:
##        counter = len(f.readlines())
##    with open(file) as f:
##        ris = re.finditer(regex, f.read(), re.MULTILINE)
##        for val in ris:
##            if val.group(1) == '192' and val.group(2) == '168':
##                domestici += 1
##            else:
##                altri += 1
##    invalidi = counter - domestici - altri
##    return {'invalidi' : invalidi, 'domestici': domestici, 'altri' : altri}    
##    
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex5, ["ip1.txt"] , {'invalidi': 0, 'domestici': 0, 'altri': 5})
counter_test_positivi += tester_fun(Ex5, ["ip2.txt"] , {'invalidi': 2, 'domestici': 1, 'altri': 2})
counter_test_positivi += tester_fun(Ex5, ["ip3.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
counter_test_positivi += tester_fun(Ex5, ["ip4.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
counter_test_positivi += tester_fun(Ex5, ["ip5.txt"] , {'invalidi': 3, 'domestici': 0, 'altri': 2})

print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
