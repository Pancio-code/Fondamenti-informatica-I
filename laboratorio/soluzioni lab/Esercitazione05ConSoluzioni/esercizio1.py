base = int(input('Inserisci la base del triangolo (dispari): '))

altezza = (base + 1) // 2

for i in range(1, altezza + 1):
    print(' '*(altezza-i)+'*'*((2*i)-1))

# versione con ciclo annidato

#base = int(input('Inserisci la base del triangolo (dispari): '))

#altezza = (base + 1) // 2

#for i in range(1, altezza + 1):
#    for j in range(1, altezza+i):   # il numero di caratteri da stampare ad ogni riga
                                    # è pari al numero di spazi (altezza-i) +
                                    # il numero di asterischi (2*i)-1 (vedi anche
                                    # soluzione con unico ciclo for. Si noti poi che
                                    # altezza-i+(2*i)-1+1=altezza+i
#        if j <= altezza-i:
#            print(' ',end='')
#        else:
#            print('*',end='')
#    print()
