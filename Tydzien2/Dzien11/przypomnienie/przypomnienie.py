def na_baze(n,p):
    wynik = ""
    if(n == 0): return '0'
    while(n!=0):
        liczba = n % p
        n = n // p
        if(liczba == 10): liczba = 'A'
        if(liczba == 11): liczba = 'B'
        if(liczba == 12): liczba = 'C'
        if(liczba == 13): liczba = 'D'
        if(liczba == 14): liczba = 'E'
        if(liczba == 15): liczba = 'F'
        liczba = str(liczba)
        wynik += liczba
    wynik = wynik[::-1]
    return wynik



assert na_baze(0, 7) == '0'
assert na_baze(100, 5) == '400'
assert na_baze(31, 16) == '1F'
assert na_baze(1000, 2) == '1111101000'