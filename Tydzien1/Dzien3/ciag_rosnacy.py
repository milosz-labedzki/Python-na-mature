def najdluzszy_rosnacy(a):
    biezacy = 1
    najlepszy = 1
    dlugosc = len(a)
    for i in range(0,dlugosc-1):
        if(a[i] < a[i+1]):
            biezacy += 1
            if(biezacy > najlepszy):
                najlepszy = biezacy
        else:
            biezacy = 1
        pierszy_lepszy = a[0]
    
    return najlepszy,pierszy_lepszy



print (najdluzszy_rosnacy([7]))
# assert najdluzszy_rosnacy([2, 5, 6, 7, 1, 3, 4]) == 4
# assert najdluzszy_rosnacy([1, 2, 3, 1, 2, 1, 2, 3, 4]) == 4
# assert najdluzszy_rosnacy([5, 4, 3]) == 1
# assert najdluzszy_rosnacy([7]) == 1