n=int(input('inserire lato di un quadrato: '))
print('*'*n)
for i in range (n-2):
    print('*','*',sep=' '*(n-2))
print('*'*n)
