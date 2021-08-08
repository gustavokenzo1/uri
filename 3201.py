f = True
p = 0
k, l = map(int, input().split())
while k != 0 and l!= 0:
    for i in range(2, l):
        if k % i == 0:
                p = i
                f = False
                break
    if f:
        print("GOOD")
    else:
        print("BAD", p)
    f = True
    p = 0
    k, l = map(int, input().split())
