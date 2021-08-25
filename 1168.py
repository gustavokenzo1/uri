testes = int(input())
leds = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]

for i in range(testes):
    num = input()
    total = 0

    for j in range(len(num)):
        numero = int(num[j])
        total += leds[numero - 1]
    print(total, "leds")
