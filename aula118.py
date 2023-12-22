# Problemas dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

clientes1 = adiciona_clientes('Lucas')
adiciona_clientes('Marcos', clientes1)
adiciona_clientes('Fernando', clientes1)
clientes1.append('Eduardo')

clientes2 = adiciona_clientes('Olivia')
adiciona_clientes('Tadeu', clientes2)

clientes3 = adiciona_clientes('Rodrigo')
adiciona_clientes('Jesus', clientes3)

print(clientes1)
print(clientes2)
print(clientes3)