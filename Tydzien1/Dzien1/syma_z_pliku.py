def suma_z_pliku(nazwa):
    wynik = 0
    with open(nazwa,"r",encoding="UTF-8") as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            line = int(line)
            wynik += line
    return wynik


assert suma_z_pliku("liczby.txt") == 30