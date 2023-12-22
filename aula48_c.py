"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append(1001)
lista.append('Lucas')
nome = lista.pop()
# del lista[-1]
# lista.clear()
lista.insert(0, 5)
print(lista, nome)
print(lista[0])
lista.insert(5, 'Gabriel')
sobrenome = lista[5]
print(f'{nome} {sobrenome}')