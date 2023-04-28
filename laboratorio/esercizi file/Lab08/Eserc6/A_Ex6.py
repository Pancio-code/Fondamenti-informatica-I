f=open("movimenti.csv",'r',encoding='UTF-8')
f1=open("resoconto.csv",'w',encoding='UTF-8')
r=f.readline()
p='nome,TotaleMovimento'
print(p,end='\n',file=f1)
r=f.readline().strip().split(',')
s=[]
t=[]

while len(r)==2:
    s.append(r[0])
    s.append(r[1])
    r=f.readline().strip().split(',')
for i in range(0,len(s),2):
    somma=0
    if s.count(s[i])>1 and s[i] not in t:
        somma=somma+int(s[i+1])
        for l in range(i+2,len(s),2):
            if s[l]==s[i]:
                somma=somma+int(s[l+1])
                t.append(s[l])
        if somma>=0:
            somma='+'+str(somma)
        p=s[i]+','+str(somma) 
        print(p,end='\n',file=f1)
    else:
        if s[i] not in t:
            t.append(s[i])
            somma=somma+int(s[i+1])
            if somma>=0:
                somma='+'+str(somma)
            p=s[i]+','+str(somma)
            print(p,end='\n',file=f1)
f.close()
f1.close()

##f=open("movimenti.csv", "r", encoding="UTF-8")
##l1=[]
##l2=[]
##f.readline()
##for riga in f:
##    l=riga.strip().split(",")
##    nome=l[0]
##    movimento=int(l[1])
##    if nome in l1:
##        i=l1.index(nome)
##        l2[i]=l2[i]+movimento
##    else:
##        l1.append(nome)
##        l2.append(movimento)
##f.close()
##f2=open("resoconto.csv", "w", encoding="UTF-8")
##print("Nome,TotaleMovimento", file=f2)
##for i in range(len(l1)):
##    if l2[i]>=0:
##        stringa="+"+str(l2[i])
##    else:
##        stringa=str(l2[i])
##    print(l1[i]+","+stringa,file=f2)
##f2.close()
##        
        
        
    
    

