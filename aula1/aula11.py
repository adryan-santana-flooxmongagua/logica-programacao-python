# Ordem de Precedência dos Operadores Aritméticos em Python:
#
# 1. Parênteses ( )
#    - Tudo que está dentro dos parênteses é resolvido primeiro.
#
# 2. Exponenciação **
#    - Operação de potência, como elevar um número a outro.
#
# 3. Multiplicação, Divisão, Divisão Inteira e Módulo (*, /, //, %)
#    - Depois da exponenciação, vêm essas operações.
#    - São resolvidas da esquerda para a direita.
#
# 4. Adição e Subtração (+, -)
#    - São as últimas a serem resolvidas, também da esquerda para a direita.



conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

# Exemplo 1: uso de parênteses para controlar a ordem
resultado_1 = (2 + 3) * 4
print(resultado_1)  # 20

# Exemplo 2: exponenciação antes de multiplicação
resultado_2 = 2 * 3 ** 2
# 3**2 = 9, depois 2*9 = 18
print(resultado_2)  # 18

# Exemplo 3: várias operações na mesma expressão
resultado_3 = 10 + 2 * 3 ** 2
# 3**2 = 9, depois 2*9 = 18, depois 10+18 = 28
print(resultado_3)  # 28

# Exemplo 4: divisão e resto
resultado_4 = 10 / 3
resultado_5 = 10 // 3
resultado_6 = 10 % 3
print(resultado_4)  # 3.333...
print(resultado_5)  # 3 (divisão inteira)
print(resultado_6)  # 1 (resto)

# Exemplo 5: adição e subtração com multiplicação
resultado_7 = 5 + 3 * 2 - 4
# 3*2=6, depois 5+6=11, depois 11-4=7
print(resultado_7)  # 7

# Exemplo 6: misturando tudo
resultado_8 = (1 + 2) * (3 + 4) ** 2 // 5
# (1+2)=3, (3+4)=7, 7**2=49, 3*49=147, 147//5=29
print(resultado_8)  # 29
