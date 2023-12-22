"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# def somar_listas(lista1, lista2):
#     qtd_indices_menor_lista = min(len(lista1), len(lista2))
#     return [(lista1[i] + lista2[i]) for i in range(qtd_indices_menor_lista)]

# lista_soma = []
# qtd_indices_menor_lista = min(len(lista_a), len(lista_b))
# for i in range(qtd_indices_menor_lista):
#     lista_soma.append(lista_a[i] + lista_b[i])
from itertools import zip_longest 

def somar_listas(lista1, lista2):
    lista_soma = [x + y for x, y in zip_longest(lista1, lista2, fillvalue=0)]
    return lista_soma

lista_soma = somar_listas(lista_a, lista_b)
print(lista_soma)