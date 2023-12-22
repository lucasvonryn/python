# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
elif not senha:
    print('Você não digitou uma senha')
else:
    print('Senha incorreta')