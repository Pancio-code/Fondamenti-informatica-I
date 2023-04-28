s=input('inserire una sringa: ')
n=int(input('inserire un intero: '))
for i in range(len(s)):
    if ord(s[i])%n==0:
        print(s[i],'=',ord(s[i]), 'è multiplo di',n)
        break
    print(s[i],'=',ord(s[i]))
