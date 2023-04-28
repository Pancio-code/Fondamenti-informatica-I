f=open("A_Ex5.py", "r", encoding="UTF-8")
fout=open("A_Ex5_bis.py", "w", encoding="UTF-8")
for riga in f:
    print (riga.replace("\n",""),file=fout)
f.close()
fout.close()

