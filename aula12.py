nome = 'Lucas'
altura = 1.80
peso = 69.5
imc = peso / (altura ** 2)

# print(f'{nome} tem {altura} de altura,')
# print(f'pesa {peso} quilos e seu IMC é')
# print(imc)

print('{} tem {} de altura,'.format(nome, altura))
print('pesa {} quilos e seu IMC é'.format(peso))
print('{}'.format(imc))