n=int(input('inserire un intero: '))
if n!=1:
    print('*'*n)
    k=0
    c=4
    if n%2==0:
        for i in range((round(n/2)-1)):
            print('*'+(' '*k)+'*'+(' '*(n-c))+'*'+(' '*k)+'*')
            k=k+1
            c=c+2


        k=round(n/2)-2
        c=n
        for i in range((round(n/2)-1)):
            print('*'+(' '*k)+'*'+(' '*(n-c))+'*'+(' '*k)+'*')
            k=k-1
            c=c-2
    else:
        for i in range((round(n/2+0.1)-2)):
            print('*'+(' '*k)+'*'+(' '*(n-c))+'*'+(' '*k)+'*')
            k=k+1
            c=c+2

        print('*'+' '*(round(((n/2)+0.1))-2)+'*'+' '*(round(((n/2)+0.1))-2)+'*')

        k=round((n/2)+0.1)-3
        c=n-1

        for i in range((round((n/2)+0.1)-2)):
            print('*'+(' '*k)+'*'+(' '*(n-c))+'*'+(' '*k)+'*')
            k=k-1
            c=c-2
        
    print('*'*n)
else:
    print('*'*n)
    
            
    
    
