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
f2=open("resoconto.csv", "w", encoding="UTF-8")
print("Nome,TotaleMovimento", file=f2)
for i in range(len(l1)):
    if l2[i]>=0:
        stringa="+"+str(l2[i])
    else:
        stringa=str(l2[i])
    print(l1[i]+","+stringa,file=f2)
f2.close()
