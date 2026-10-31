def sito(n):
    tablica = n*[True]
    if(tablica[n] <2):
         tablica[n] = False
      
    for i in range(2, n + 1):
        if(tablica[i]==False): continue
        while(i<=n):
               i += i
               if(i<11):
                  tablica[i] = False
    return tablica


print(sito(5))