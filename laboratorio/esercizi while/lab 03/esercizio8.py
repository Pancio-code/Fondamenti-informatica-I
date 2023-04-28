a=input('inserire una stringa: ')
prima=a

while len(a)>0:
    if a<prima:
     prima=a
    a=input('inserire una stringa: ')
    
print('la prima stringa in ordine alfabetico è',prima)
    


