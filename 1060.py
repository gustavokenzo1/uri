total_positivo = 0

for i in range(6):
    num = float(input())
    
    if num > 0:
        total_positivo += 1
    else:
        continue

print(str(total_positivo) + ' valores positivos')
