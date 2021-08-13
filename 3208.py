while True:
    f = True
    p = 0
    k, l = map(int, input().split())
    if k == 0 and l == 0:
        break
    for i in range(2, l):
        if k % i == 0:
                p = i
                f = False
                break
    if f:
        print("GOOD")
    else:
        print("BAD", p)
