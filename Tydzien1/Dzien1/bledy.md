# Dziennik błędów

## Z poprzedniej sesji (maks_i_indeks)

### 1. Maksimum startowało od `0`
- **Źle:** `najwieksza = 0`. Dla samych ujemnych liczb nic nie jest większe od `0`, więc maksimum się nie aktualizuje.
- **Dobrze:** start od pierwszego elementu: `najwieksza = lista[0]`, `indeks = 0`.
- **Test:** `[-5, -2, -7]` → `(-2, 1)`.

### 2. Pętla pomijała ostatni element
- **Źle:** `range(0, dlugosc-1)`. `range(n)` kończy się już na `n-1`, więc odejmowanie 1 ucina ostatni indeks.
- **Dobrze:** `range(dlugosc)`.
- **Test:** `[1, 2, 9]` → `(9, 2)`.

### 3. `indeks` bez wartości na starcie (2 razy)
- **Źle:** `indeks` ustawiany tylko w `if`. Gdy `if` się nie spełni, zmienna nie istnieje i jest `UnboundLocalError`.
- **Dobrze:** zmienne, które zwracam, ustawiam przed pętlą.
- **Test:** `[5]` → `(5, 0)`.

### 4. Zbiór `{}` zamiast krotki `()`
- **Źle:** `return {najwieksza, indeks}`. Zbiór gubi kolejność i powtórzenia, i nie jest równy krotce.
- **Dobrze:** `return (najwieksza, indeks)`.
- **Test:** `[3, 8, 2]` → `(8, 1)`.

## Dzisiaj

### 5. Licznik zadeklarowany poza funkcją
- **Źle:** `liczba = 0` stało nad funkcją, a w środku `liczba += i`. Python widzi `+=` jako zmienną lokalną bez wartości i rzuca błąd.
- **Dobrze:** `liczba = 0` w funkcji, przed pętlą.
- **Test:** `suma_parzystych(10) == 30`.

### 6. `=` zamiast `+=`
- **Źle:** `liczba = i` nadpisuje wynik w każdym obrocie, więc zostaje tylko ostatnie `i`.
- **Dobrze:** `liczba += i`, czyli dodawanie do tego, co już jest.
- **Test:** `suma_parzystych(10) == 30`.

### 7. Brak sprawdzenia parzystości
- **Źle:** dodawałem wszystkie liczby, wyszło `55` zamiast `30`.
- **Dobrze:** `if i % 2 == 0:` przed dodaniem.
- **Test:** `suma_parzystych(7) == 12`.

### 8. Tylko jedna wielka litera w warunku
- **Źle:** w warunku dopisałem `"A"`, ale nie `"E"`, `"U"` itd., więc duże litery były liczone źle.
- **Dobrze:** `zdanie = zdanie.lower()` przed pętlą, a w warunku zostają same małe litery.
- **Test:** `liczba_samoglosek("EGON UMY OKNO") == 6`.

### 9. `return` w środku `if` w pętli
- **Źle:** `return` natychmiast kończy funkcję, więc wyszła w pierwszej spełnionej iteracji. Dla `[3, 8, 10]` dało `(8, 1)`.
- **Dobrze:** `return` po pętli, na tym samym wcięciu co `for`.
- **Test:** `[3, 8, 10]` → `(10, 2)`.

### 10. Testowałem tylko przykłady tutora
- **Źle:** dwa asserty przeszły przypadkiem, a funkcja była błędna. Nie dopisałem też asserta, o który prosiłem.
- **Dobrze:** dopisuję własne przypadki graniczne: maksimum na początku, w środku, na końcu, lista jednoelementowa.
- **Test:** `[9, 1, 2]`, `[1, 9, 2]`, `[1, 2, 9]`, `[5]`.

### 11. Pusty wiersz w pliku wywalał `int()`
- **Źle:** `int(line)` na `""` rzuca `ValueError`. Pliki często mają pusty wiersz na końcu.
- **Dobrze:** `if line == '': continue` przed `int()`.
- **Test:** dopisz pusty wiersz do `liczby.txt`, suma dalej `30`.

### 12. Cyfry wyciągałem dzieleniem przez 2
- **Źle:** `n // 2` nie ma nic wspólnego z cyframi. Do tego `n % polowa` mogło dzielić przez zero.
- **Dobrze:** `n % 10` daje ostatnią cyfrę, `n // 10` ją odcina.
- **Test:** `123 % 10 == 3`, `123 // 10 == 12`.

### 13. Trzy kroki na sztywno zamiast pętli
- **Źle:** działało tylko do 3 cyfr. Dla `9999` wyszło `27`.
- **Dobrze:** `while n != 0:` i te same dwa kroki w środku.
- **Test:** `suma_cyfr(9999) == 36`.

### 14. Cyfrę odcinałem od złej zmiennej
- **Źle:** `n = liczba // 10`. `liczba` to już jedna cyfra, więc wynik to zawsze `0`.
- **Dobrze:** `n = n // 10`.
- **Test:** `suma_cyfr(123) == 6`, a nie `3`.