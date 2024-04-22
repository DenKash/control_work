n = int(input())
m = []
for i in range(n):
    m += [input()]

for j in m:
    k = str(j).split()
    print(sum(int(l) for l in k))
