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
