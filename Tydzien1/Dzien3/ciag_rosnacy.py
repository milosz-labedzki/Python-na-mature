def najdluzszy_rosnacy(tabelka):
    biezacy = 0
    najlepszy = 0
    dlugosc = len(tabelka)
    for i in range(0,dlugosc-1):
        if(tabelka[i] < tabelka[i+1]):
            biezacy += 1
            if(biezacy > najlepszy):
                najlepszy = biezacy
        else:
            biezacy = 1
    return najlepszy



print (najdluzszy_rosnacy([2, 5, 6, 7, 1, 3, 4]))
# assert najdluzszy_rosnacy([2, 5, 6, 7, 1, 3, 4]) == 4
# assert najdluzszy_rosnacy([1, 2, 3, 1, 2, 1, 2, 3, 4]) == 4
# assert najdluzszy_rosnacy([5, 4, 3]) == 1
# assert najdluzszy_rosnacy([7]) == 1