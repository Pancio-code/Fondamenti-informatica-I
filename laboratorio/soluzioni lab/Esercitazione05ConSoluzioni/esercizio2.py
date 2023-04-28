lato = int(input('Inserisci il lato del quadrato: '))

for i in range(1, lato + 1):
    if i == 1 or i == lato:
        print('*'*lato)
    else:
        print('*'+' '*(lato-2)+'*')
