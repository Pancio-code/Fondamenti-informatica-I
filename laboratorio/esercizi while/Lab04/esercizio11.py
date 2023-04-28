a=input('inserie una stringa: ')
i=0
r=0
if a!='':
    s=a[i]
    s=a.count(s)
while i<len(a):
    a.count(a[i])
    if a.count(a[i])>=s:
        s=a.count(a[i])
        r=a[i]
    i=i+1
if a!='':
    print(r)
    print(s)
else:
    print('stringa vuota')

if a!='':
    a=a.lower()
    i=0
    s=a[i]
    s=a.count(s)
while i<len(a):
    a.count(a[i])
    if a.count(a[i])>=s:
        s=a.count(a[i])
        r=a[i]
    i=i+1

if a!='':
    print(r)
    print(s)
