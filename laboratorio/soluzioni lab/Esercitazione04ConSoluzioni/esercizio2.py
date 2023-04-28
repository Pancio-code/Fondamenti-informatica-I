i=int(input('inserisci un intero (0 per terminare): '))
somma=0
while i!=0:
    if i%3 == 0:
        somma=somma+i
    i=int(input('inserisci un intero (0 per terminare): '))
print(somma)
