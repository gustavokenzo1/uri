mae = int(input())

a = int(input())
b = int(input())
c = mae-a-b

if a > b and a > c:
    print(a)

if b > a and b > c:
    print(b)

if c > a and c > b:
    print(c)
