from random import randint
g=0
for i in range(100000,888888):
    r=str(i)
    g+=1
    if '1' in r and '2' in r and '4' in r and '5' in r and '7' in r and '8' in r:
            r1=str(int(r)*2)
            r2=str(int(r)*3)
            r3=str(int(r)*4)
            r4=str(int(r)*5)
            r5=str(int(r)*6)
            if '1' in r1 and '2' in r1 and '4' in r1 and '5' in r1 and '7' in r1 and '8' in r1:
               if '1' in r2 and '2' in r2 and '4' in r2 and '5' in r2 and '7' in r2 and '8' in r2:
                   if '1' in r3 and '2' in r3 and '4' in r3 and '5' in r3 and '7' in r3 and '8' in r3:
                       if '1' in r4 and '2' in r4 and '4' in r4 and '5' in r4 and '7' in r4 and '8' in r4:
                           if '1' in r5 and '2' in r5 and '4' in r5 and '5' in r5 and '7' in r5 and '8' in r5:
                               ns=r
print("il numero è ",int(ns),g)
                   
