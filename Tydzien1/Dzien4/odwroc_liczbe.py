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