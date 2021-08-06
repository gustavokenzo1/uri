total = int(input())

for i in range(total):
    nums = input().split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    soma = 0

    if num1 < num2:
        for j in range(num1 + 1, num2, 1): # Primeiro argumento é inclusivo e o segundo não
            if j % 2 != 0:
                soma += j

    elif num1 == num2:
        soma = 0
    
    else:
        for j in range(num1 - 1, num2, -1):
            if j % 2 != 0:
                soma += j
    print(soma)
