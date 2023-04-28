a=input('inserire una stringa: ')
p=0
r='NO'
for i in range(1,len(a)):
    if a[i]==a[p]:
        r='SI'
        break
    p=i
print(r)
    
