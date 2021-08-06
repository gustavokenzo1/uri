trips = input().split()

a = int(trips[0])
b = int(trips[1])
c = int(trips[2])

# 0 = presente

# Caso 1: duas trips, de mesmo valor (volta para o presente)
if (a-b == 0) or (a-c == 0) or (c-b == 0):
    print('S')

# Caso 2: três trips que voltam para o presente:
elif ((a+b) - c == 0) or ((a+c) - b == 0) or ((b+c) - a == 0):
    print('S')

# Caso 3: ir tantos anos para o futuro, voltar para o passado somando os outros 2 termos 
# e mesmo assim continuando no futuro
elif (a-b-c == 0) or (b-a-c == 0) or (c-b-a == 0):
    print('S')

else:
    print('N')
