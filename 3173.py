# Questão estranha. Não considera os anos bissextos corretamente, apenas os que quando divididos por 4 dão resto 0.
# Sendo que deveria ser ano % 4 == 0 and ano % 100 != 0 OU ano % 400 == 0

from datetime import date, datetime, timedelta
from math import ceil, floor

ciclos = int(input())

# Júpiter: 11.9 At
# Saturno: 29.6 At
# 1 At = 365 dias (contar bissextos)
# Exemplo: dias júpiter: 11.9*365 = 4343,5 + 3 dias de anos bissextos = 4346 (arredondando o dia)

# Anos terrestres para 'n' ciclos de cada planeta
at_jupiter = 11.9 * ciclos
at_saturno = 29.6 * ciclos

# Número de anos bissextos 
leap_j = 0
leap_s = 0

# Ano bissexto: divisível por 4 e não por 100, ou de 400
# Ano inicial: 2021, pois 2020 já estava em dezembro, e já havia passado o dia extra de fevereiro
# Obs.: Caso dê erro, verificar se o autor da questão pode não ter considerado isso
# Arredondar pra cima, pq o ano não está completo mas já é esse ano, e somar 1 pq não é inclusivo
for i in range(2021, 2021 + ceil(at_jupiter) + 1):
    if i % 4 == 0:
        leap_j += 1
    """ elif i % 400 == 0:
        leap_j += 1 """

for i in range(2021, 2021 + ceil(at_saturno) + 1):
    if i % 4 == 0: 
        leap_s += 1
    """ elif i % 400 == 0:
        leap_s += 1 """

data = datetime(2020, 12, 21)
# Arredondar para baixo, pois o dia não está completo
dias_jupiter = floor(at_jupiter*365 + leap_j)
dias_saturno = floor(at_saturno*365 + leap_s)

# Guardar o mês e o ano futuro, pois se o mês for menor que 3, e for ano bissexto,
# devemos subtrair o dia extra que o for loop contou
mes_j = (data + timedelta(dias_jupiter)).month
mes_s = (data + timedelta(dias_saturno)).month
ano_j = (data + timedelta(dias_jupiter)).year
ano_s = (data + timedelta(dias_saturno)).year

# Por algum motivo a questão considera o 3 na condição (?)
if mes_j <= 3 and (ano_j % 4 == 0 and ano_j % 100 != 0) or (ano_j % 400 == 0):
    dias_jupiter -= 1

if mes_s <= 3 and (ano_s % 4 == 0 and ano_s % 100 != 0) or (ano_s % 400 == 0):
    dias_saturno -= 1

# Achar o delta T 
data_jupiter = data + timedelta(dias_jupiter)
data_saturno = data + timedelta(dias_saturno)

print("Dias terrestres para Jupiter =", dias_jupiter)
print("Data terrestre para Jupiter:", data_jupiter.date())
print("Dias terrestres para Saturno =", dias_saturno)
print("Data terrestre para Saturno:", data_saturno.date())
