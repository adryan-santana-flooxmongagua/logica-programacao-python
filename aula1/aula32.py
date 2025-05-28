"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Digite um número: ')

try:
    entrada_int = int(entrada)
    par_impar_texto = 'par' if entrada_int % 2 == 0 else 'ímpar'
    print(f'O número {entrada_int} é {par_impar_texto}')
except ValueError:
    print('Você não digitou um número inteiro')

print()  # Separador visual para o próximo exercício

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)
    if 0 <= hora <= 11:
        print('Bom dia')
    elif 12 <= hora <= 17:
        print('Boa tarde')
    elif 18 <= hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except ValueError:
    print('Por favor, digite apenas números inteiros')

print()  # Separador visual para o próximo exercício

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif 5 <= tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
