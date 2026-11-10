with open("bin.txt", "r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        dlugosc = len(line)
        for i in range(dlugosc,0,-1):
            print(line[i])
            # if(line[i]=="1"):
            #     print("dasasd")
