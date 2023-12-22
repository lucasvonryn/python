# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1, 6}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET', end=' ')
        item.add(7)
        print(item, isinstance(item, set))
    elif isinstance(item, str):
        print('STR', end=' ')
        print(item.upper())
    elif isinstance(item, (int, float)):
        print('NUM', end=' ')
        print(item, item * 2)
    else:
        print('OUTRO', end=' ')
        print(item)