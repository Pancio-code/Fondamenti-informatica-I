c=input('inserire un carattere: ')
a='casa'
while a.count(c)<3:
    a=input('inserire una stringa: ')
    print(c,'compare',a.count(c),'volte in',a)
