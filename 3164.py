# Outputs do URI estão errados, mudar o código caso corrijam
from math import ceil, floor

while True:
    try:
        total, multa = map(int, input().split())
        pesos = []  

        peso = input().split()

        for i in range(total):
            pesos.append(int(peso[i]))

        pesos.sort()

        if total % 2 == 0:
            if total % 4 == 0:
                q1 = pesos[int(total*0.25)]
                q3 = pesos[int(total*0.75)]
            else:
                q1 = pesos[int(total*0.25) + 1]
                q3 = pesos[int(total*0.75) - 1]
        else:
            q1 = pesos[floor(total*0.25)]
            q3 = pesos[ceil(total*0.75)]
        
        meio = q3 - q1
        # As próximas duas linhas deverão ser alteradas de 0.5 para 1.5 caso arrumem os outputs
        # A criatura caiu na pegadinha do meio + 50% de meio, que é 1.5*meio, e não 0.5*meio
        limite_q1 = q1 - 0.5*meio
        limite_q3 = q3 + 0.5*meio

        outliers = 0

        for peso in pesos:
            if peso < limite_q1:
                outliers += 1
            if peso > limite_q3:
                outliers += 1
        """ print(pesos)
        print('q1', q1)
        print('q3', q3)
        print('lim1', limite_q1)
        print('lim3', limite_q3) """

        print(outliers*multa)
        
    except EOFError:
        break
