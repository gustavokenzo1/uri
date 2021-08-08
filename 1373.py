# DNA SUBSEQUENCES
# Calcular a maior subsequence de um par de strings
# Considerar um alfabeto 'S' de letras e 1 palavra
# Uma subsequence 'x' é um segmento de 'w'
# lovely: 'ove' é um segmento de lovely
# 'loly' é uma subsequence de lovely, mas não é um segmento
# uma w é uma subsequence comum de duas palavras w1 e w2 se for uma 
# subsequence de cada uma delas
# a maior subsequence dessas duas palavras é a subsequence de maior tamanho (óbvio)
# w1 = lovxxelyxxxxx,  w2 = xxxxxxxlovely, w3 = lovely, w4 = xxxxxxx 
# w3 e w4 são ambos subsequences comums de w1 e w2, e w4 é a subsequence comum mais longa (7)
# A subsequence deve ser formada de segmentos comums de, pelo menos, tamanho K.
# Ex.: Se K = 3
# lovxxelyxxxxx, xxxxxxxlovely
# lovely é aceito como uma subsequence comum, porém xxxxxxx, que também é uma 
# subsequence, não é aceito.

# q q ta acontecendo mds

# IMPOSSIVEL DO URI ACEITAR SAPORRA (TIME LIMIT EXCEEDED)

while True:
    k = int(input())

    if k == 0 or k < 1 or k > 100:
        break
    
    l1 = input()
    l2 = input()

    n, m = len(l1), len(l2)

    # Criar uma array para guardar o tamanho da maior subsequence comum
    lcs = [[0]*(m+1) for z in range(n+1)]
    # Criar uma array para contar o tamanho do segmento comum
    count = [[0]*(m+1) for z in range(n+1)]

    # Algoritmo de Longest Common Sequence
    # Percorrer a matriz formada pelas duas strings
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Pegar o maior valor entre os valores da esquerda e de cima
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

            # Se os caracteres forem iguais, somar 1 na diagonal
            if (l1[i - 1] == l2[j - 1]):
                count[i][j] = count[i - 1][j - 1] + 1

            # Se o tamanho do segmento comum for maior que k, atualizar a array lcs 
            if count[i][j] >= k:
                for a in range(k, count[i][j] + 1):
                    lcs[i][j] = max(lcs[i][j], lcs[i - a][j - a] + a)

    print(lcs[n][m])
