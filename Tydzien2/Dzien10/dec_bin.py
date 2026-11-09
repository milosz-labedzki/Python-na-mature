# wynik = ""
# def dec_na_bin(n):
#     if(n == 0 or n == 1): return str(n)
#     liczba = n%2
#     n = n//2
#     if(liczba%2==1):
#         wynik += '1'
#     wynik += dec_na_bin(n)
#     return wynik

# print(dec_na_bin(13))


def dec_na_bin(n):
    wynik = ""
    liczba = 0
    if(n == 0 or n == 1): return str(n)
    while(n!=0):
        liczba = n % 2
        n = n // 2
        if(liczba == 1):
            wynik += "1"
        else:
            wynik += "0"
    koncowy_wynik = wynik[::-1]
    return koncowy_wynik
print(dec_na_bin(13))