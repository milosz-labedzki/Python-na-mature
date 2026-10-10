liczby = []
suma = 0
with open("liczby.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if(line == ''):
            continue
        line = int(line)
        suma += line
        liczby.append(line)

    dlugosc = len(liczby)
    najwieksza = liczby[0]
    najmniejsza = liczby[0]
    for i in range(1,dlugosc):
        liczba = liczby[i]

        if(liczba > najwieksza):
            najwieksza = liczba

        if(liczba < najmniejsza):
            najmniejsza = liczba
            
    srednia = suma/dlugosc

print(suma)
print(srednia)
print(najwieksza)
print(najmniejsza)