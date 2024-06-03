nome = 'Matheus Fonseca'
altura = 1.72
peso = 52
imc = ... # IMC = peso / (altura x altura)
imc = peso / altura ** 2
"f-strings"
linha_1 = f'{nome} tem {altura:,.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)
# Matheus Fonseca tem 1.72  de altura
# pesa 95e seu IMC é
# 17.577068685776098 