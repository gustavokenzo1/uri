# URI ERRADOOOOO
from numpy import mean, std
quantidade, multa = map(int, input().split())
pesos = []

peso = input().split()

for i in range(quantidade):
    pesos.append(int(peso[i]))

# Colocar em ordem crescente e calcular o tamanho
pesos = sorted(pesos)
media = mean(pesos, axis=0)
dp = std(pesos, axis=0)

menor = media - 2*dp
maior = media + 2*dp

# Quartil 1 são os valores até menos que 25% do total (inclusivo?)
q1 = int((quantidade + 1)/4)
# Quartil 3 são os valores acima de 75% do total
q3 = int((quantidade + 1)*3/4)

# O peso na posição dos quartis 1 e 3 é:
peso_q1 = pesos[q1]
peso_q3 = pesos[q3]

# Os outliers são valores fora do extremo dos quartis + ou - 1,5 da diferença de Q1 e Q3
# Outputs do URI estão errados
i = peso_q3 - peso_q1
lim_q1 = int(peso_q1 - 1.5*i)
lim_q3 = int(peso_q3 + 1.5*i)

""" print()
print(pesos)
print()
print(q1)
print(q3)
print()
print(peso_q1)
print(peso_q3)
print()
print(lim_q1)
print(lim_q3)
print() """

print(pesos)
print(menor)
print(maior)
outliers = 0
for i in pesos:
    if i < menor:
        outliers += 1
    if i > maior:
        outliers +=1

print(outliers*multa)

"""
Output do exemplo

[304295, 318756, 326952, 330056, 330061, 330544, 332191, 344292, 372976, 381282,
 386097, 387983, 395933, 400290, 402952, 407361, 413123, 413374, 424806, 425169, 
 431670, 435672, 450114, 453651, 464763, 466148, 466565, 468372, 470320, 472567,
  474019, *480924*, 484183, 486861, 488436, 496882, 503779, 507567, 511281, 512419, 
  516169, 518946, 525518, 533097, 536530, 538861, 545334, 547938, 552863, 557276, 
  559285, 560948, 563465, 564383, 569753, 575586, 578567, 581547, 585054, 587713, 
  588121, 591918, 592543, 595460, 597232, 602675, 602968, 606122, 609377, 616578, 
  629718, 630502, 630824, 640365, 644958, 647438, 650196, 650453, 658433, 662112, 
  662830, 669662, 669805, 670811, 671663, 675800, 686318, 687915, 691486, 692250, 
  692536, 694684, 695330, 707191, *708922*, 713625, 718326, 724519, 730177, 732920, 
  734208, 736512, 740911, 742504, 743645, 746834, 747738, 766020, 785591, 788451, 
  790490, 794537, 797989, 803743, 806957, 809345, 814395, 821822, 829583, 852958, 
  873597, 876572, 877885, 879872, 890146]

  31 abaixo 
  52 meio
  30 acima 
  Não está incluindo os próprios valores
  Os valores entre ** indicam os quartis 1 e 3, dps de fazer a conta e achar o lim_q1 e lim_q3, que seriam os valores máximos 
  para um valor não ser considerado outlier. Nenhum valor da lista é menor que lim_q1 ou maior que lim_q3
"""
