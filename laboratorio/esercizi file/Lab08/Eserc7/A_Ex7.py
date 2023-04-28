f=open("movimenti.csv",'r',encoding='UTF-8')
f1=open("resoconto.csv",'w',encoding='UTF-8')
r=f.readline()
p='nome,TotaleMovimento'
print(p,end='\n',file=f1)
f=open("movimenti.csv", "r", encoding="UTF-8")
l1=[]
l2=[]
f.readline()
for riga in f:
    l=riga.strip().split(",")
    nome=l[0]
    movimento=int(l[1])
    if nome in l1:
        i=l1.index(nome)
        l2[i]=l2[i]+movimento
    else:
        l1.append(nome)
        l2.append(movimento)
f.close()
f2=open("resocontoOrdinato.csv", "w", encoding="UTF-8")
l3=list(set(l2))
l3.sort()
l3.reverse()
print("Nome,TotaleMovimento", file=f2)
for tot in l3:
    if tot>=0:
        stringa="+"+str(tot)
    else:
        stringa=str(tot)
    for i in range(len(l2)):
        if l2[i]==tot:
            print(l1[i]+","+stringa,file=f2)
f2.close()




##r=f.readline().strip().split(',')
##s=[]
##t=[]
##s2=[]
##s3=[]
##resoconto=[]
##
##while len(r)==2:
##    s.append(r[0])
##    s.append(r[1])
##    r=f.readline().strip().split(',')
##for i in range(0,len(s),2):
##    somma=0
##    if s.count(s[i])>1 and s[i] not in t:
##        somma=somma+int(s[i+1])
##        for l in range(i+2,len(s),2):
##            if s[l]==s[i]:
##                somma=somma+int(s[l+1])
##                t.append(s[l])
##        s2.append(s[i])
##        s3.append(somma)
##    else:
##        if s[i] not in t:
##            t.append(s[i])
##            somma=somma+int(s[i+1])
##            s2.append(s[i])
##            s3.append(somma)
##while len(s3)!=0:
##    M=max(s3)
##    c=s3.index(M)
##    if M>=0:
##        M='+'+str(M)    
##    p=s2[c]+','+str(M)
##    print(p,end='\n',file=f1)
##    s3.remove(int(M))
##    s2.remove(s2[c])
##f.close()
##f1.close()            

