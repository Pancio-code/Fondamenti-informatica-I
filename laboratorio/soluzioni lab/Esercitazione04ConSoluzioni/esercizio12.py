n = int(input("Inserire un numero naturale maggiore di 1: "))
print ("I numeri primi tra 1 e", n, "sono:")
cont = 2
while cont <= n :  
    primo = True  
    divisore = 2
    while divisore < cont :  
        if cont % divisore == 0 :
            primo = False  
        divisore = divisore + 1  
    if primo == True :
        print (cont)
    cont = cont + 1

# per ottimizzare, sostituire
# while divisore < cont:
# con
# while divisore <= cont/2 and primo == True :  
