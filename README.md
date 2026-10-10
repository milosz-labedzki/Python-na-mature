# Python pod maturę rozszerzoną z informatyki — plan na 30 dni

**Rytm:** 1 godzina dziennie, poniedziałek–sobota, 5 tygodni = 30 dni.
**Zasady projektowe:** maksimum zrozumienia, nie tempa. Każdy dzień stoi na dwóch filarach: **uczenie kogoś** (najgłębsze przetwarzanie materiału) i **praktyczne rozwiązywanie zadań** (drugie w kolejności). Do tego aktywne przypominanie z pamięci i powtórki rozłożone w czasie.

> Uwaga o "piramidzie uczenia": konkretne procenty (90%, 75%…) nie mają solidnego oparcia w badaniach, ale kierunek jest dobrze potwierdzony: tłumaczenie innym, aktywne przypominanie i rozwiązywanie zadań biją czytanie i oglądanie. Dlatego plan jest zbudowany z tych trzech rzeczy.

---

## 1. Szablon każdej godziny

| Czas | Blok | Co robisz |
|---|---|---|
| 0–5 min | **Rozgrzewka z pamięci** | Bez notatek napisz funkcję z wczoraj i jedną sprzed 7 dni (powtórka rozłożona w czasie). Nie wychodzi? Zapisz to w dzienniku błędów i wróć do tego w bloku 45–55. |
| 5–15 min | **Mini-lekcja** | Tylko to, co potrzebne do dzisiejszych zadań. Zanim napiszesz kod, rozpisz **ręcznie na kartce** jeden przykład. |
| 15–45 min | **Zadania 🟢 → 🟡 → 🔴** | Drabinka trudności (patrz sekcja 2). Każde zadanie ma **gotowy wynik oczekiwany** albo `assert`, żebyś od razu widział, czy działa. |
| 45–55 min | **🗣️ Naucz** | Wytłumacz dzisiejszy temat komuś (patrz sekcja 3). |
| 55–60 min | **Dziennik + commit** | Wpis do `bledy.md`, `git commit`. |

**Sobota** wygląda inaczej: **40 min test bez podpowiedzi i bez notatek**, potem **20 min analizy i "lekcji dla kogoś"**. Ocenianie dopiero po skończeniu testu.

---

## 2. Jak trzymać się w stanie flow

Flow pojawia się, gdy trudność jest tuż nad Twoim poziomem, cel jest jasny, a informacja zwrotna natychmiastowa. Plan to zapewnia tak:

1. **Jasny cel i szybki feedback:** do każdego zadania masz przykładowe dane i oczekiwany wynik. Dla zadań z plikami generuj własne dane skryptem `gen.py` (`random.seed(...)`, żeby były powtarzalne) i sprawdzaj wynik drugą, prostą metodą (brute force).
2. **Drabinka trudności w każdym dniu:**
   - 🟢 **Rozgrzewka** — poniżej Twojego poziomu, daje rozpęd i pewność.
   - 🟡 **Rdzeń** — dokładnie na Twoim poziomie, tu dzieje się nauka.
   - 🔴 **Wyzwanie** — o oczywisty krok wyżej; jeśli się nie uda, to nie porażka, tylko materiał na jutrzejszą rozgrzewkę.
3. **Automatyczne dopasowanie trudności:**
   - 🟢 zrobione w <5 min i bez błędu → **od razu przejdź do 🔴**.
   - 🟡 zajmuje >15 min → **zejdź po drabince podpowiedzi** (poniżej).
   - 3 dni z rzędu "za łatwo" → dołóż 🔴 z następnego dnia. 3 dni z rzędu "za trudno" → rób tylko 🟢 + 🟡 i poświęć dłużej na mini-lekcję.
   - Cel: rozwiązywać **ok. 70–85% zadań bez podpowiedzi**. Dużo więcej = nuda, dużo mniej = frustracja.
