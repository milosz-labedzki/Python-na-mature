def nwd(a,b):
    dzielnik = 0
    while(b>0):
        dzielnik = a%b
        a = b
        b = dzielnik
    return a




def czy_pierwsza(n):
    if(n == 0 or n == 1): return False
    pierwiastek = n ** 0.5
    pierwiastek = int(pierwiastek)
    for i in range(2,pierwiastek+1):
        if(n%i==0):
            return False
    return True


assert nwd(48, 18) == 6
assert nwd(17, 5) == 1
assert nwd(100, 100) == 100
assert nwd(7, 21) == 7


assert czy_pierwsza(2) == True
assert czy_pierwsza(0) == False
assert czy_pierwsza(1) == False
assert czy_pierwsza(25) == False
assert czy_pierwsza(91) == False
assert czy_pierwsza(97) == True