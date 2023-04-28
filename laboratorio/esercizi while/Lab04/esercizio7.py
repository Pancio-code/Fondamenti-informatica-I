precedente=input('inserire una stringa: ')
s=input('inserire una stringa: ')
successiva=input('inserire una stringa: ')
while len(precedente)+len(s)!=len(successiva):
    precedente=s
    s=successiva
    successiva=input('inserire una stringa: ')
    
