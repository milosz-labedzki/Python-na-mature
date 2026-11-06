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
    
assert dodaj(1, 2, 1, 3) == (5, 6)
assert dodaj(1, 6, 1, 3) == (1, 2)
assert dodaj(2, 3, 1, 6) == (5, 6)
assert dodaj(1, 2, 1, 2) == (1, 1)
assert dodaj(0, 1, 3, 4) == (3, 4)