def tylko_raz(tablica):
    zliczenia = {}
    tabela = []
    for a in tablica:
        zliczenia[a] = zliczenia.get(a,0) + 1


    for k in tablica:
        if(zliczenia[k]) == 1:
            tabela.append(k)
    return tabela

assert tylko_raz([1, 2, 2, 3, 3, 3, 4]) == [1, 4]
assert tylko_raz([5, 5, 5]) == []
assert tylko_raz([4, 1, 4, 2]) == [1, 2]
assert tylko_raz([]) == []
assert tylko_raz([9]) == [9]