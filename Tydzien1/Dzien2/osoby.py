lista = []
wartosc = 0
wynik = 0
with open("osoby.csv","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = line.split(";")
        if(line[1] == 'wiek'):
            continue
        wiek = int(line[1])
        wartosc += wiek
        lista.append(wiek)
    dlugosc = len(lista)
    srednia = wartosc/dlugosc
    for lata in range(0,dlugosc):
        if(lista[lata]>srednia):
            wynik += 1

with open("wyniki.txt","w",encoding="UTF-8") as f:
    f.write(f"srednia wieku to: {srednia} a liczba osob starszych to: {wynik} \n")