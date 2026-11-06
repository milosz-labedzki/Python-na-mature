def nwd_iter(a,b):
    dzielnik = 0
    while(a%b != 0):
        dzielnik = a % b
        a = b
        b = dzielnik
    return b

def dodaj(a,b,c,d):
    licznik = (a*d)+(b*c)
    mianownik = b * d
    najwiekszy = nwd_iter(licznik,mianownik)
    if(najwiekszy == 1):
        return licznik,mianownik
    else:
        licznik = licznik // najwiekszy
        mianownik = mianownik // najwiekszy
        return licznik,mianownik
    
