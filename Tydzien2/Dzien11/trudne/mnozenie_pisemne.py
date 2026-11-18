def pomnoz(a,c):
    if(c == 0): return '0'

    dlugosc = len(a)
    suma = 0
    wynik = ""
    reszta = 0

    for i in range(dlugosc-1,-1,-1):
        suma = int(a[i]) * c + reszta
        reszta = 0

        reszta = suma // 10
        suma = suma %10

        wynik += str(suma)
    if(reszta !=0):
        wynik += str(reszta)
    return wynik[::-1]




with open("trudne/liczby5.txt","r",encoding="UTF-8") as f:
    wartosc = 0
    licznik = 0
    najwieksza = None
    for line in f:
        line = line.strip()
        if(line == ''):continue

        if(najwieksza == None or len(najwieksza) < len(line)):najwieksza = line
        if(len(najwieksza) == len(line)):
            najwieksza = max(najwieksza,line)

        dlugosc1 = len(line)
        wartosc = pomnoz(line,5)
        dlugosc2 = len(wartosc)

        if(dlugosc2 > dlugosc1):licznik +=1

with open("trudne/wyniki5.txt","w",encoding="UTF-8") as t:
    t.write(f"a) {licznik} \nb) {najwieksza}")