#Scrivere un programma che calcola la media di una sequenza di n>=0 interi
#media di una sequenza di n>=0 interi con lettura fuori ciclo
a=input('inserire un intero("*" per terminare): ')
i=0
media=0
while a!='*':
    i=i+1
    media=(int(media)+int(a))
    a=input('inserire un intero("*" per terminare): ') 
if i>0:
    print(media/i)
else:
    print('non sono stati inseriti valori')
