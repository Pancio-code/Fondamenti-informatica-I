finito=False
while not finito:
    
    #-----------
    base=input("inserisci la base (2..16): ")
    if not (base.isdecimal() and (2<=int(base)<=16)):
        print('inserito un input errato per la base')
    else:
        base=int(base)
        s=input("numerale in base "+str(base)+": ")
        valore=0
        potenza=len(s)-1
        errore = False
        for c in s:
            if not (c.isdecimal() or c in "ABCDEF"):
                print('inserito un numerale errato per la base')
                errore=True
                break
            if c in "ABCDEF":
                c = ord(c)-ord("A")+10
            else:
                c=int(c)
            if not (0<=c<base):
                print('inserito un numerale errato per la base')
                errore = True
                break
            valore=valore+c*base**potenza
            potenza=potenza-1
        if not errore:
            print(s,"vale",valore)
    #------------
    s1=input("----Finisco (si/no)? ")
    finito=s1.lower()=="si"
