with open("latwe/dec.txt","r",encoding="UTF-8") as f:
    wynik5 = 0
    najwieksza = 0
    najwieksza_num = 0
    for line in f:
        wynik = ""
        liczba = 0
        liczba5 = 0
        line = line.strip()
        if(line == ''): continue
        line = int(line)

        if(line > najwieksza_num):
            najwieksza_num = line

        if(line == 0 or line == 1):print (str(line))
        while(line!=0):
                liczba = line % 2
                line = line // 2
                if(liczba == 1):
                    wynik += "1"
                    liczba5 += 1
                else:
                    wynik += "0"
                
        if(liczba5==5):
            wynik5 += 1
        koncowy_wynik = wynik[::-1]

        if(int(koncowy_wynik) > najwieksza):
             najwieksza = int(koncowy_wynik)





with open("latwe/wyniki1.txt","w",encoding="UTF-8") as l:
     l.write(f"a){wynik5} \nb){najwieksza_num} {najwieksza}")






  
        