def nwd_iter(a,b):
    dzielnik = 0
    while(a%b != 0):
        dzielnik = a % b
        a = b
        b = dzielnik
    return b

def dodaj(a,b,c,d):
    licznik = (a*d)+(b*c)
    mianownik = b * d
    najwiekszy = nwd_iter(licznik,mianownik)
    if(najwiekszy == 1):
        return licznik,mianownik
    else:
        licznik = licznik // najwiekszy
        mianownik = mianownik // najwiekszy
        return licznik,mianownik
    

licznik_sumy = 0
mianownik_sumy = 1
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
            licznik_sumy,mianownik_sumy = dodaj(licznik_sumy,mianownik_sumy,liczba1,liczba2)
            t.write(f"{liczba1}/{liczba2}\n")
        suma = (f"{licznik_sumy}/{mianownik_sumy}")
        t.write(f"{suma}")

