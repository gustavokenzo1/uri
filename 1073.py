n = int(input())

while n <= 5 and n > 2000:
    n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        square = i**2
        print(str(i) + '^' + '2' + ' = ' + str(square))
    else:
        continue
