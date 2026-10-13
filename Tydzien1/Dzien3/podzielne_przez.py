wynik = 0
with open("dane.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = int(line)
        if(line % 5 == 0 or line % 3 == 0):
            wynik += 1
with open("wyniki.txt","w",encoding="UTF-8") as f:
    f.write(f"{wynik}")