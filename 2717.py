restantes = int(input())
minutos = input().split(' ')

total = int(minutos[0]) + int(minutos[1])

if total > restantes:
    print('Deixa para amanha!')
else: 
    print('Farei hoje!')
