def nwd_iter(a,b):
    dzielnik = 0
    while(a%b != 0):
        dzielnik = a % b
        a = b
        b = dzielnik
    return b

with open("wyniki.txt","w",encoding="UTF-8") as t:
    with open("ulamki.txt","r",encoding="UTF-8") as f:  
        for line in f:
            line = line.strip()  
            line = line.split('/') 
            liczba1 = int(line[0])
            liczba2 = int(line[1])
            b = nwd_iter(liczba1,liczba2)
            liczba1 = liczba1 // b
            liczba2 = liczba2 // b
            t.write(f"{liczba1}/{liczba2}\n")
                