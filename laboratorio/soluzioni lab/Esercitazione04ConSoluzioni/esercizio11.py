s=input('inserisci una stringa ')
#s=s.lower() #decommentare per non fare distinzione fra minuscole e maiuscole.
i=0
massimo=s.count(s[i])
maxCar=s[i]
while(i<len(s)):
    print(s[i])
    if s.count(s[i])>=massimo:
        massimo=s.count(s[i])
        maxCar=s[i]
    i=i+1
print(maxCar)
