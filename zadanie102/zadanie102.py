def silnia(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * silnia(n - 1)


liczba = input("Podaj liczbe: ")
try:
    liczba = int(liczba)
except ValueError:
    print("Musisz podac liczbe")
    exit()

print(f"Liczba : {liczba}")
print(f"Silnia : {silnia(liczba)}")