while True:
    keys = input().split()

    if len(keys) != 2:
        continue

    k = int(keys[0])
    l = int(keys[1])

    if k == 0 and l == 0:
        break

    primo, primo2 = 0, 0

    for i in range(l, k):
        if k % i == 0:
            primo = k/i
            break

    for i in range(2, l):
        if k % i == 0: 
            primo2 = k/i
            break

    if primo2 > l:
        primo2 = k/primo2

    if round(k/(primo2+0.1)) < primo2:
        primo2 = k/primo2

    if primo < l:
        print("BAD", int(primo2))
    else:
        print("GOOD")
