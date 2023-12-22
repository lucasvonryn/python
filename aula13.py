# f-strings são as formatações de strings
# podem ser feitas de vários modos, inclusive
# utilizando o .format

nome = 'Lucas'
altura = 1.80
peso = 69.5
imc = peso / (altura ** 2)

# print(f'{nome} tem {altura} de altura,')
# print(f'pesa {peso} quilos e seu IMC é')
# print(imc)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc}'
print(linha_1)
print(linha_2)
print(linha_3)
