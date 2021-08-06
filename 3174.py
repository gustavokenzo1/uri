from math import floor

elves = int(input())
total = 0
bonecos = 0
arquitetos = 0
musicos = 0
desenhistas = 0

for i in range(elves):
    dados = input().split()
    # papai noel tá cagando pro nome
    toy = dados[1]
    hours = int(dados[2])

    # boneco: 8
    # arquitetos: 4
    # musicos: 6
    # desenhistas: 12

    # Podem ter mais elfos para uma mesma tarefa, 2 elfos juntos podem 
    # ter tempo sobrando para ainda mais brinquedos
    # melhor juntar todas as horas disponíveis para depois dividir pelo tempo de cada 
    
    if toy == 'bonecos':
        bonecos += hours
    
    if toy == 'arquitetos':
        arquitetos += hours
    
    if toy == 'musicos':
        musicos += hours

    if toy == 'desenhistas':
        desenhistas += hours

# Arredondar para baixo antes, se n fica zuado
total = floor(bonecos/8) + floor(arquitetos/4) + floor(musicos/6) + floor(desenhistas/12)
print(total)
