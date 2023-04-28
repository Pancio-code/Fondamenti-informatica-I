from tester import tester_fun

def A_Ex4(file):
    f=open(file,'r',encoding='UTF-8')
    nomi=f.readline().strip().split(',')
    diz={}
    for i in nomi:
        diz[i]=[0,0,0,0]
    for r in f:
        r1=r.strip().split(',')
        r2=[]
        for m in r1:
            if int(m)!=0:
                r2.append(m)     
        mass=int(max(r2))
        mini=int(min(r2))
        c=0
        for key in diz:
            list=diz.get(key)
            if int(r1[c])==0:
                c+=1
                continue
            else:
                list[1]+=1
                if list[0]==0:
                    list[0]=int(r1[c])
                if int(r1[c])<list[0]:
                    list[0]=int(r1[c])
                if int(r1[c])==mini:
                    list[2]+=1
                if int(r1[c])==mass:
                    list[3]+=1
            diz[key]=list
            c+=1
    f.close()
    return diz 
            
            

                
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['maratone1.csv'],{'Mario': [130, 3, 0, 1], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone2.csv'],{'Mario': [111, 3, 1, 0], 'Paolo': [112, 3, 1, 1], 'Gianna': [113, 2, 1, 0], 'Giulia': [114, 3, 1, 1], 'Riccardo': [115, 2, 0, 2]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone3.csv'],{'Mario': [135, 2, 0, 0], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1], 'Riccardo': [132, 1, 0, 1]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone4.csv'],{'Mario': [121, 4, 1, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 1], 'Riccardo': [132, 1, 0, 0], 'Melania': [124, 3, 1, 2]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone5.csv'],{'Mario': [121, 4, 2, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 2], 'Riccardo': [132, 1, 0, 1]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
