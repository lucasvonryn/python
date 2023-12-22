# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Gabriel',
    'idade': 900,
}

pessoa.setdefault('idade', None)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys())[0])
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for value in pessoa.values():
#     print(value)

# for chave, valor in pessoa.items():
#     print(chave, valor)