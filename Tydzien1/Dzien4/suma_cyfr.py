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