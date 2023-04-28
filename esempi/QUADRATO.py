#stampa quadrato
l=int(input("inserisci lato del quadrato: "))

for i in range(l):
    for j in range(l):
        print('*',end='')
    print() #vado a capo ogni ciclo
    
# versione senza uso del ciclo
# print(('*'*l+'\n')*l)
#end= inserisce cosa fare dopo
#sep= spazi fra la separazione delle stringhe degli argomenti
