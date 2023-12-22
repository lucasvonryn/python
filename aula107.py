# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
def zipper(l1, l2):
    qtd_indices_menor_lista = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(qtd_indices_menor_lista)]
# from itertools import zip_longest

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
lista_atualizada = list(zipper(lista1, lista2))
# print(list(zip_longest(lista1, lista2, fillvalue='SEM CIDADE')))

for cidade in lista_atualizada:
    for estado in cidade:
        print(estado)