def nwd_rek(a,b):
    if(b>0):
        dzielnik = a%b
        a = b
        b = dzielnik
        return nwd_rek(a,b)
    return a

print(nwd_rek(84,30))