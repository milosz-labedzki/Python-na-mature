def suma_cyfr(n):
    wynik = 0
    while(n > 0):
          liczba = n % 10
          n = n//10
          wynik += liczba
    return wynik

print (suma_cyfr(9875))