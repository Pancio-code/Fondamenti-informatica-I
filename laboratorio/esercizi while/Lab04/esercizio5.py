a=input('inserire una stringa(INVIO per terminare): ')
bigger=a
while a!='':
    if len(bigger)<len(a):
        bigger=a
    a=input('inserire una stringa(INVIO per terminare): ')

print(bigger)
