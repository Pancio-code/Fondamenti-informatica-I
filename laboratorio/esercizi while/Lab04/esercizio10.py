n1=int(input("inserisci il primo intero: "))
n2=int(input("inserisci il secondo intero: "))
prodotto=0
volte=abs(n2)
while (volte > 0):
    prodotto=prodotto+n1
    volte=volte-1
if n2 > 0:
    print(prodotto)
else:
    print(-prodotto)
