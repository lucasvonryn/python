# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(f'{chave.capitalize()}: {valor}')

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Gabriel Von Ryn',
}

dados_da_pessoa = {
    'idade': 18,
    'altura': 1.8,
}

dados_completos_pessoa = {
    **pessoa,
    **dados_da_pessoa
}
# print(dados_completos_pessoa)

# args e kwargs
# args (já vimos)
# kwargs - keywords arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    
    for chave, valor in kwargs.items():
        print(f'{chave.capitalize()}: {valor}')

mostro_argumentos_nomeados(nome='Joana', idade='18')