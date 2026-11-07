tablica = []
with open("liczby.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = int(line)
        tablica.append(line)

def nwd_iter(a,b):
    dzielnik = 0
    while(a%b != 0):
        dzielnik = a % b
        a = b
        b = dzielnik
    return b


def ile_par(lista):
    liczba = 0
    dlugosc = len(lista)
    for i in range(0,dlugosc):
        for j in range(i+1,dlugosc):
            if(nwd_iter(lista[i],lista[j]))==1:
                liczba += 1
    return liczba
wynik = ile_par(tablica)
with open("wyniki2.txt","w",encoding="UTF-8") as t:
    t.write(f"{wynik}")




