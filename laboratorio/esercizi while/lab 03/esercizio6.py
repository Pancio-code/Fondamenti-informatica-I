a=int(input('inserire un intero: '))
i=2
primo=True

while i<=a/2 and primo:
      if a%i==0:
       primo=False
      i+=1
if primo==True and a!=1:
      print('il numero è primo')
else:
      print('il numero non è primo')



