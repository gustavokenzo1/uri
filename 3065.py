total = 1
while True:
    sinais = []
    nums = int(input())
    if nums == 0:
        break

    # Tirar os sinais para guardar apenas os números
    conta = input()
    filtro_nums = conta.replace('+',' ').replace('-',' ').split()

    # Transformar as strings em ints
    for i in range(len(filtro_nums)):
        filtro_nums[i] = int(filtro_nums[i])
    
    # URI fala que só serão passados sinais e números, então se um char não for numérico,
    # ele deverá ser um sinal
    for i in range(len(conta)):
        if not conta[i].isnumeric():
            sinais.append(conta[i])

    # Começar a conta já com o primeiro número
    soma = filtro_nums[0]
    
    for i in range(len(sinais)):
        if sinais[i] == '+':
            soma += filtro_nums[i + 1] # Se houver um sinal de "+", somar com o próximo número
        else:
            soma -= filtro_nums[i + 1] # Análogo

    print('Teste ' + str(total))
    print(soma)
    print() # Morra presentation error
    total += 1
