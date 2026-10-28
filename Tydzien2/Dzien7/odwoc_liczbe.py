def odwroc_liczbe(n):
    nowa_liczba = 0
    while(n != 0):
        liczba = n % 10
        n = n // 10
        nowa_liczba = nowa_liczba * 10 + liczba
    return nowa_liczba


print(odwroc_liczbe(123))