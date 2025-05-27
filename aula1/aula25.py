"""
Interpolação básica de strings com o operador % em Python
---------------------------------------------------------

A interpolação de strings com o operador % funciona de maneira
parecida com a função printf de outras linguagens como C. Você
usa "marcadores" especiais dentro da string e, em seguida,
passa os valores que vão preencher esses marcadores.

Marcadores mais comuns:
- %s : string (texto)
- %d ou %i : inteiro (int)
- %f : ponto flutuante (float)
- %x ou %X : hexadecimal (x = minúsculo, X = maiúsculo)

Exemplos abaixo:
"""

nome = 'Luiz'
preco = 1000.95897643

# Interpolação com marcador %s para string e %.2f para float formatado com 2 casas decimais
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

# Exemplo com inteiro (%d) e hexadecimal (%X) formatado com 8 dígitos (zero à esquerda)
print('O hexadecimal de %d é %08X' % (1500, 1500))

"""
Resumo:
- O operador % permite inserir valores dentro de strings, de forma controlada e formatada.
- Depois da string, usamos o operador % e passamos uma tupla (com vírgula e parênteses)
  contendo os valores que queremos interpolar.
- Cada marcador de formatação (%s, %d, %.2f, %X etc.) define como o valor correspondente
  será exibido no resultado final.
"""

