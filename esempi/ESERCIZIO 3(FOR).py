n=int(input('inserire grado del polinomio: '))
x=int(input('inserire valore della x: '))
somma=0
for i in range(0,n+1):
            a=int(input('coefficente di a: '))
            somma=somma+(a*(x**i))
            print(somma)

print(somma)
            
