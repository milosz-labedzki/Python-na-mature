def sito(n):
    tablica = (n+1)*[True]
    tablica[0] = False
    tablica[1] = False
    pierwsze = []
    for i in range(2, n + 1):
        if(tablica[i]==False): continue
        p = i
        while(p<=n):
               p += i
               if(p<=n):
                  tablica[p] = False
    for j in range(2,n+1):
         if(tablica[j] != False):
              pierwsze.append(j)
    return pierwsze


assert sito(10) == [2, 3, 5, 7]
assert sito(2) == [2]
assert sito(1) == []
assert sito(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]