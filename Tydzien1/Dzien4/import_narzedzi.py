from narzedzia import (suma_cyfr,czy_palindrom_liczba)
with open("liczby.txt" ,"r", encoding="UTF-8") as f:
    for line in f:
        wynik = 0
        line = line.strip()
        if(line == ''):
            continue
        line = int(line)
        if(suma_cyfr(line) == 10 and czy_palindrom_liczba(line) == True):
            wynik +=1

with open("wyniki4.txt","w",encoding="UTF-8") as f:
    f.write(f"{wynik}")