4. **Drabinka podpowiedzi (schodzisz po jednym szczebelku co ~5 min utknięcia):**
   1. Podkreśl w treści: co jest daną, co wynikiem.
   2. Rozwiąż ręcznie mały przykład (3–5 elementów).
   3. Zapisz algorytm słowami lub pseudokodem.
   4. Napisz tylko szkielet kodu (pętle, zmienne), bez warunków.
   5. Dopiero teraz zajrzyj do wskazówki / poproś o **wskazanie, GDZIE jest błąd** (nie o gotowe rozwiązanie).
5. **Warunki zewnętrzne:** stała pora, telefon poza zasięgiem ręki, jeden cel na sesję, brak zaglądania na ekran z odpowiedziami.

---

## 3. Jak "uczyć kogoś" (blok 🗣️ Naucz)

Jeśli nie masz słuchacza, **uczeń może być wyimaginowany**: kolega z klasy, który jeszcze tego nie widział. Wybierz jedną formę:
- **Gumowa kaczka / głośno do ściany** — 3 minuty bez zaglądania w kod.
- **Nagranie głosowe** 2–3 minuty (odsłuchaj raz, zanotuj, gdzie się zacinasz — tam jest luka).
- **Wpis `notatka.md` w repo** pisany tak, by zrozumiała go osoba, która nie zna tematu.
- **Prawdziwy słuchacz** (kolega, rodzeństwo) — najlepsza opcja raz w tygodniu.

**Struktura każdego wyjaśnienia:** (1) po co to jest, (2) przykład policzony ręcznie, (3) kod linijka po linijce, (4) typowy błąd i jak go rozpoznać. Gdy w którymś punkcie się zatniesz, wróć do mini-lekcji i **popraw wyjaśnienie**, nie tylko kod.

---

# TYDZIEŃ 1 — Fundamenty i pliki

### Dzień 1 (Pn) — Diagnostyka i środowisko

- [x] **Dzień ukończony**

**Cel:** ustalić poziom startowy, żeby reszta planu trafiała w flow.
- **Test diagnostyczny (25 min, bez podpowiedzi):** 8 mini-zadań: (1) suma liczb parzystych od 1 do n, (2) odwrócenie napisu, (3) liczba samogłosek w zdaniu, (4) maksimum listy i jego indeks, (5) wczytanie pliku z liczbami i suma, (6) suma cyfr liczby, (7) czy liczba jest pierwsza, (8) zliczenie wystąpień każdego elementu listy.
- **Wynik → poziom:** 7–8 zadań = poziom **szybki** (pomijaj 🟢 do końca tygodnia 2); 4–6 = **standard** (wszystko po kolei); 0–3 = **spokojny** (🟢 + 🟡, 🔴 opcjonalnie; mini-lekcje rób bez pośpiechu).
- **Konfiguracja (20 min):** VS Code + Python 3, repo na GitHubie, plik `bledy.md` na dziennik błędów.
- 🗣️ **Naucz:** wytłumacz, jak działa `for i in range(...)` (trzy przykłady: `range(5)`, `range(2, 10)`, `range(10, 0, -2)`).

### Dzień 2 (Wt) — Wczytywanie i zapisywanie plików

- [x] **Dzień ukończony**

**Cel:** pewnie obsługiwać pliki tekstowe, bo na maturze prawie każde zadanie od nich zaczyna.
- **Mini-lekcja:** `open`/`with`, `read`/`readlines`/iteracja po liniach, `strip`, `split` (spacja vs `;`), `int`/`float`, kodowanie, zapis do pliku.
- 🟢 Plik z liczbami (jedna na linię): suma, średnia, min, max.
- 🟡 Plik CSV z `;` (`imię;wiek;miasto`): ile osób jest starszych niż średnia wieku; wynik zapisz do `wyniki.txt`.
- 🔴 Plik z liczbami w jednej linii oddzielonymi spacjami, z pustymi liniami i zbędnymi spacjami: napisz odporny parser, zlicz liczby ujemne, zapisz wyniki w formacie `a) ...`, `b) ...`.
- 🗣️ **Naucz:** wytłumacz "5 najczęstszych pułapek wczytywania pliku" (znak nowej linii, puste linie, `str` vs `int`, separator, kodowanie).

