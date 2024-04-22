for A in range(10000, 2, -1):
    k = 0
    for x in range(1, 1000):
        F = (21 // A) and (((x // 40) and (x // 30)) <= (x // A))
        if F:
            k = 1
            break
    if k:
        print(A)
        break
