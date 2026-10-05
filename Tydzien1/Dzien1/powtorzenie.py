def maks_i_indeks(tablica):
    dlugosc = len(tablica)
    najwieksza = tablica[0]
    indeks = 0
    for i in range(0,dlugosc):
        if(tablica[i]>najwieksza):
            najwieksza = tablica[i]
            indeks = i
    return najwieksza,indeks


assert maks_i_indeks([4, 9, 9, 1]) == (9, 1)
assert maks_i_indeks([-5, -2, -7]) == (-2, 1)
assert maks_i_indeks([3, 8, 10]) == (10, 2)
assert maks_i_indeks([5]) == (5, 0)