### Dzień 3 (Śr) — Warunki, pętle i tłumaczenie pseudokodu

- [ ] **Dzień ukończony**

**Cel:** płynnie przechodzić z pseudokodu CKE na Pythona i obsługiwać wzorzec "bieżący vs najlepszy".
- **Mini-lekcja:** `if/elif/else`, `for`/`while`, `break`/`continue`, `%`, `//`, `**`, `divmod`; zamiana `dla i ← 1 do n` na `range(1, n+1)` oraz `dopóki` na `while`.
- 🟢 Zlicz liczby podzielne przez 3 lub 5 w pliku.
- 🟡 Najdłuższy ciąg kolejnych, rosnących liczb w pliku (długość + pierwszy element). Wzorzec: licznik bieżący, licznik najlepszy.
- 🔴 Liczba par `(i < j)` o sumie równej `k`: najpierw wersja O(n²), potem przetestuj na małych danych ręcznie.
- 🗣️ **Naucz:** wyjaśnij wzorzec "bieżący vs najlepszy" na ciągu 1 2 3 1 2 1 2 3 4.

### Dzień 4 (Cz) — Funkcje i własna biblioteka

- [ ] **Dzień ukończony**

**Cel:** dzielić rozwiązanie na małe, testowalne funkcje.
- **Mini-lekcja:** `def`, `return` vs `print`, parametry, zasięg zmiennych, `assert`.
- 🟢 `suma_cyfr`, `odwroc_liczbe`, `ile_cyfr` + po 3 `assert` na każdą.
- 🟡 `czy_palindrom` (liczba i napis) i dodanie wszystkiego do `narzedzia.py`.
- 🔴 Zadanie z pliku z użyciem biblioteki: ile liczb ma sumę cyfr równą 10 **i** jest palindromem?
- 🗣️ **Naucz:** pokaż na błędnym przykładzie, czym różni się `return` od `print`, i czemu funkcja zwracająca `None` psuje dalszy kod.

### Dzień 5 (Pt) — Listy, wycinki i komprehensje

- [ ] **Dzień ukończony**

**Cel:** swobodnie operować na listach i rozumieć referencje.
- **Mini-lekcja:** indeksy (też ujemne), slicing, `append`/`pop`/`insert`, `in`, `enumerate`, `zip`, list comprehension, kopiowanie vs referencja (`b = a` vs `b = a[:]`).
- 🟢 Odwróć listę; obróć listę o `k` miejsc w prawo.
- 🟡 Elementy występujące w liście dokładnie raz (najpierw ręcznie, bez `Counter`).
- 🔴 Drugi największy element bez sortowania i bez `max` dwa razy; potem to samo jednym przebiegiem.
- 🗣️ **Naucz:** narysuj na kartce, co dzieje się w pamięci przy `b = a` i `b = a[:]`, i wytłumacz to komuś.

### Dzień 6 (So) — 🧪 TEST 1 (bez podpowiedzi)

- [ ] **Dzień ukończony**

**Zakres:** dni 1–5. **40 min, bez notatek.** Trzy zadania z plikami (dane z `gen.py`):
1. `liczby.txt` (1000 liczb): ile jest parzystych; największa i pozycja pierwszego wystąpienia.
2. `dane.txt` (`imię;wiek;miasto`): ile osób z każdego miasta; najstarsza osoba.
3. Najdłuższy ciąg rosnących kolejnych liczb w `liczby.txt`.

**Po teście (20 min):** analiza błędów → `bledy.md`; 🗣️ nagraj 3-minutową "lekcję tygodnia 1" na wybrany temat, w którym straciłeś/aś najwięcej czasu.

---

# TYDZIEŃ 2 — Liczby i teoria liczb

### Dzień 7 (Pn) — Cyfry liczby

