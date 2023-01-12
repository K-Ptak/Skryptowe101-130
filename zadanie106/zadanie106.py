import math
import time
import datetime


data = datetime.datetime.now()
data = data.strftime("%d.%m.%Y")

with open(f"raport_{data}", "w") as wynik:
    wynik.write("RAPORT ALGORYTMOW SORTOWANIA \n")
    wynik.write("NAZWA -- LICZBA SORTOWANYCH PLIKOW -- SREDNI CZAS -- ODCHYLENIE STANDARDOWE \n")
    start_time = time.time()
    exec(open("../zadanie104/zadanie104_bubble.py").read())
    end_time = time.time() - start_time
    numbers = []
    with open("../zadanie104/zadanie104_bubble.txt", 'r') as fp:
        for line in fp:
            numbers.append(int(line))

    srednia = sum(numbers)/len(numbers)
    licznik = 0
    for x in numbers:
        licznik += math.pow((x - srednia), 2)

    odchyl = math.sqrt(licznik / len(numbers))

    wynik.write(f"1. babelkowe -- {len(numbers)} -- {end_time} s -- {odchyl} \n")

    start_time = time.time()
    exec(open("../zadanie104/zadanie104_insertion.py").read())
    end_time = time.time() - start_time
    numbers = []
    with open("../zadanie104/zadanie104_insertion.txt", 'r') as fp:
        for line in fp:
            numbers.append(int(line))

    srednia = sum(numbers) / len(numbers)
    licznik = 0
    for x in numbers:
        licznik += math.pow((x - srednia), 2)

    odchyl = math.sqrt(licznik / len(numbers))

    wynik.write(f"2. wstawianie -- {len(numbers)} -- {end_time} s -- {odchyl} \n")
    start_time = time.time()
    exec(open("../zadanie104/zadanie104_quick.py").read())
    end_time = time.time() - start_time
    numbers = []
    with open("../zadanie104/zadanie104_quick.txt", 'r') as fp:
        for line in fp:
            numbers.append(int(line))

    srednia = sum(numbers) / len(numbers)
    licznik = 0
    for x in numbers:
        licznik += math.pow((x - srednia), 2)

    odchyl = math.sqrt(licznik / len(numbers))

    wynik.write(f"3. Szybkie -- {len(numbers)} -- {end_time} s -- {odchyl} \n")
