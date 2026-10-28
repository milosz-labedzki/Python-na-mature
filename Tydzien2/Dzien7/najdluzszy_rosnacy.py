def najdluzszy_rosnacy(tablica):
    biezacy = 1
    najlepszy = 1
    dlugosc = len(tablica)
    for i in range(1,dlugosc):
        if(tablica[i-1] < tablica[i]):
            biezacy += 1
            if(biezacy > najlepszy):
                najlepszy = biezacy
        else:
            biezacy = 1
    return najlepszy

print(najdluzszy_rosnacy([1,2,3,2,6,1]))