- [ ] **Dzień ukończony**

**Cel:** biegle rozbijać liczbę na cyfry.
- **Mini-lekcja:** `%10` i `//10`, wersja ze `str(n)`, kiedy która.
- 🟢 Suma cyfr liczb z pliku.
- 🟡 Liczby, których suma cyfr równa się iloczynowi cyfr.
- 🔴 Liczby Armstronga w przedziale; liczby, których kwadrat kończy się na nią samą.
- 🗣️ **Naucz:** wytłumacz algorytm `%10` / `//10` komuś, kto nie zna dzielenia z resztą.

### Dzień 8 (Wt) — Podzielniki, liczby pierwsze, doskonałe

- [ ] **Dzień ukończony**

**Cel:** rozumieć, dlaczego algorytmy na liczbach działają i ile kosztują.
- **Mini-lekcja:** dzielniki do `√n`, test pierwszości, sito Eratostenesa.
- 🟢 `czy_pierwsza` naiwnie; potem do `√n`.
- 🟡 Wszystkie liczby pierwsze do 100 000 sitem; porównaj czas z testem naiwnym (`time.perf_counter`).
- 🔴 Liczby doskonałe i zaprzyjaźnione; liczba z największą liczbą dzielników w pliku.
- 🗣️ **Naucz:** wyjaśnij w trzech zdaniach, dlaczego wystarczy sprawdzać dzielniki do `√n`.

### Dzień 9 (Śr) — NWD, NWW, rozkład na czynniki, ułamki

- [ ] **Dzień ukończony**

**Cel:** opanować algorytm Euklidesa w obu wersjach.
- **Mini-lekcja:** Euklides iteracyjnie i rekurencyjnie, `NWW = a*b // NWD`, rozkład na czynniki pierwsze.
- 🟢 `nwd` iteracyjnie i rekurencyjnie, z `assert`.
- 🟡 Plik z ułamkami `a/b`: skróć każdy; zsumuj wszystkie do jednego nieskracalnego ułamka.
- 🔴 Ile par liczb z pliku jest względnie pierwszych? Wersja O(n²), potem pomysł na szybsze liczenie.
- 🗣️ **Naucz:** wyjaśnij Euklidesa na parze 48 i 18 (rysunek kroków) i **dlaczego** to działa.

### Dzień 10 (Cz) — Systemy liczbowe i operacje bitowe

- [ ] **Dzień ukończony**

**Cel:** konwersje bez magii i bez kopiowania gotowców.
- **Mini-lekcja:** `bin`/`hex`/`oct`, `int(s, base)`, f-stringi `:b` `:x`, operatory `&`, `|`, `^`, `<<`, `>>`.
- 🟢 Własne `dec_na_bin` i `bin_na_dec` (bez `bin()` i `int(s, 2)`).
- 🟡 Plik z liczbami binarnymi: ile jest parzystych, największa, ile ma więcej zer niż jedynek.
- 🔴 Liczby, które w zapisie binarnym są palindromami; konwersja do dowolnej podstawy 2–16.
- 🗣️ **Naucz:** wyjaśnij, dlaczego grupa 4 bitów to jedna cyfra szesnastkowa (i 3 bity = cyfra ósemkowa).

### Dzień 11 (Pt) — Duże liczby i arytmetyka pisemna

- [ ] **Dzień ukończony**

**Cel:** rozumieć, co robi Python za Ciebie, i umieć to zrobić ręcznie.
- **Mini-lekcja:** nieograniczony `int`, `pow(a, b, m)`, liczby jako napisy, dodawanie pisemne.
- 🟢 Plik z liczbami 100-cyfrowymi: suma i największa (przez `int`).
- 🟡 Własne dodawanie pisemne dwóch liczb zapisanych jako napisy (bez `int()`), z przeniesieniem.
- 🔴 Mnożenie pisemne przez liczbę jednocyfrową; porównanie dwóch dużych liczb jako napisów.
- 🗣️ **Naucz:** wytłumacz, dlaczego dodawanie pisemne idzie od końca i jak działa przeniesienie.

