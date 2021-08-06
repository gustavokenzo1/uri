x = int(input())
z = int(input())

while z <= x:
    z = int(input())

soma = x
total = 0

while soma < z:
    proximo = x + 1
    soma += proximo
    total += 1

print(total)
