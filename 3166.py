palavras, linhas, colunas = map(int, input().split())

words = []
rev_words = []

# Guardar as palavras e seus inversos
for i in range(palavras):
    palavra = input().lower()
    words.append(palavra)
    rev_words.append(palavra[::-1])

menor = len(min(words, key=len))
text = []

for i in range(linhas):
    texto = input().lower()
    text.append(texto)

max_col = len(text[0])
max_row = len(text)
fdiag = [[] for i in range(max_row + max_col - menor)]
bdiag = [[] for i in range(len(fdiag))]
min_bdiag = -max_row + 1

for i in range(max_col):
    for j in range(max_row):
            bdiag[i - j - min_bdiag - menor + 1].append(text[j][i])
    
for i in range(len(bdiag)):
    bdiag[i] = ''.join(bdiag[i])

temp = []
bdiag.append('')
for i in range(len(bdiag)):
    if len(bdiag[i]) == menor and len(bdiag[i + 1]) == menor:
        temp.append(bdiag[i])
        break
    temp.append(bdiag[i])

maiores = []
for i in range(len(temp)):
    if colunas > linhas:
        if len(temp[i]) == linhas:
            maiores.append(i)
    else:
        if len(temp[i]) == colunas:
            maiores.append(i)

principal = 0
if colunas > linhas:
    principal = maiores[0]

elif linhas > colunas:
    principal = maiores[len(maiores) - 1]

else:
    principal = maiores[0]

for i in range(len(words)):
    for j in range(len(temp)):
        if j < principal:
            if words[i] in temp[j] or rev_words[i] in temp[j]:
                print('3 Palavra "' + words[i] + '" abaixo da diagonal principal')
                break

        elif j == principal:
            if words[i] in temp[j] or rev_words[i] in temp[j]:
                print('1 Palavra "' + words[i] + '" na diagonal principal')
                break
        
        elif j > principal:
            for k in range(len(temp)):
                if words[i] in temp[k] or rev_words[i] in temp[k]:
                    print('2 Palavra "' + words[i] + '" acima da diagonal principal')
                    break
            else:
                print('4 Palavra "' + words[i] + '" inexistente')
            break

""" Para me guiar
A z C d Z f G h
I a B c D e Z z
Z z A b C d E f
K j I Z B z Z e

Z z Z d
I a B c
Z i A b
K j I a
Z k J z
M l K j
Z m L z
O n Z l

"""