### Dzień 12 (So) — 🧪 TEST 2 (bez podpowiedzi)

- [ ] **Dzień ukończony**

**Zakres:** dni 7–11 + powtórka tygodnia 1. **40 min.**
1. `liczby.txt`: ile liczb pierwszych; największa pierwsza.
2. Ile liczb ma palindromiczny zapis binarny; największa z nich.
3. NWD wszystkich liczb z pliku; para o największym NWD (n ≈ 500).

Po teście: analiza, `bledy.md`, 🗣️ lekcja tygodnia 2.

---

# TYDZIEŃ 3 — Napisy i struktury danych

### Dzień 13 (Pn) — Napisy

- [ ] **Dzień ukończony**

**Cel:** swobodnie analizować teksty.
- **Mini-lekcja:** indeksy i slicing, `s[::-1]`, `upper`/`lower`, `isalpha`/`isdigit`, `find`/`count`/`replace`, `join`/`split`, f-stringi, `ord`/`chr`.
- 🟢 Palindromy w pliku ze słowami.
- 🟡 Najdłuższe słowo, najkrótsze, pierwsze alfabetycznie; liczba samogłosek w każdym słowie.
- 🔴 Najdłuższy podciąg jednej litery; naprzemienna wielkość liter.
- 🗣️ **Naucz:** wytłumacz, czemu napisy są niemutowalne i dlaczego `s[0] = "a"` kończy się błędem.

### Dzień 14 (Wt) — Szyfry

- [ ] **Dzień ukończony**

**Cel:** ćwiczyć `ord`/`chr` i arytmetykę modulo na czymś, co ma sens.
- **Mini-lekcja:** Cezar, `(ord(c) - 65 + k) % 26 + 65`, odwracanie szyfru, Atbash, ROT13.
- 🟢 Szyfr Cezara z kluczem `k`.
- 🟡 Plik: pierwsza linia to klucz, kolejne to tekst do odszyfrowania.
- 🔴 Vigenère z hasłem; złam szyfr Cezara brute force (szukaj słowa w tekście).
- 🗣️ **Naucz:** zaszyfruj zdanie i **wyślij komuś jako wyzwanie do złamania**. Jeśli nie umie, wytłumacz mu, jak.

### Dzień 15 (Śr) — Słowniki i zliczanie

- [ ] **Dzień ukończony**

**Cel:** myśleć "klucz → wartość" tam, gdzie wcześniej pisałeś/aś pętle w pętli.
- **Mini-lekcja:** `dict`, `.get`, `.items()`, `defaultdict`, `Counter`, sortowanie po wartościach (`key=lambda`).
- 🟢 Histogram liter w pliku z tekstem.
- 🟡 Najczęstsze słowo; remisy rozstrzygaj alfabetycznie.
- 🔴 Grupowanie anagramów; dla każdej grupy podaj liczebność i listę słów.
- 🗣️ **Naucz:** wyjaśnij, dlaczego szukanie w słowniku jest szybsze niż w liście (idea haszowania).

### Dzień 16 (Cz) — Zbiory i krotki

- [ ] **Dzień ukończony**

**Cel:** wybierać właściwą strukturę danych świadomie.
- **Mini-lekcja:** `set`, `|`, `&`, `-`, `in` w O(1), `tuple`, `zip`, rozpakowywanie.
- 🟢 Liczba unikalnych wartości w pliku.
- 🟡 Wspólne słowa dwóch plików.
- 🔴 Pary o sumie `k` w O(n) z użyciem zbioru.
- 🗣️ **Naucz:** zrób tabelkę decyzyjną "lista / zbiór / słownik / krotka — kiedy co?" i wyjaśnij ją komuś.

### Dzień 17 (Pt) — Złożone pliki i łączenie danych

- [ ] **Dzień ukończony**

