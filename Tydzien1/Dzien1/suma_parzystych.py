def suma_parzystych(n):
    liczba = 0
    for i in range(0,n+1):
        if(i%2==0):
            liczba += i
    return liczba

assert suma_parzystych(10) == 30
assert suma_parzystych(7) == 12
assert suma_parzystych(1) == 0