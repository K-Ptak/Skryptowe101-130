def quickSort(input):
    def partition(input, p, k):
        x = input[k]
        i = p - 1
        for j in range(p, k):
            if input[j] <= x:
                i += 1
                input[i], input[j] = input[j], input[i]
        input[k], input[i + 1] = input[i + 1], input[k]
        return i + 1

    def main(input, p, k):
        if p < k:
            q = partition(input, p, k)
            main(input, p, q - 1)
            main(input, q + 1, k)

    new = input
    main(new, 0, len(new) - 1)
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

    with open("zadanie104_quick.txt", "w") as quick:
        for number in quickSort(numbers):
            quick.write(str(number) + "\n")

except IOError:
    print("Blad otwierania pliku")