**Cel:** radzić sobie z danymi tak "brudnymi", jak w arkuszach CKE.
- **Mini-lekcja:** nagłówki, kolumny, daty `RRRR-MM-DD` (`split("-")`), formatowanie `f"{x:.2f}"`, sortowanie krotek.
- 🟢 Dwa pliki (`osoby.txt`, `wyniki.txt`): połącz po identyfikatorze (słownik).
- 🟡 Średnie w grupach, najlepszy w grupie, ranking.
- 🔴 Plik z błędnymi wierszami (puste pola, przecinek zamiast kropki): wyczyść i przygotuj raport błędów.
- 🗣️ **Naucz:** opisz algorytm "JOIN w Pythonie" (słownik jako indeks) tak, żeby zrozumiał go ktoś, kto zna tylko SQL.

### Dzień 18 (So) — 🧪 TEST 3 (bez podpowiedzi)

- [ ] **Dzień ukończony**

**Zakres:** dni 13–17 + losowo z tygodni 1–2. **40 min.**
1. `slowa.txt`: ile palindromów; najdłuższe słowo (pierwsze alfabetycznie przy remisie).
2. Tekst zaszyfrowany Cezarem z nieznanym kluczem: znajdź klucz, odszyfruj, podaj histogram liter.
3. Dwa pliki: połącz po id, policz średnie, wypisz najlepszego z każdej grupy.

---

# TYDZIEŃ 4 — Algorytmy

### Dzień 19 (Pn) — Sortowanie kwadratowe

- [ ] **Dzień ukończony**

**Cel:** rozumieć, co sortowanie robi krok po kroku.
- **Mini-lekcja:** bubble, selection, insertion; `sorted`/`.sort()` z `key` i `reverse`; stabilność.
- 🟢 Bubble sort ze zliczaniem zamian.
- 🟡 Sortowanie rekordów po dwóch kryteriach (`key=lambda r: (r[1], r[0])`).
- 🔴 Selection i insertion na tej samej tablicy: porównaj liczbę porównań i zamian z teorią O(n²).
- 🗣️ **Naucz:** pokaż bubble sort na kartach (fizycznie) i wytłumacz, czemu stabilność ma znaczenie.

### Dzień 20 (Wt) — Sortowanie szybkie

- [ ] **Dzień ukończony**

**Cel:** zrozumieć "dziel i zwyciężaj".
- **Mini-lekcja:** merge sort, quicksort, sortowanie przez zliczanie.
- 🟢 Funkcja scalająca dwie posortowane listy.
- 🟡 Merge sort rekurencyjnie.
- 🔴 Counting sort dla zakresu 0–1000; porównaj czas z `sorted()` na 10⁵ elementów.
- 🗣️ **Naucz:** wytłumacz scalanie na dwóch taliach kart posortowanych rosnąco.

### Dzień 21 (Śr) — Wyszukiwanie, dwa wskaźniki, okno

- [ ] **Dzień ukończony**

**Cel:** szybkie schematy na tablicach.
- **Mini-lekcja:** liniowe, binarne (iteracyjnie i rekurencyjnie), `bisect`, dwa wskaźniki, okno przesuwne, sumy prefiksowe.
- 🟢 Wyszukiwanie binarne z licznikiem porównań.
- 🟡 Para o sumie `k` w posortowanej tablicy (dwa wskaźniki).
- 🔴 Najdłuższy odcinek o sumie ≤ `S` (okno przesuwne); suma dowolnego przedziału w O(1) (prefiksy).
- 🗣️ **Naucz:** wyjaśnij trzy zmienne `p`, `k`, `mid` i **dlaczego** warunkiem stopu jest `p > k`.

### Dzień 22 (Cz) — Rekurencja

- [ ] **Dzień ukończony**

