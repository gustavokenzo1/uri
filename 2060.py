total = int(input())
numero = input().split()
nums = []

for i in range(total):
    nums.append(int(numero[i]))

m2 = 0
m3 = 0
m4 = 0
m5 = 0


for i in range(len(nums)):

    if nums[i] % 4 == 0: # Um múltiplo de 4 é, consequentemente, de 2 também
        m2 += 1
        m4 += 1

    elif nums[i] % 2 == 0:
        m2 += 1

    if nums[i] % 3 == 0:
        m3 += 1
    
    if nums[i] % 5 == 0:
        m5 += 1

print(str(m2) + ' Multiplo(s) de 2')
print(str(m3) + ' Multiplo(s) de 3')
print(str(m4) + ' Multiplo(s) de 4')
print(str(m5) + ' Multiplo(s) de 5')
