ile_osob = 0
zliczenia = {}
najsatrsza = 0
najstarsi = []
with open("dane.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if(line == ''):
            continue
        line = line.split(';')
        zliczenia[line[2]] = zliczenia.get(line[2],0) + 1
        wiek = int(line[1])
        if(najsatrsza < wiek):
            najsatrsza = wiek
            najstarsi.append(najsatrsza)
        if(najsatrsza == wiek):
            najstarsi.append(najsatrsza)
            

print (f"{zliczenia} najstarsi są {najstarsi}")