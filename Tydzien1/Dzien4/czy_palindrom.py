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
    for i in s:     
        while(i == i[-1]):
            print("to palindrom")
        return True
    return False

print (czy_palindrom_tekst("kajak"))