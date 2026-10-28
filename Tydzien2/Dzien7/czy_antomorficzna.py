def czy_automorficzna_a(n):
    kwadrat = pow(n,2)
    return str(kwadrat).endswith(str(n))








































def czy_automorficzna_b(n):
    liczba = n
    dlugosc = 0
    wynik = 0
    odwrocony_wynik = 0
    liczba_odwrot = 0 
    while(n>0):
        dlugosc += 1
        n = n//10

    liczba_pow = pow(liczba,2)

    while(dlugosc != 0):
        ostatni_pow = liczba_pow % 10
        liczba_pow = liczba_pow // 10
        dlugosc -= 1
        wynik = wynik * 10 + ostatni_pow

    while(wynik > 0):
        liczba_odwrot = wynik % 10
        wynik = wynik // 10
        odwrocony_wynik = odwrocony_wynik * 10 + liczba_odwrot

    return (liczba == odwrocony_wynik)




a = [n for n in range(1, 1000) if czy_automorficzna_a(n)]
b = [n for n in range(1, 1000) if czy_automorficzna_b(n)]
assert a == b
assert len(a) == 7

