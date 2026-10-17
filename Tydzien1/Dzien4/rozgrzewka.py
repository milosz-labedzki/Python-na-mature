biezacy = 1
najlepszy = 1
tablica = []
with open("dane.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if(line == ''):
            continue
        line = int(line)
        tablica.append(line)
    dlugosc = len(tablica)
pierwszy_biezacy = tablica[0]
pierwszy_najlepszy = tablica[0]

for i in range(0,dlugosc-1):
    if(tablica[i]<tablica[i+1]):
        biezacy += 1
        if(biezacy > najlepszy):
            najlepszy = biezacy
            pierwszy_najlepszy = pierwszy_biezacy
    else:
        biezacy = 1
        pierwszy_biezacy = tablica[i+1]

with open("wyniki.txt","w",encoding="UTF-8") as f:
    f.write(f"{najlepszy} {pierwszy_najlepszy}")

        