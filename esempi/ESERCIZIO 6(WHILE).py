#stampa i singoli caratteri di una stringa distanziati di passo :
# s[0], s[passo], s[2*passo], etc...
a=input('inserisci una stringa: ')
n=input('inserisci un intero: ')
c=0
while int(c)<len(a):
    print(a[c])
    c=c+int(n)
