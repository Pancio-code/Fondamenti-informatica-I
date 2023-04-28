x=input('inserire una stringa: ')
if x[0]==x[len(x)-1]:
    print('caratteri iniziali e finali uguali')
elif len(x) == 0:
    print('Stringa vuota!')
else:
    print('caratteri iniziali e finali diversi')
