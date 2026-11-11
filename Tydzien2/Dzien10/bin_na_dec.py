licznik = 0
def bin_na_dec(s):
    wynik = 0
    liczba = 0
    dlugosc = len(s)
    line_odwrot = s[::-1]
    for i in range(dlugosc-1,-1,-1):
        if(line_odwrot[i] == '1'):
            liczba = (2 ** i)
            wynik += liczba
        if(wynik > 500):
             return 1
    


with open("bin.txt", "r",encoding="UTF-8") as f:
        for line in f:
            line = line.strip()
            licznik += bin_na_dec(line)
            with open("wyniki2.txt","w",encoding="UTF-8") as t:
                t.write(f"a) {licznik}")


