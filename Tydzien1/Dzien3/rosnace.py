lista = []
najlepszy = 1
biezacy = 1
with open("dane2.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if(line == ''):
            continue
        line = int(line)
        lista.append(line)
    dlugosc = len(lista)

    pierwszy_biezacy = lista[0]
    pierwszy_najlepszy = lista[0]

    for i in range(0,dlugosc-1):
        if(lista[i] < lista[i+1]):
            biezacy += 1
            if(biezacy > najlepszy):
                najlepszy = biezacy
                pierwszy_najlepszy = pierwszy_biezacy
        else:
            biezacy = 1
            pierwszy_biezacy = lista[i+1]

with open("wyniki2.txt","w",encoding="UTF-8") as f:
    f.write(f"{najlepszy} {pierwszy_najlepszy}")