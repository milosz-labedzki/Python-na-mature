def drugi_najwiekszy(a):
    if(a == []):
        return None
    najwieksza = max(a)
    liczba = None
    dlugosc = len(a)
    for i in range(0,dlugosc):
        if(a[i] < najwieksza):
            if(liczba is None or liczba < a[i]):
                liczba = a[i]
    return liczba




assert drugi_najwiekszy([3, 1, 4, 1, 5]) == 4
assert drugi_najwiekszy([5, 5, 3]) == 3
assert drugi_najwiekszy([2, 2, 2]) is None
assert drugi_najwiekszy([7]) is None
assert drugi_najwiekszy([]) is None
assert drugi_najwiekszy([-1, -5, -3]) == -3
assert drugi_najwiekszy([1, 2]) == 1
