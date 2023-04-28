n1=int(input('inserire un numero intero: '))
n2=int(input('inserire un numero intero: '))
n3=int(input('inserire un numero intero: '))
if n1>n2>n3:
    print(n1,n2,n3)
elif n2>n1>n3:
    print(n2,n1,n3)
elif n1>n3>n1:
    print(n1,n3,n2)
elif n2>n3>n1:
    print(n2,n3,n1)
elif n3>n2>n1:
    print(n3,n2,n1)
else:
    print(n3,n1,n2)
    
