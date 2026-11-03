tablica = []
def suma_dzielnikow(n):
    p = 1
    suma_dziel = 0 
    while(p<n):
        if(n%p==0):
            suma_dziel += p
        p+=1
    return suma_dziel




def suma_dzielnikow_szybka(n):
    if(n == 1): return 0
    d = 0
    para = 0
    suma = 0
    pierwiastek = n**0.5
    pierwiastek = int(pierwiastek)
    for i in range(1,pierwiastek+1):
        if(n%i==0): 
            d = i
            para =  n // d
            if(para == n): para = 0
            if(para == d): para = 0
            suma += d+para
    return suma

for n in range(2, 10000):
    if(suma_dzielnikow_szybka(n)==n):tablica.append(n) 
print(tablica)

