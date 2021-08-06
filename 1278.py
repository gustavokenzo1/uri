repeticoes = 0

while True:
    linhas = int(input())

    if linhas == 0:
        break

    if repeticoes >= 1:
        print() # VAMO PORRAAAAAAA DPS DE 17 ENVIOS!!! ESPAÇO FDP

    repeticoes += 1
    tamanho = 0
    frases = []

    for i in range(linhas):
        texto = input().split()
        text = ' '.join(texto)
        frases.append(text)

        if len(text) > tamanho:
            tamanho = len(text)

    for i in range(len(frases)):
        if len(frases[i]) < tamanho:
            espaços = tamanho - len(frases[i])
            print((' '*espaços + frases[i]).rstrip()) # Tirar todos os espaços dps da última letra
        else:
            print((frases[i]).rstrip())

    
