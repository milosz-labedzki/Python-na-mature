def wiecej_zer(s):
    zera = 0
    jeden = 0
    dlugosc = len(s)
    for i in range(0,dlugosc): 
        if(s[i] == '1'):jeden+=1
        if(s[i] =='0' ):zera += 1 
    if(zera>jeden): return True
    return False


def bin_na_dec(s):
    wynik = 0  
    liczba = 0
    dlugosc = len(s)
    odwrocona = s[::-1]
    for i in range(dlugosc-1,-1,-1): 
        if(odwrocona[i] == '1'): 
            liczba = (2 ** i)
            wynik += liczba

    return wynik
    

with open("srednie/liczby_bin.txt","r",encoding="UTF-8") as f:
    licznik = 0
    liczenie = 0
    najwieksza = None
    for line in f:
        line = line.strip()
        wartosc = wiecej_zer(line)
        if(wartosc == True): licznik += 1
        wartosc2 = bin_na_dec(line)
        if(wartosc2 % 2 == 0): liczenie += 1

        if(najwieksza == None or najwieksza < wartosc2): najwieksza = wartosc2

with open("srednie/wyniki3.txt","w",encoding="UTF-8") as t:
    t.write(f"a) {liczenie}\nb) {najwieksza}\nc) {licznik}")

