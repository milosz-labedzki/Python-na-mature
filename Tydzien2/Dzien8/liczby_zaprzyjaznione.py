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

for a in range(2,10001):
    b = suma_dzielnikow_szybka(a)
    if(b>a):
        if(suma_dzielnikow_szybka(b) == a):
            print(a,b)
