from tester import tester_fun

def stringaMaxFreq(file,l):
    parola=l[0]
    cont=0
    testo=open(file,'r',encoding='UTF-8')
    lett=testo.read().split()
    for i in l:
        if i in lett:
            a=lett.count(i)
            print(i,a)
            if a==cont:
                if i<parola:
                    parola=i
            if a>cont:
                cont=a
                parola=i
    testo.close()
    return parola
a=stringaMaxFreq('I_Malavoglia.txt',['mario','maria','marco'])
print(a)
