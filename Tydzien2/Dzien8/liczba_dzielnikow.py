def liczba_dzielnikow(n):
    licznik = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            if(d * d == n):licznik += 1
            else: licznik += 2
        d += 1
    return licznik


