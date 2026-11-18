def dodaj(a,b):
    suma = 0
    result = ""
    przeniesienie = 0

    dlugosc = max(len(a),len(b))
    dlugosc_a = dlugosc-len(a)
    dlugosc_b = dlugosc-len(b)
    a = a[::-1]
    b=b[::-1]
    a = a+'0'*dlugosc_a
    b = b+'0'*dlugosc_b
    for i in range(0,dlugosc):
        suma = int(a[i]) + int(b[i]) + przeniesienie
        przeniesienie = suma // 10
        result += str(suma%10)

    if(przeniesienie > 0):result += str(przeniesienie)
    result = result[::-1]
    return result


with open("srednie/pary.txt","r",encoding="UTF-8") as f:
    
    wynik = 0
    licznik = 0

    for line in f:
        line = line.strip()
        line = line.split(" ")
        pierwsza = line[0]
        druga = line[1]
        dlugosc = max(len(pierwsza),len(druga))
        wynik = dodaj(pierwsza,druga)

        if(len(wynik) == dlugosc+1): licznik +=1

with open("srednie/wyniki2.txt","w",encoding="UTF-8") as t:
    t.write(f"a) {licznik}")