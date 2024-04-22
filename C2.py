from itertools import product

lib = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
glas = "AEIOUY"

k = 0

for i in product(lib, repeat=5):
    for j in i:
        if j in glas:
            k += 1
            print(str(i).replace("'", ",").replace(" ", ",").replace(",", "")[1:len(i)+1])
            break

print(k)

