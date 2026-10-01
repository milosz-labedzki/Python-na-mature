najwieksza = 0 jako start → dla samych ujemnych liczb maksimum nigdy się nie zaktualizuje → pierwszy element listy jest punktem startowym (lista[0]) → assert z [-5, -2, -7].


range(0, dlugosc-1) → ostatni element nigdy nie jest sprawdzany → range(n) daje indeksy 0..n-1, więc nie odejmuj 1 → assert z maksimum na końcu listy, np. [1, 2, 9].


indeks bez wartości początkowej → UnboundLocalError, gdy warunek nigdy się nie spełni → zmienne wynikowe inicjalizuj przed pętlą → assert z jednoelementową listą [5].


{} zamiast () → zbiór zamiast krotki, gubi kolejność i duplikaty → krotka to (a, b) → assert ... == (8, 1).