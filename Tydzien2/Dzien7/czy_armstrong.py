def czy_armstrong(n):
    liczba_poczatkowa = n
    dlugosc = 0
    wynik = 0
    liczba = n
    while(n > 0):
        n = n // 10
        dlugosc +=1

    while(liczba > 0):
        cyfra = liczba % 10
        wynik = wynik + pow(cyfra,dlugosc)
        liczba = liczba // 10
    return wynik == liczba_poczatkowa

wyniki = [n for n in range(1, 1000) if czy_armstrong(n)]
print(wyniki)
assert len(wyniki) == 13