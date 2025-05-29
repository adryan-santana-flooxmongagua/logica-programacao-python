"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Adr', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()  # cria uma cópia da lista_a

lista_a[0] = 'Qualquer coisa'  # altera apenas lista_a
print(lista_a)  # ['Qualquer coisa', 'Maria', 1, True, 1.2]
print(lista_b)  # ['Adr', 'Maria', 1, True, 1.2]


"""
Listas em Python
Tipo list – Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis – índices e fatiamento
Métodos úteis:
- append, insert, pop, del, clear, extend, +
- Create Read Update Delete
- Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# índices: 0 … 1 … 2 … 3 … 4 … 5
lista2 = [10, 20, 30, 40, 50, 60]
lista2[2] = 300  # altera o valor do índice 2 para 300
del lista2[2]    # deleta o elemento do índice 2
print(lista2)    # exibe a lista atualizada
print(lista2[2]) # exibe o novo valor no índice 2 após a deleção
