def pierwsze(a):
    if(a < 2):  return 'nie'

    pierwiastek = a ** 0.5
    pierwiastek = int(pierwiastek)


    for i in range(2,pierwiastek+1):
        if(a % i == 0): return 'nie'
        

    
    return [najwieksza,'tak']



with open("liczby.txt","r",encoding="UTF-8") as f:
    licznik = 0
    najwieksza = None

    for line in f:
        line = line.strip()
        line = int(line)
        wynik = (pierwsze(line))
        print(wynik)

        if(najwieksza == None or najwieksza < wynik[1]):
            najwieksza = wynik[1]

        if(wynik[1] == 'tak'):licznik += 1


with open("wyniki.txt","w",encoding="UTF-8") as t:
    t.write(f"a) {licznik}\nb) {wynik[0]}")