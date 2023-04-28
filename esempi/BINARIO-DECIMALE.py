s=input("inserisci una stringa corrispondente a un binario: ")
valore=0
potenza=len(s)-1
for c in s:
    valore=valore+int(c)*2**potenza
    potenza=potenza-1
print(s,"vale",valore)
