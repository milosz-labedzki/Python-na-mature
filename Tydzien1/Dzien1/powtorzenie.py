def suma_z_pliku(nazwa):
    with open(nazwa,"r",encoding="UTF-8") as f:
        wynik = 0
        for line in f:
            line = line.strip()
            if(line == ''):
                continue
            line=int(line)
            wynik += line
    return wynik

assert suma_z_pliku("liczby.txt") == 30