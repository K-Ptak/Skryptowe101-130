def silnia(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        while (n > 1):
            factorial *= n
            n -= 1
        return factorial


liczba = input("Podaj liczbe: ")
try:
    liczba = int(liczba)
except ValueError:
    print("Musisz podac liczbe")
    exit()

print(f"Liczba : {liczba}")
print(f"Silnia : {silnia(liczba)}")