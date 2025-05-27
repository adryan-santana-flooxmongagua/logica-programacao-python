nome = 'Lopez'
idade = 19
altura = 1.80
peso = 90
imc = peso / altura ** 2

# Usando f-strings para exibir as informações
linha_1 = f'{nome}, {idade} anos, tem {altura:.2f}m de altura,'
linha_2 = f'pesa {peso} kg e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
