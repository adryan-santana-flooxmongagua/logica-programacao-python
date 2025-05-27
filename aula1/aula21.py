# Operadores lógicos
# -------------------
# and (e), or (ou), not (não)
#
# - and: todas as condições precisam ser verdadeiras.
#        Se qualquer valor for considerado falso,
#        a expressão inteira será avaliada naquele valor.
#
# Valores considerados "falsy" (falsos):
# - 0, 0.0, '', False
# - Também existe o tipo None, que representa a ausência de valor.

# Exemplo com entrada de usuário:
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True)  # False (primeiro False interrompe)
print(True and 0 and True)      # 0 (0 é "falsy", interrompe avaliação)
