i=input('inserie un numero intero (* per terminare): ' )
x=0
while i!='*':
    if '-' not in i and int(i)!=0:
     x=x+1
    i=input('inserisce un altro intero(* per terminare): ')

print('hai inserito',x,'interi positivi')
