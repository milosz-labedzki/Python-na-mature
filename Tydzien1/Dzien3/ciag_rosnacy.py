def najdluzszy_rosnacy(a):
    biezacy = 1
    najlepszy = 1
    dlugosc = len(a)
    poczatek_biezacego = a[0]
    poczatek_najlepszego = a[0]
    for i in range(0,dlugosc-1):
        if(a[i] < a[i+1]):
            biezacy += 1
            if(biezacy > najlepszy):
                najlepszy = biezacy
                poczatek_najlepszego = poczatek_biezacego
        else:
            biezacy = 1
            poczatek_biezacego = a[i+1]
    
    return najlepszy,poczatek_najlepszego



assert najdluzszy_rosnacy([3, 1, 2, 5, 7, 6, 8, 9, 2, 10]) == (4, 1)
assert najdluzszy_rosnacy([1, 2, 3, 4, 5]) == (5, 1)
assert najdluzszy_rosnacy([5, 4, 3]) == (1, 5)
assert najdluzszy_rosnacy([9, 10, 11]) == (3, 9)
assert najdluzszy_rosnacy([1, 2, 9, 3, 4]) == (3, 1)
assert najdluzszy_rosnacy([5, 1, 2, 3]) == (3, 1)
assert najdluzszy_rosnacy([1, 2, 2, 3]) == (2, 1)
assert najdluzszy_rosnacy([7]) == (1, 7)
assert najdluzszy_rosnacy([4, 5, 1, 2]) == (2, 4)