import copy

from dados import produtos

# Exercícios
# Aumente os preços dos produtos as seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [
    {**produtos, 'preco': round(produtos['preco'] * 1.1)} 
    for p in produtos
]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)


# print(*produtos, sep='\n')
# print()
# print(*produto_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# FINAL
