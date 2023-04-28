q = 34 #Quotation mark character
l=[
    "q = 34 #Quotation mark character",
    "l = [",
    "   ",
    "]",
    "for i in range(0,2): #Print opening code",
    "   print(l[i])",
    "for elem in l: #Print list",
    "   print(chr(q) + elem + chr(q) + ',')",
    "for i in range(2,len(l)): #Print this code",
    "    print(l[i])",
]
for i in range(0,2): #Print opening code
    print(l[i])
for elem in l: #Print list
    print(l[2]+chr(q) + elem + chr(q) + ',')
for i in range(3,len(l)): #Print this code
    print(l[i])