**Cel:** widzieć drzewo wywołań, nie tylko wzór.
- **Mini-lekcja:** przypadek bazowy, stos wywołań, `lru_cache`/słownik jako pamięć, rekurencja → iteracja.
- 🟢 Silnia i Fibonacci rekurencyjnie; zmierz czas dla `n = 35`.
- 🟡 Fibonacci z memoizacją; szybkie potęgowanie.
- 🔴 Wieże Hanoi; wszystkie podzbiory zbioru i ile z nich ma sumę `k`.
- 🗣️ **Naucz:** narysuj drzewo wywołań `fib(5)`, zaznacz powtórzenia i wyjaśnij, co daje memoizacja.

### Dzień 23 (Pt) — Tablice dwuwymiarowe i obrazy

- [ ] **Dzień ukończony**

**Cel:** pewnie pracować na macierzach, w tym na obrazach 320×200.
- **Mini-lekcja:** wczytanie macierzy z pliku, `[i][j]`, sąsiedzi i granice, transpozycja, obrót o 90°.
- 🟢 Min/max w obrazie; negatyw (`255 - x`).
- 🟡 Obrót o 90° i odbicie lustrzane (komprehensje list).
- 🔴 Piksele, które różnią się o więcej niż 128 od któregokolwiek sąsiada (pilnuj granic!); najdłuższa linia o stałej wartości.
- 🗣️ **Naucz:** wytłumacz, jak uniknąć `IndexError` przy sprawdzaniu sąsiadów w narożnikach.

### Dzień 24 (So) — 🧪 TEST 4 (bez podpowiedzi)

- [ ] **Dzień ukończony**

**Zakres:** dni 19–23 + losowo z tygodni 1–3. **40 min.**
1. Własne sortowanie z licznikiem zamian na danych z pliku.
2. Wyszukiwanie binarne z licznikiem porównań dla 50 zapytań.
3. Obraz 320×200: liczba pikseli o kontraście powyżej progu.

---

# TYDZIEŃ 5 — Integracja, optymalizacja, egzamin

### Dzień 25 (Pn) — Programowanie dynamiczne i algorytmy zachłanne

- [ ] **Dzień ukończony**

**Cel:** poznać dwie "rodziny" rozwiązań, które pojawiają się w trudniejszych zadaniach.
- **Mini-lekcja:** zachłanność (wydawanie reszty), DP (tablica wyników częściowych), Kadane.
- 🟢 Liczba sposobów wejścia po schodach (1 lub 2 stopnie).
- 🟡 Największa suma spójnego podciągu (Kadane); wydawanie reszty zachłannie vs DP — znajdź zestaw monet, gdzie zachłanność zawodzi.
- 🔴 Najdłuższy podciąg rosnący; (opcjonalnie) plecak 0/1.
- 🗣️ **Naucz:** wyjaśnij różnicę między rekurencją z memoizacją a DP "od dołu".

### Dzień 26 (Wt) — Złożoność w praktyce

- [ ] **Dzień ukończony**

**Cel:** przewidywać i mierzyć koszt kodu.
- **Mini-lekcja:** `time.perf_counter`, O(n²) vs O(n log n), `in` na liście vs zbiorze, `+=` na napisach vs `join`.
- 🟢 Zmierz czasy 3 algorytmów na rosnących `n` i wpisz do tabelki.
- 🟡 Przyspiesz rozwiązanie z dnia 8 (pierwsze) dla 10⁵–10⁶ liczb.
- 🔴 Dostajesz kod z celowym wąskim gardłem; znajdź go i przyspiesz.
- 🗣️ **Naucz:** zrób tabelkę "operacja → koszt" (lista, zbiór, słownik, napis) i wytłumacz ją komuś.

### Dzień 27 (Śr) — Symulacje, ciągi, kombinatoryka

- [ ] **Dzień ukończony**

**Cel:** zadania "z życia wzięte": reguły, kroki, symulacja.
- **Mini-lekcja:** ciąg Collatza, trójkąt Pascala, `itertools` (permutacje, kombinacje), automaty komórkowe.
- 🟢 Collatz: długość sekwencji dla `n`.
- 🟡 Trójkąt Pascala; Collatz — liczba do `N` o najdłuższej sekwencji.
- 🔴 Automat 1D (reguła 30 lub 110) lub jeden krok gry w życie na tablicy 2D.
- 🗣️ **Naucz:** zasymuluj na kartce 3 kroki automatu **przed** uruchomieniem kodu i wytłumacz regułę komuś.

