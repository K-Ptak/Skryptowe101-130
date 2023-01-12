import string


def szyfruj(tekst):
    tekst = ''.join(c for c in tekst if c not in string.punctuation)
    czestosci = {}
    for c in tekst:
        if c in czestosci:
            czestosci[c] += 1
        else:
            czestosci[c] = 1
    czestosci_sort = sorted(czestosci.items(), key=lambda x: x[1])
    kody = {}
    kody[czestosci_sort[0][0]] = '0'
    for i in range(1, len(czestosci_sort)):
        kody[czestosci_sort[i][0]] = kody[czestosci_sort[i - 1][0]] + '1'
    szyfr = ''
    for c in tekst:
        szyfr += kody[c]
    return szyfr


def deszyfruj(szyfr):
    kody = {}
    kody[szyfr[0]] = '0'
    for i in range(1, len(szyfr)):
        if szyfr[i] not in kody:
            kody[szyfr[i]] = kody[szyfr[i - 1]] + '1'
    tekst = ''
    kod = ''
    for c in szyfr:
        kod += c
        if kod in kody.values():
            for key, value in kody.items():
                if value == kod:
                    tekst += key
            kod = ''
    return tekst

szyfr = szyfruj('Ala ma kota')
tekst = deszyfruj(szyfr)

print(szyfr)
print(tekst)