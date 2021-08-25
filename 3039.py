# boys = car
# girls = doll

n = int(input())
m = 0
f = 0

for i in range(n):
    name = input().lower().split()
    sexo = name[1]
    if sexo == 'm':
        m += 1
    else:
        f += 1

print(str(m) + ' carrinhos')
print(str(f) + ' bonecas')