### Dzień 28 (Cz) — Debugowanie i testy graniczne

- [ ] **Dzień ukończony**

**Cel:** szybko znajdować własne błędy.
- **Mini-lekcja:** czytanie traceback, `print`-debug, `assert`, typowe błędy (off-by-one, kopiowanie list, `/` vs `//`, `"01"` vs `1`, domyślne argumenty mutowalne), `try/except`.
- 🟢 Napraw 5 celowo zepsutych funkcji (przygotuj je sobie albo poproś kogoś).
- 🟡 Dopisz testy graniczne (pusta lista, jeden element, same duplikaty) do funkcji z `narzedzia.py`.
- 🔴 Przejrzyj własny kod z dni 1–6 i zrób listę 10 rzeczy, które dziś zrobiłbyś/zrobiłabyś inaczej.
- 🗣️ **Naucz:** zrób code review własnego kodu sprzed miesiąca, tak jak zrobiłbyś/zrobiłabyś koledze.

### Dzień 29 (Pt) — Trening zintegrowany + naprawa luk

- [ ] **Dzień ukończony**

**Cel:** połączyć wszystko i załatać to, co jeszcze się sypie.
- **Przegląd (10 min):** otwórz `bledy.md` i wybierz **3 najczęściej powtarzające się błędy**.
- **Zadania (30 min):** dla każdego z tych błędów 1 nowe zadanie w stylu CKE (plik + pytanie + zapis wyników), każde z innego działu planu.
- **Wyzwanie:** jedno zadanie łączące co najmniej 3 techniki (np. plik → słownik → sortowanie → zapis).
- 🗣️ **Naucz:** wybierz najtrudniejszy temat całego planu i przygotuj 5-minutową lekcję z przykładem.

### Dzień 30 (So) — 🧪 TEST FINAŁOWY

- [ ] **Dzień ukończony**

**Zakres:** cały plan. **40 min bez notatek i bez podpowiedzi**, potem 20 min analizy.
- Weź 2–3 zadania programistyczne z **archiwalnego arkusza CKE** (z formuły egzaminu obowiązującej Cię na maturze, strona CKE, arkusze maturalne), z plikami danych.
- Zadanie na czas: najpierw wszystkie przeczytaj, wybierz kolejność od najłatwiejszego, na każde zaplanuj z góry czas.
- Po teście: wynik porównaj z kluczem CKE (z punktacją częściową), przejrzyj `bledy.md` i sporządź listę tematów do powtórek na kolejne tygodnie.

---

## 4. Lista kontrolna zakresu ("czy umiem wszystko z Pythona?")

| Obszar | Dni |
|---|---|
| Pliki (odczyt, zapis, brudne dane, łączenie) | 2, 17 |
| Pętle, warunki, pseudokod → Python | 3 |
| Funkcje, testy, własna biblioteka | 4 |
| Listy, wycinki, komprehensje | 5 |
| Cyfry, podzielniki, pierwsze, NWD/NWW | 7–9 |
| Systemy liczbowe, operacje bitowe | 10 |
| Duże liczby, arytmetyka pisemna | 11 |
| Napisy, szyfry | 13–14 |
| Słowniki, zbiory, krotki | 15–16 |
| Sortowanie (kwadratowe i szybkie) | 19–20 |
| Wyszukiwanie, dwa wskaźniki, okno, prefiksy | 21 |
| Rekurencja, memoizacja | 22 |
| Tablice 2D, obrazy | 23 |
| DP, zachłanność | 25 |
| Złożoność i optymalizacja | 26 |
| Symulacje, ciągi, kombinatoryka | 27 |
| Debugowanie, testy graniczne | 28 |
| Integracja i egzamin | 29–30 |

Powodzenia na maturze! 🎯
