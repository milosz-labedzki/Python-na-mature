def drugi_najwiekszy_1p(a):
    najwiekszy = None
    kolejny_najwiekszy = None
    dlugosc = len(a)
    for i in range(0,dlugosc):

        if(najwiekszy is None or a[i] > najwiekszy):
            kolejny_najwiekszy = najwiekszy
            najwiekszy = a[i]

    
        if(a[i] < najwiekszy):
            if( kolejny_najwiekszy is None or kolejny_najwiekszy < a[i]):
                kolejny_najwiekszy = a[i]
            

    return kolejny_najwiekszy


assert drugi_najwiekszy_1p([3, 1, 4, 1, 5]) == 4
assert drugi_najwiekszy_1p([5, 5, 3]) == 3
assert drugi_najwiekszy_1p([2, 2, 2]) is None
assert drugi_najwiekszy_1p([7]) is None
assert drugi_najwiekszy_1p([]) is None
assert drugi_najwiekszy_1p([-1, -5, -3]) == -3
assert drugi_najwiekszy_1p([1, 2]) == 1

