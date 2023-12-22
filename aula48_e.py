"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Lucas'
# outra_variavel = nome
# nome = 'Luiz'
# print(nome)
# print(outra_variavel)

lista_a = ['Lucas', 'Ewelin']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)
print(lista_a)