"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

print('LISTA DE COMPRAS')

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower()
    
    if opcao == 'i':
        os.system('cls')
        item_inserido = input('Item a adicionar: ')
        lista.append(item_inserido)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite um número int.')
        except IndexError: 
            print('Esse índice não existe na lista.')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Não há nada para listar')

        for i, item in enumerate(lista):
            print(i, item)
    else:
        print('Por favor, digite "i", "a" ou "l"')
