def obroc_liste(a,k):
    tablica = []
    dlugosc = len(a)
    if(dlugosc == 0):
        dlugosc = 1
    while(k > dlugosc):
        k = k - dlugosc
    wycinek = a[-k:]
    reszta = a[:-k]
    tablica = wycinek + reszta
    return tablica



assert obroc_liste([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert obroc_liste([1, 2, 3], 0) == [1, 2, 3]
assert obroc_liste([1, 2, 3], 3) == [1, 2, 3]
assert obroc_liste([1, 2, 3], 4) == [3, 1, 2]
assert obroc_liste([], 5) == []