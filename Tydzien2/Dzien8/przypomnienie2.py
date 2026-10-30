def tylko_raz(a):
    zliczenia = {}
    tablica = []
    dlugosc = len(a)
    for i in range(0, dlugosc):
        zliczenia[a[i]] = zliczenia.get(a[i],0) + 1

    for j in zliczenia:
        if(zliczenia[j] == 1):
            tablica.append(j)
    return tablica



assert(tylko_raz([1,2,2,3,1,4])) == [3,4]
assert(tylko_raz([9])) == [9]
assert(tylko_raz([5,5])) == []
assert(tylko_raz([])) == []