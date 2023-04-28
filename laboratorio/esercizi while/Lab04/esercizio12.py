a=int(input('inserire un intero: '))
print ("I numeri primi tra 1 e", a, "sono:")
i=2
c=3
primo=True

while i<a:
    primo=True
    while c<i and primo==True:
        if i%c==0:
            primo=False
        c=c+1
    c=2
    if primo==True:
        print(i)
    i=i+1
