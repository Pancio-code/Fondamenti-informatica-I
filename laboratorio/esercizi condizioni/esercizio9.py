t=int(input('inserire una temperatura: '))
if t>30:
    print('molto caldo')
elif t>20 and t<=30:
    print('caldo')
elif t<=20 and t>10:
    print('gradevole')
else:
    print('freddo')
    
