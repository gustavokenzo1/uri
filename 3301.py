idades = input().split()

h = idades[0]
z = idades[1]
l = idades[2]

if z < h < l or l < h < z:
    print('huguinho')

elif l < z < h or h < z < l:
    print('zezinho')

else:
    print('luisinho')
