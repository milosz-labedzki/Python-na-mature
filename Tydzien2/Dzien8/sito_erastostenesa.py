tablica = []
def sito(n):
    for i in range(1,n+1):
        tablica.append(i)
    for j in tablica:
        wielokrotnosc = j*j
        tablica.pop(wielokrotnosc)
    return tablica
print(sito(20))