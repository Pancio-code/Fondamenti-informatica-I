b=int(input('inserire un intero positivo dispari: '))
c=1
i=round(b/2)
while c<=b:
    print(' '*i,'*'*c,sep='')
    c=c+2
    i=i-1
