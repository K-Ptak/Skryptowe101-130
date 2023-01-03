def insertionSort(input):
    new = input
    for j in range(2, len(new)):
        key = new[j]
        i = j - 1
        while i >= 0 and new[i] > key:
            new[i + 1] = new[i]
            i -= 1
        new[i + 1] = key
    return new

numbers = []

try:

    file = open("danezadanie104.txt", "r")
    for line in file.readlines():
        try:
            numbers.append(int(line))
        except ValueError:
            continue

    file.close()

    with open("zadanie104_insertion.txt", "w") as insert:
        for number in insertionSort(numbers):
            insert.write(str(number) + "\n")

except IOError:
    print("Blad otwierania pliku")
