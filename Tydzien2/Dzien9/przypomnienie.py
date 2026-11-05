def czy_pierwsza(n):
    if(n < 2): return False

    pierwiastek = n ** 0.5
    pierwiastek = int(pierwiastek)
    for i in range(2,pierwiastek+1):
        if(n%i==0): return False
    return True

assert czy_pierwsza(2) == True
assert czy_pierwsza(1) == False
assert czy_pierwsza(25) == False
assert czy_pierwsza(97) == True


def suma_cyfr(n):
    liczba = 0
    suma = 0
    while(n!=0):
        liczba = n % 10
        n = n//10
        suma += liczba
    return suma


assert suma_cyfr(0) == 0
assert suma_cyfr(7) == 7
assert suma_cyfr(472) == 13
assert suma_cyfr(1000) == 1
assert suma_cyfr(99999) == 45