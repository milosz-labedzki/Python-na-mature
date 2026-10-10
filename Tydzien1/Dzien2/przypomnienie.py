def zlicz(napis):
    zliczenia = {}
    for i in napis:
        zliczenia[i] = zliczenia.get(i, 0) + 1
    return zliczenia

print (zlicz("banan"))