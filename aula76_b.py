# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Lucas'
pessoa['sobrenome'] = 'Gabriel'

print(pessoa['nome'])

pessoa['nome'] = 'Maria'


del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('não existe')
else:
    print(pessoa['sobrenome'])
