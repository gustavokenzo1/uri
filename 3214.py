n = input().split()

e = int(n[0]) # bottles tim had at the start
f = int(n[1]) # bottles found during the day
c = int(n[2]) # bottles required to buy one soda

total_bottles = e + f
total_sodas = 0

# exemplo: 9 0 3 -> perde 3, fica com 6, ganha 1 soda e, portanto, 1 bottle
# 7 0 3 (com 1 bottle)
# 5 0 3 (2)
# 3 0 3 (3)
# 0 0 3 (4)

while total_bottles >= c:
    total_bottles -= c
    total_sodas += 1
    total_bottles += 1

print(total_sodas)
