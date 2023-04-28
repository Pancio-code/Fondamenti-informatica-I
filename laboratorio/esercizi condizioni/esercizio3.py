from math import *
x=int(input('inserie un anno: '))

if x%4==0 and x%100!=0 or x%400==0:
      print("L'anno "+str(x)+' è bisestile')
else:
      print("L'anno "+str(x)+' non è bisestile')
