t=int(input('inserire una temperatura: '))
p=input('inserire C o F: ')
if p.count('C')==1 and t>=100:
      print('a',str(t)+p,'l\'acqua è allo stato gassoso')
elif p.count('C')==1 and t<0:
      print('a',str(t)+p,'l\'acqua è allo stato solido')
elif p.count('C')==1 and t>=0 and t<100:
      print('a',str(t)+p,'l\'acqua è allo stato liquido')
if p.count('F')==1 and t>=212:
      print('a',str(t)+p,'l\'acqua è allo stato gassoso')
elif p.count('F')==1 and t<32:
      print('a',str(t)+p,'l\'acqua è allo stato solido')
elif p.count('F')==1 and t>= 32and t<212:
      print('a',str(t)+p,'l\'acqua è allo stato liquido')

      
