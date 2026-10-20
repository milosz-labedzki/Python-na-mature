def czy_palindrom_liczba(liczba):
    wynik = 0
    poczatkowa_liczba = liczba
    while(liczba != 0):
        a = liczba % 10
        liczba = liczba // 10
        wynik = wynik * 10 + a

    return poczatkowa_liczba == wynik



assert czy_palindrom_liczba(4) == True
assert czy_palindrom_liczba(0) == True
assert czy_palindrom_liczba(12321) == True
assert czy_palindrom_liczba(1221) == True
assert czy_palindrom_liczba(14) == False
assert czy_palindrom_liczba(40) == False


def czy_palindrom_tekst(s):
    tablica = []
    for i in s:
        tablica.append(i)
    dlugosc = len(tablica)
    for j in range(1,dlugosc+1):
        if(tablica[j-1] != tablica[-j]):
            return False
    return True

assert czy_palindrom_tekst("kajak") == True
assert czy_palindrom_tekst("abba") == True
assert czy_palindrom_tekst("") == True
assert czy_palindrom_tekst("abcd") == False