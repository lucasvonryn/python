"""
Exercício
Exiba os índices da lista
0 Lucas
1 Ewelin
2 Carol
"""
lista = ['Lucas', 'Ewelin', 'Carol', 'Milena', 'Silvana']
lista.append('Nilza')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])