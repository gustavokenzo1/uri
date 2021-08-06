# one, two, three
# one and two têm 3 letras
# one e two têm apenas o 'o' em comum
# apenas uma das letras estará errada

cases = int(input())

for i in range(cases):
    num = input()
    certo = 0
    num = list(num)
    
    if num[0] == 'o':
        certo += 1
    if num[1] == 'n':
        certo += 1
    if num[2] == 'e':
        certo += 1

    if len(num) > 3:
        print(3)
        
    elif len(num) == 3:
        if certo >= 2:
            print(1)
            
        else:
            print(2)
