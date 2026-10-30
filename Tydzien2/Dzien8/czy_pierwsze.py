def czy_pierwsza(n):
    if(n < 2):
        return False
    pierwiastek = n ** 0.5
    pierwiastek = int(pierwiastek)
    for i in range(2,pierwiastek+1):
        if(n % i == 0):
            return False
    return True

assert(czy_pierwsza(1)) == False
assert(czy_pierwsza(2)) == True
assert(czy_pierwsza(3)) == True
assert(czy_pierwsza(4)) == False
assert(czy_pierwsza(49)) == False
assert(czy_pierwsza(91)) == False
assert(czy_pierwsza(97)) == True