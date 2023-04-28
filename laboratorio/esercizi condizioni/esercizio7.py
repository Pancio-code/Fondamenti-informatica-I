a=int(input('inserire un anno: '))
m=int(input('inserire un mese: '))

if m>=1 and m<=11:
    print(m+1,'e',a)
elif m==12:
    print(1,'e',a+1)
else:
    print('error')
