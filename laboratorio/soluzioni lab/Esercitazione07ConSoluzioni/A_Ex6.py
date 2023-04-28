from tester import tester_fun

def A_Ex6(a,b):
    r=set()
    for t in a:
        for tu in b:
            if t[1]==tu[0]:
                r.add((t[0],tu[1]))
    return r

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex6, [{('Giovanni', 'Napoli'), ('Marco', 'Roma'), ('Giuseppe', 'Rieti'), ('Aldo', 'Torino')}, {('Napoli', 'Campania'), ('Benevento', 'Campania'), ('Roma', 'Lazio'), ('Rieti', 'Lazio'), ('Genova', 'Liguria')}] , {('Giovanni', 'Campania'), ('Marco', 'Lazio'), ('Giuseppe', 'Lazio')})
counter_test_positivi += tester_fun(A_Ex6, [{('Giovanni', 'Napoli')}, {('Roma', 'Lazio')}] , set())
counter_test_positivi += tester_fun(A_Ex6, [set(), {('Napoli', 'Campania')}] , set())
counter_test_positivi += tester_fun(A_Ex6, [{('Giovanni', 'Napoli'), }, {('Napoli', 'Campania')}] , {('Giovanni', 'Campania')})
counter_test_positivi += tester_fun(A_Ex6, [{('Giovanni', 'Napoli'), ('Marco', 'Roma')}, {('Napoli', 'Campania'), ('Roma', 'Lazio'), ('Rieti', 'Lazio')}] , {('Giovanni', 'Campania'), ('Marco', 'Lazio')})

print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
