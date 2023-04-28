a=input('inserire una stringa: ')
if(len(a)>0):
       b=a[0]
i=0
while i<len(a):
       if ord(a[i])>b:
           b=ord(a[i])
       i+=1

if len(a)>0:
       print(b)

