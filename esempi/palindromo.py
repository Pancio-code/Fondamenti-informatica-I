from math import *
p=input('inserire una stringa: ')
x=len(p)

if x%2==0 and p[ceil((x)/2)-1::-1]==p[ceil((x)/2):]:
    print('è un palindromo')
elif x%2!=0 and p[ceil((x)/2)-1::-1]==p[ceil((x)/2)-1:]:
    print('è un palindromo')
else:
    print('non è un palindromo')

