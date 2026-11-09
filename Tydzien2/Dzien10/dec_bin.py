wynik = 0
def dec_na_bin(n):
    if(n == 0 or n == 1): return str(n)
    liczba = n%2
    n = n//2
    if(liczba%2==1):
        wynik += 1
    wynik += dec_na_bin(n)
    return wynik

print(dec_na_bin(13))