# Permutação de termos
# em python não precisa de uma variável 'temp' para armazenar o valor pq python é roubado

moves = int(input())
start = input()
pos = [0, 0, 0]

if start == 'A':
    pos[0] = 1

if start == 'B':
    pos[1] = 1

if start == 'C':
    pos[2] = 1

for i in range(moves):
    mover = int(input())
    if mover == 1:
        pos[0], pos[1] = pos[1], pos[0]
        
    if mover == 2:
        pos[1], pos[2] = pos[2], pos[1]

    if mover == 3:
        pos[2], pos[0] = pos[0], pos[2]

for i in range(len(pos)):
    if pos[i] == 1:
        if i == 0:
            print('A')
        if i == 1:
            print('B')
        if i == 2:
            print('C')
