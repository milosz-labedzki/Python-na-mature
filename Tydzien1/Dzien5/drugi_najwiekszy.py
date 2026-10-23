def drugi_najwiekszy(a):
    najwiekszy = 0
    kolejny_najwiekszy = 0
    dlugosc = len(a)
    for i in range(0,dlugosc):
        if(a[i] > najwiekszy):
            kolejny_najwiekszy = najwiekszy
            najwiekszy = a[i]
    
    if(kolejny_najwiekszy == 0):
        return None
    
    return kolejny_najwiekszy
print(drugi_najwiekszy([5, 5, 3]))