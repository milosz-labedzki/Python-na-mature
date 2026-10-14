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


            



