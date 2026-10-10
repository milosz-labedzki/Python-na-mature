ile_liczb = 0
ujemne = 0
with open("dane.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if(line == ''):
            continue
        line = line.split()
        for i in line:
            i = int(i)
            ile_liczb += 1
            if(i<0):
                ujemne += 1
with open("wyniki.txt","w",encoding="UTF-8") as f:
    f.write(f"a) wszystkich liczb jest: {ile_liczb} \nb) ujemnych jest: {ujemne}")




