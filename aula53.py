"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Lucas'), (1, 'Ewelin'), (2, 'Carol'), (3, 'Milena'), (4, 'Silvana'), (5, 'Nilza')]
lista = ['Lucas', 'Ewelin', 'Carol', 'Milena', 'Silvana']
lista.append('Nilza')

# lista_enumerada = enumerate(lista)
# print(lista_enumerada)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)