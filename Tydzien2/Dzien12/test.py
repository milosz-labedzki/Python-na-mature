def pierwsze(a):
    if(a < 2):  return 'nie'

    pierwiastek = a ** 0.5
    pierwiastek = int(pierwiastek)


    for i in range(2,pierwiastek+1):
        if(a % i == 0): return 'nie'
        

    
    return 'tak'



def czy_palindrom_bin(b):
    binarna = ""
    while(b != 0):
        reszta = b % 2
        b = b // 2
        binarna += str(reszta)

    return binarna




def NWD(a,b):
    dzielnik = 0
    while(a % b != 0):
        dzielnik = a % b
        a = b
        b = dzielnik
    return b     












with open("liczby.txt","r",encoding="UTF-8") as f:
    licznik1 = 0
    najwieksza1 = None
    
    
    licznik2 = 0
    najwieksza2 = None

    for line in f:
        line = line.strip()
        line = int(line)
        wynik1 = (pierwsze(line))
        if(wynik1 == 'tak'):
            if(najwieksza1 == None or najwieksza1 < line):
                najwieksza1 = line

        if(wynik1 == 'tak'):licznik1 += 1


        wynik2 = czy_palindrom_bin(line)
        if(wynik2 == wynik2[::-1]): 
            licznik2 += 1
            if(najwieksza2 == None or najwieksza2 < line):
                najwieksza2 = line










with open("liczby3.txt","r",encoding="UTF-8") as f:
    tablica = []
    for linia in f:
        linia = linia.strip()
        linia = int(linia)
        tablica.append(linia)
    wynik3 = tablica[0]
    for i in range(1,len(tablica)):
        wynik3 = NWD(wynik3,tablica[i])

    najlepsze = 0
    najlepsze_i = 0
    najlepsze_j = 0
for i in range(len(tablica)):
    for j in range(i + 1, len(tablica)):
        wynik = (NWD(tablica[i], tablica[j]))
        if(najlepsze < wynik): 
            najlepsze = wynik
            najlepsze_i = i
            najlepsze_j = j
 


with open("wyniki.txt","w",encoding="UTF-8") as t:
    t.write(f"1a) {licznik1}\n1b) {najwieksza1}\n2a) {licznik2}\n2b) {najwieksza2} {czy_palindrom_bin(najwieksza2)} \n3a) {wynik3}\n3b) {najlepsze_i + 1} {najlepsze_j + 1} {najlepsze}")