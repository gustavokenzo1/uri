""" 
ex: 3 2 3 4
Primeira: ligada na tomada diretamente, e pode ligar no próximo: 3 livres
Segunda: 2 outlets ocupados, um de entrada e um de saída. Inútil: 0 livres
Terceira: 1 livre: 1 livre
Última: só 1 outlet precisa ser ocupado para energia: 3 livres
Total: 3 + 0 + 1 + 3 = 7

Conclusões:
Primeiro power strip fica completamente livre
Power strips intermediários ficam com -2
Último power strip fica com 1 ocupado

"""
cases = int(input())
power = []

for i in range(cases):
    tomadas = input().split()

    for j in range(0, len(tomadas)):
        if j == 0:
            power.append(int(tomadas[j]))
        
        elif j != 0 and j != (len(tomadas) - 1):
            power.append(int(tomadas[j]) - 2)
        
        else:
            power.append(int(tomadas[len(tomadas) - 1]) - 1)

    print(sum(power))
    power.clear()
    
