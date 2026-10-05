def suma_cyfr(n):
    wynik = 0
    liczba = 0
    while(n != 0):
        liczba = n % 10
        wynik += liczba
        n = n // 10


    return wynik


assert suma_cyfr(123) == 6
assert suma_cyfr(5) == 5
assert suma_cyfr(0) == 0
assert suma_cyfr(9999) == 36
assert suma_cyfr(100) == 1

