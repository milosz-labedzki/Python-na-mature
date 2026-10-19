def ile_cyfr(n):
    wynik =0
    if(n == 0):
        return 1
    while(n != 0):
        n = n // 10
        wynik += 1
    return wynik


assert ile_cyfr(3) == 1
assert ile_cyfr(31) == 2
assert ile_cyfr(4567) == 4
assert ile_cyfr(120) == 3
assert ile_cyfr(0) == 1