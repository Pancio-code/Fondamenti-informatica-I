a=int(input('inserire un intero(0 per terminare): '))
somma=0
while a!=0:
    if a%3==0:
        somma=somma+a
    a=int(input('inserire un intero(0 per terminare): '))
print('la somma degli interi divisibili per tre è:',somma)
