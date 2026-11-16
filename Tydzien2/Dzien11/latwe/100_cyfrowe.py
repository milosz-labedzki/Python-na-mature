with open("latwe/liczby100.txt","r",encoding="UTF-8") as f:
    wynik = 0
    najwieksza = None
    for line in f:
        line = line.strip()
        line = int(line)
        if(najwieksza == None or najwieksza < line): najwieksza = line
        wynik += line
    dlugosc = len(str(wynik))

with open("latwe/wyniki1.txt","w",encoding="UTF-8") as t:
    t.write(f"a) {wynik}\nb) {najwieksza}\nc) {dlugosc}")