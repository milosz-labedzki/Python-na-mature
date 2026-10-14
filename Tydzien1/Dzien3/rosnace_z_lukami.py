lista = []
ciag = []
najdluzszy = []

with open("dane2.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if(line == ''):
            continue
        line = int(line)
        lista.append(line)
    dlugosc = len(lista)
    najdluzszy.append(lista[0])

    for i in range(0,dlugosc-1):
        ciag.append(lista[i])
        print (ciag)
        if(lista[i] < lista[i+1]):
            ciag.append(lista[i+1])
        if(len(ciag) > len(najdluzszy)):
            najdluzszy = ciag
        if(lista[i] >= lista[i+1]):
            ciag = []
    najdluzszy = set(najdluzszy)
    najdluzszy = sorted(najdluzszy)
            

with open("wyniki2.txt","w",encoding="UTF-8") as f:
    f.write(f"{len(najdluzszy)} {najdluzszy[0]}")


