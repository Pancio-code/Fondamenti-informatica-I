a=int(input('inserire un intero: '))
i=1
precedente=1
c=2
if a>=1:
    print(precedente)
if a>=2:
    print(i)
while c<=a and a>2:
    somma=i+precedente
    print(somma)
    precedente=i
    i=somma
    c=c+1

#soluzione alternativa

n = int(input("inserisci un intero : "))
precedente1=1
precedente2=1
if n==1:
    print(1)
else:
    print(1)
    print(1)
    i=3
    while (i <= n):
        successivo=precedente1+precedente2
        print(successivo)
        precedente2=precedente1
        precedente1=successivo
        i=i+1


    
    
    
