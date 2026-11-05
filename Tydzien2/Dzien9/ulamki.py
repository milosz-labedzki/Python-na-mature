with open("ulamki.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()  
        line = line.split('/') 
        print (line[0], line[1])
        dzielnik = 0
        liczba1 = int(line[0])
        liczba2 = int(line[1])
        print(liczba1,liczba2)

        # while(line[1]%line[0] != 0):
        #     dzielnik = line[1]%line[0]
        #     a = line[1]
        #     b = dzielnik
        # x = line[0] // b
        # y = line[1] // a
    # print(x,y)
