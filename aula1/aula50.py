"""
Exercício - Exiba os índices e valores da lista
0 - Maçã
1 - Banana
2 - Laranja
3 - Uva
"""

frutas = ['Maçã', 'Banana', 'Laranja', 'Uva']
frutas.append('Abacaxi')  # adiciona uma nova fruta ao final da lista

indices = range(len(frutas))  # cria um range de índices baseado no tamanho da lista

for indice in indices:
    print(f"Índice {indice}: {frutas[indice]} (Tipo: {type(frutas[indice])})")
