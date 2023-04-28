from math import *
n=int(input('inserire un numeratore intero: '))
m=int(input('inserire un denominatore intero: '))
if  n<m:
    print('la frazione è propria')
elif n%m==0:
    print('la frazione è apparente')
elif n>m and n%m!=0:
    print('la frazione è impropria')
