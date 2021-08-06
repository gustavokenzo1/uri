from math import sqrt

ponto1 = input().split(' ')
x1 = float(ponto1[0])
y1 = float(ponto1[1])

ponto2 = input().split(' ')
x2 = float(ponto2[0])
y2 = float(ponto2[1])

# Ordem não importa, pois está elevado ao quadrado
delta_x = (x2 - x1)**2 
delta_y = (y2 - y1)**2

distance = sqrt(delta_x + delta_y)
print(round(distance, 4))
