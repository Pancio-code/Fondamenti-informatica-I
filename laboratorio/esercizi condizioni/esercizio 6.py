a=int(input('inserire un intero: '))
b=int(input('inserire un intero: '))
c=int(input('inserire un intero: '))
if a>=0 and b>=0 and c>=0 and (a+b)>c and (a+c)>b and (b+c)>a and a==b==c:
      print('è un triangolo equilatero')
elif a>=0 and b>=0 and c>=0 and (a+b)>c and (a+c)>b and (b+c)>a and a!=b!=c:
      print('è un triangolo scaleno')
elif a>=0 and b>=0 and c>=0 and (a+b)>c and (a+c)>b and (b+c)>a and (a==b or a==c or b==c):
      print('è un triangolo isoscele')
else:
      print('non è un triangolo')


#if a+b>c and a+c>b and b+c>a: #La somma di due lati è sempre maggiore del terzo
    #if a==b and b==c: #I tre lati sono tutti uguali
        #print ("Equilatero")
    #elif a==b or a==c or b==c: #Almeno due lati sono uguali
        #print("Isoscele")
    #else:
        #print("Scaleno")
#else: #Un lato è più corto o uguale alla somma degli altri 2
    #print("I tre interi non corrispondono a un triangolo valido")

