# Vírus:
# adicionou letras nos lados dos nomes das input
# mudou a case de algumas letras
# inverteu as letras da palavra

x = input().split()
fruta = int(x[0])
linhas = int(x[1])
fruta_list = []
frutas = []
lista = []

for i in range(fruta):
    fruit = input().lower()
    invert_fruit = fruit[::-1] # end : finnish : steps
    frutas.append(invert_fruit)
    fruta_list.append(fruit)

for i in range(linhas):
    linha = input().lower()
    lista.append(linha)
    
lista_str = ''.join(map(str, lista))

for i in range(fruta):
    if frutas[i] in lista_str or fruta_list[i] in lista_str:
        print('Sheldon come a fruta ' + fruta_list[i])
    else:
        print('Sheldon detesta a fruta ' + fruta_list[i])
