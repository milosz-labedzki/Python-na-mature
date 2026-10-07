def czy_pierwsza(n):
    if(n <= 1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True



assert czy_pierwsza(2) == True
assert czy_pierwsza(17) == True
assert czy_pierwsza(97) == True
assert czy_pierwsza(18) == False
assert czy_pierwsza(25) == False
assert czy_pierwsza(1) == False
assert czy_pierwsza(0) == False
assert czy_pierwsza(-5) == False
assert czy_pierwsza(3) == True