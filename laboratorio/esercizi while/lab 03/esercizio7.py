a=input('inserire una stringa: ')
i=0
somma=0
c='la stringa è finita'
while i<len(a) and somma<=500 :
    somma=somma+ord(a[i])
    print(a[i])
    i+=1
    

if i>=len(a) and somma> 500:
    print("stringa consumata e somma >500")
elif i>=len(a):
    print("stringa consumata")
else:
    print("somma > 500")

print("i =",i,"somma =",somma) 


        
