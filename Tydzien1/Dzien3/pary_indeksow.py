def liczba_par(a,k):
    dlugosc = len(a)
    pary = 0
    for i in range(0,dlugosc):
        for j in range(0,dlugosc):
            if(i<j and a[i]+a[j]==k):
                pary +=1

    return pary

assert liczba_par([3, 7, 5, 5, 2, 8], 10) == 3
assert liczba_par([1, 1, 1], 2) == 3
assert liczba_par([4, 6, 4, 6], 10) == 4
assert liczba_par([1, 2, 3], 10) == 0
assert liczba_par([5], 10) == 0
