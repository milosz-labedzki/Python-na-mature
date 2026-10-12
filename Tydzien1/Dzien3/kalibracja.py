n=10
i = 1
wynik = 0
while i <= n:
    if(i % 3 == 0 or i % 5 == 0):
        wynik += 1
    i += 1 
print (wynik)