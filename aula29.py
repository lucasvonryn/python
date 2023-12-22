"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Digite um numero para ver o seu dobro: ')

try: # tenta executar o código que vem dentro
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except: # se ocorrer erro dentro do try, vem para o except
    print(f'Você não digitou um número')

# if numero_str.isdigit(): # pergunta se é um digito ou não
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print(f'Você não digitou um número')