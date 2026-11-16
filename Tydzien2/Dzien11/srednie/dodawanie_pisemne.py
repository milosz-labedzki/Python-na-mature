def dodaj(a,b):
    dlugosc_a = len(a)
    dlugosc_b = len(b)
    if(len(a) > len(b)): 
        dluzszy = len(a)
        for i in range(dlugosc_b,dluzszy):
            b += '0'
        napis_b = b[::-1]
        return a,napis_b
    if(len(a) < len(b)): 
        dluzszy = len(b)
        for j in range(dlugosc_a,dluzszy):
            a += '0'
        napis_a = b[::-1]
        return napis_a,b
    


print(dodaj('123','20'))
# with open("srednie/pary.txt","r",encoding="UTF-8") as f:
#     pary = 0
#     for line in f:
#         line = line.strip()
#         line = line.split(' ')
#         wynik = dodaj(line[0],line[1])
#         dlugosc = len(wynik)
#         dluzszy = 0
#         if(len(line[0]) > len(line[1])): dluzszy = len(line[0])
#         if(len(line[0]) < len(line[1])): dluzszy = len(line[1])
#         if(dlugosc == dluzszy+1): pary +=1
#     print(pary)