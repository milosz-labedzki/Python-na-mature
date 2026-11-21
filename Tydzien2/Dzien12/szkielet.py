def NWD(a,b):
    dzielnik = 0
    while(a % b != 0):
        dzielnik = a % b
        a = b
        b = dzielnik
    return b



tablica = [12, 18, 8]
najlepsze = 0
najlepsze_i = 0
najlepsze_j = 0
for i in range(len(tablica)):
    for j in range(i + 1, len(tablica)):
        wynik = (NWD(tablica[i], tablica[j]))
        if(najlepsze < wynik): 
            najlepsze = wynik
            najlepsze_i = i
            najlepsze_j = j
print(najlepsze,najlepsze_i,najlepsze_j)    