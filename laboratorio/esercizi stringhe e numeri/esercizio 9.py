from math import *
x=int(input('scrivere un numero intero diverso da zero: '))
y=int(input('scrivere un numero intero: '))
z=int(input('scrivere un numero intero: '))
print('con i tre numeri a,b,c svolgeremo una equazione di secondo grado')
print('la soluzione 1 è:',(-y+sqrt(pow(y,2)-(4*x*z)))/(2*x))
print('la soluzione 2 è:',(-y-sqrt(pow(y,2)-(4*x*z)))/(2*x))
