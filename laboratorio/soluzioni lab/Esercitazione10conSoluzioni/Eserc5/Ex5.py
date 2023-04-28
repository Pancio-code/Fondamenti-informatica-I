from tester import tester_fun

def Ex5(file):
    import re
    altri = 0
    invalidi = 0
    domestici = 0
    regex = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$' #trova solo i validi
    with open(file) as f:
        counter = len(f.readlines())
    with open(file) as f:
        ris = re.finditer(regex, f.read(), re.MULTILINE)
        for val in ris:
            if val.group(1) == '192' and val.group(2) == '168':
                domestici += 1
            else:
                altri += 1
    invalidi = counter - domestici - altri
    return {'invalidi' : invalidi, 'domestici': domestici, 'altri' : altri}
    
    
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
