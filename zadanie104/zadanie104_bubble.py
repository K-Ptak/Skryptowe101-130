def bubbleSort(input):
    new = input
    for i in range(0, len(new) - 1):
        for j in range(0, len(new) - 1):
            if new[j] > new[j + 1]:
                new[j], new[j + 1] = new[j + 1], new[j]
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

    with open("zadanie104_bubble.txt", "w") as bubble:
        for number in bubbleSort(numbers):
            bubble.write(str(number) + "\n")

except IOError:
    print("Blad otwierania pliku")
