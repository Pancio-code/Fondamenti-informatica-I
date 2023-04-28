x=float(input('inserire l\'età di un cane: '))
y=10.5*x
z=4*(x-2)
if x < 0:
    print("L'eta' deve essere positiva!")
elif x<=2:
    print('l\'età umana corrispondente è:',y)
elif x>2:
    print('l\'età umana corrispondente è:',(10.5*2)+z)

    
## Soluzione alternativa: si noti che nel codice possiamo 
## fare a meno di una istruzione print, ma abbiamo un livello
## di indentazione in più
##        
##etaCane = float(input("Inserisci eta' del cane: "))
##if etaCane < 0:
##        print("L'eta' deve essere positiva!")
##else:
##        if etaCane <= 2 :
##                etaCaneUmana = etaCane * 10.5
##        elif etaCane > 2:
##                etaCaneUmana = 21 + (etaCane - 2)*4
##        print("L'eta' del cane è':", etaCaneUmana)
