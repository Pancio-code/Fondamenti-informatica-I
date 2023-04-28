def isintero(s):
    if len(s) > 0 and (s.isdecimal() or (s[0] in '+-' and s[1:].isdecimal())):
        return True
    else:
        return False

def isreale(s):
    if isintero(s):
        return True
    k = s.find('.')
    if k == -1:
        return False
    intera = s[0:k]
    decimale = s[k+1:]
    if isintero(intera) and decimale.isdecimal():
        return True
    else:
        return False
