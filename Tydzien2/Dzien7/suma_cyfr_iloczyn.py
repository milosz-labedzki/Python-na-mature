def suma_rowna_iloczynowi(n):
    suma = 0
    iloczyn = 1
    while(n > 0):
        liczba = n%10
        n = n // 10
        suma += liczba
        iloczyn = iloczyn * liczba
    return suma == iloczyn

wyniki = [n for n in range(1, 1001) if suma_rowna_iloczynowi(n)]
print(wyniki)
assert len(wyniki) == 16
