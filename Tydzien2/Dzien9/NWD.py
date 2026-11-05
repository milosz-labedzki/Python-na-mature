def nwd_iter(a,b):
    dzielnik = 0
    while(a%b != 0):
        dzielnik = a % b
        a = b
        b = dzielnik
    return b

assert nwd_iter(84, 30) == 6
assert nwd_iter(105, 42) == 21
assert nwd_iter(17, 5) == 1
assert nwd_iter(12, 12) == 12
assert nwd_iter(7, 21) == 7
assert nwd_iter(1000000, 999999) == 1