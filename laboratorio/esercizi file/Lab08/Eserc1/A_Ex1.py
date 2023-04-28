f=open("Fibonacci.txt", "w", encoding="UTF-8")
n1=0
n2=1
print(n1,file=f)
print(n2,file=f)
i=0
while (i<98):
    n3=n1+n2
    print(n3,file=f)
    n1=n2
    n2=n3
    i=i+1
f.close()

