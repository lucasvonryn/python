"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[:3])
print(variavel[4:])
print(len(variavel))
print(variavel[:len(variavel):2]) # a função len retorna o tamanho da string
print(variavel[::-1]) # variável invertida
