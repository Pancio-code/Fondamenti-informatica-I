from tester import tester_fun

def A_Ex2(m,l1,l2):
    r1=0
    m1=[[0 for i in range(len(m[0])-len(l2))]for i in range(len(m)-len(l1))]
    for r in range(len(m)):
        c1=0
        if r+1 in l1:
            continue
        for c in range(len(m[0])):
            if c+1 in l2:
                continue
            m1[r1][c1]=m[r][c]
            c1+=1
        r1+=1
    return m1
    
            


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,5,1],[4,10,11],[3,4,4]],[1,3],[2]],[[9,1],[3,4]])
counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,7,1]],[1],[2]],[[9,1]])
counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,9,1]],[2],[1,3]],[[7]])
counter_test_positivi += tester_fun(A_Ex2, [[[15,5,6,18],[9,7,1,2],[4,3,8,15]],[],[]],[[15,5,6,18],[9,7,1,2],[4,3,8,15]])
counter_test_positivi += tester_fun(A_Ex2, [[[15,18,6,5],[9,0,1,2],[4,3,8,25],[28,21,15,32]],[],[2,4]],[[15,6],[9,1],[4,8],[28,15]])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
