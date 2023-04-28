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
