def maks_i_indeks(lista):
    dlugosc = len(lista)
    indeks = 0
    najwieksza = lista[0]
    for i in range(0,dlugosc):
        if lista[i] > najwieksza:
            najwieksza = lista[i]
            indeks = i
    return(najwieksza, indeks)


assert maks_i_indeks([3, 8, 2]) == (8, 1)
assert maks_i_indeks([5]) == (5, 0)
assert maks_i_indeks([4, 9, 9, 1]) == (9, 1)
assert maks_i_indeks([-5, -2, -7]) == (-2, 1)