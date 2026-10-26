wynik = 0
najwieksza = 0
indeks = 0
with open("liczby.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if(line == ''):
            continue
        line = int(line)
        if(line % 2 == 0):
            wynik += 1
        indeks += 1
        if(line > najwieksza):
            najwieksza = line
            miejsce = indeks


print(wynik,najwieksza,miejsce)
        