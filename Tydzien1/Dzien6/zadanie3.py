najdluzszy = 1
biezacy = 1
tablica = []
with open("liczby.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if(line == ''):
            continue
        line = int(line)
        tablica.append(line)
    dlugosc = len(tablica)
    for i in range(1,dlugosc):
        if(tablica[i-1] < tablica[i]):
            biezacy += 1
            if(biezacy > najdluzszy):
                najdluzszy = biezacy
        else:
            biezacy = 1

print (najdluzszy)

