s=input("inserisci una stringa: ")
massimo=len(s)
while s!='':
    if len(s)>massimo:
        massimo=len(s)
    s=input("inserisci una stringa: ")
print(massimo)
