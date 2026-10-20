def suma_cyfr(n):
    suma = 0
    while(n != 0):
        liczba = n % 10
        n = n // 10
        suma += liczba
    return suma


assert suma_cyfr(5) == 5
assert suma_cyfr(12) == 3
assert suma_cyfr(1531) == 10
assert suma_cyfr(0) == 0



def odwroc_liczbe(n):
    wynik = 0

    while(n != 0):
        liczba = n % 10
        n = n // 10
        wynik = wynik * 10 + liczba

    return wynik


assert odwroc_liczbe(3) == 3
assert odwroc_liczbe(31) == 13
assert odwroc_liczbe(4567) == 7654
assert odwroc_liczbe(120) == 21
assert odwroc_liczbe(0) == 0




def ile_cyfr(n):
    wynik =0
    if(n == 0):
        return 1
    while(n != 0):
        n = n // 10
        wynik += 1
    return wynik


assert ile_cyfr(3) == 1
assert ile_cyfr(31) == 2
assert ile_cyfr(4567) == 4
assert ile_cyfr(120) == 3
assert ile_cyfr(0) == 1





def czy_palindrom_liczba(liczba):
    poczatkowa_liczba = liczba
    liczba_odwrot = odwroc_liczbe(liczba)

    return poczatkowa_liczba == liczba_odwrot



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
assert czy_palindrom_tekst("a") == True