a=input('inserire una stringa: ')
n=0
for i in range(len(a)):
    if ord(a[i])<=ord(a[n]):
        minimo=a[i]
    print(a[i],ord(a[i]))
    n=i
print('il carettere con il valore unicode più piccolo è ',minimo,'=',ord(minimo))
        
