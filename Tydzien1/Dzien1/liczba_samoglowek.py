def liczba_samoglosek(zdanie):
    liczba = 0
    zdanie = zdanie.lower()
    for i in zdanie:
        if i=="a" or i == "e"  or i == "i" or i == "o" or i == "u" or i == "y":
            liczba += 1
    return liczba


assert liczba_samoglosek("Ala ma kota") == 5
assert liczba_samoglosek("matura") == 3
assert liczba_samoglosek("bcd") == 0
assert liczba_samoglosek("") == 0
assert liczba_samoglosek("EGON UMY OKNO") == 6