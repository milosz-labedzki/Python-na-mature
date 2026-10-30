def suma_rowna_iloczynowi(n):
    suma = 0
    iloczyn = 1
    if(n == 0):
        return True
    while(n > 0):
        liczba = n % 10
        n = n //10
        suma += liczba
        iloczyn *= liczba
    return suma == iloczyn

print(suma_rowna_iloczynowi(0))