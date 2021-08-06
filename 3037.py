rounds = int(input())
pontos_joao = 0
pontos_maria = 0

for i in range(rounds):
    for j in range(3):
        pontos = input().split()
        x = int(pontos[0])
        d = int(pontos[1])
        points = x*d
        pontos_joao += points
    for j in range(3):
        pontos = input().split()
        x = int(pontos[0])
        d = int(pontos[1])
        points = x*d
        pontos_maria += points

    if pontos_joao > pontos_maria:
        print("JOAO")
    else:
        print("MARIA")
    
    # Resetar para o próximo jogo, seu burro! aleluia, dps de vários erros
    pontos_joao = 0
    pontos_maria = 0
