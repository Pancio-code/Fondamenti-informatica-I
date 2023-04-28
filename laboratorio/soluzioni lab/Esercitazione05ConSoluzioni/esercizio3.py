lato = int(input('Inserisci il lato del quadrato: '))

for i in range(1, lato + 1):
    if i == 1 or i == lato: # prima ed ultima riga sono piene
        print('*'*lato)
    elif i <= lato//2:  # siamo nella prima metà del disegno
        k = i-2 #numero di spazi bianchi prima della prima diagonale e dopo la seconda
        h = (lato - 4 - 2*k) # numero di spazi bianchi TRA le diagonali
        print('*'+' '*k+'*'+' '*h+'*'+' '*k+'*')
    elif i == (lato + 1)/2: # se il lato è dispari disegno la riga centrale in cui c'è un solo asterisco
        print('*'+' '*(i-2)+'*'+' '*(i-2)+'*')
    else: # siamo nella seconda metà del disegno
        k = lato-i-1 #numero di spazi bianchi prima della prima diagonale e dopo la seconda
        h = (lato - 4 - 2*k) # numero di spazi bianchi TRA le diagonali
        print('*'+' '*k+'*'+' '*h+'*'+' '*k+'*')


# versione con doppio ciclo

#lato = int(input('Inserisci il lato del quadrato: '))

#for i in range(1, lato + 1):
#    for j in range(1, lato + 1):
#        if (i == 1) or (i== lato) or (j == 1) or (j == lato) :
#            print('*',end='')
#        else:
#            print(' ',end='')
#    print()
