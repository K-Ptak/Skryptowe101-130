string = input("Podaj zdanie: ")

count = 0

for letter in string.lower():
    if letter in "aeyiouó":
        count += 1

print(count)
