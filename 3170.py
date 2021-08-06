# Árvore tem G branches, então precisa de G/2 marbles
# Se G for ímpar, arredondar pra baixo
# input 1: B = bolas já existentes
# input 2: G = branches
from math import floor

bolas = int(input())
branches = int(input())

if branches % 2 != 0:
    branches = floor(branches/2)
else: 
    branches /= 2

precisa = branches - bolas

if precisa > 0:
    print('Faltam ' + str(round(precisa)) + ' bolinha(s)')

else:
    print('Amelia tem todas bolinhas!')
