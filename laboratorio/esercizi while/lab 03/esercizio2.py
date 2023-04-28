i=input('inserie un numero intero (* per terminare): ' )
somma=0
while i!='*':
    if '-' in i:
     somma=int(somma)+int(i)
    i=input('inserisce un altro intero(* per terminare): ')
print('la somma degli interi negativi è',somma)
    

