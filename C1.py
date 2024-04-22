codes = ['0', '110', '111']

for i in range(1, 3):
    for x in range(2 ** i):
        pfx = bin(x)[2:].zfill(i)
        if all(c[:i] != pfx and pfx[:len(c)] != c
               for c in codes):
            print(pfx)
            break
