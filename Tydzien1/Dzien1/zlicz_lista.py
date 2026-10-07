def zlicz(lista):
    zliczenia = {}
    dlugosc = len(lista)
    for i in range(0,dlugosc):
        zliczenia[lista[i]] = zliczenia.get(lista[i],0) + 1
    return zliczenia



assert zlicz([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
assert zlicz(["a", "b", "a"]) == {"a": 2, "b": 1}
assert zlicz([7]) == {7: 1}
assert zlicz([]) == {}