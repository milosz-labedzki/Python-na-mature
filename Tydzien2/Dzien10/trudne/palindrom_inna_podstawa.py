def na_baze(n,p):
    wynik = ""
    if(n == 0): return '0'
    while(n != 0):
        reszta = n % p
        n = n // p
        if(reszta == 10): reszta = 'A'
        if(reszta == 11): reszta = 'B'
        if(reszta == 12): reszta = 'C'
        if(reszta == 13): reszta = 'D'
        if(reszta == 14): reszta = 'E'
        if(reszta == 15): reszta = 'F'
        reszta = str(reszta)
        wynik += reszta
    wynik = wynik[::-1]
    return wynik 

with open("liczby4.txt","r",encoding="UTF-8") as f:
    licznik_palindromow = 0
    najwyzszy_palindrom = None
    for line in f:
        line = line.strip()
        if(line == ''): continue
        palindrom = na_baze(line,2)

with open("wyniki4.txt","w",encoding="UTF-8") as t:
    t.write(f"a) {licznik_palindromow} \nb) {najwyzszy_palindrom}")
