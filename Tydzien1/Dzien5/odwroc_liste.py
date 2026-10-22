def odwroc_liste(a):
    tablica = []
    dlugosc = len(a)
    for i in range(1,dlugosc+1):
        element = a[-i]
        tablica.append(element)
    return tablica


assert odwroc_liste([1, 2, 3]) == [3, 2, 1]
assert odwroc_liste([7]) == [7]
assert odwroc_liste([]) == []