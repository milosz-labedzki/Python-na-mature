lista = []
wynik = 1
ciag = []
najdluzszy = 1
with open("dane2.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if(line == ''):
            continue
        lista.append(line)
    dlugosc = len(lista)
    
    for i in range(1,dlugosc):
        if(lista[i-1] < lista[i]):
            ciag.append(lista[i])
        else:
            if(len(ciag) > najdluzszy):
                najdluzszy = len(ciag)
                print(najdluzszy)
            ciag = []

# with open("wyniki2.txt","w",encoding="UTF-8") as f:
#     f.write(f"{len(najdluzszy)} {najdluzszy[0]}")


