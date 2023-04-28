a=input('inserire una stringa: ')
c=input('inserire un carattere: ')
i=0
primo_c=c
A=''
while i<len(a):
    if a[i] != primo_c:
        A=A+a[i]
    if a[i]==primo_c:
        primo_c=''
    i=i+1
print(A)
