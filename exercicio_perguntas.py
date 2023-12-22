perguntas = [
    {
        'Pergunta': 'Quanto é 10 + 10?',
        'Opções': ['10', '20', '30', '40'],
        'Resposta': '20',
    },
    {
        'Pergunta': 'Quanto é 10 - 100?',
        'Opções': ['10', '100', '-90', '-110'],
        'Resposta': '-90',
    },
    {
        'Pergunta': 'Qual é o nome do livro mais vendido do mundo?',
        'Opções': ['Dicionário', 'O Pequeno Principe', 'Bíblia', 'Os Miseráveis'],
        'Resposta': 'Bíblia',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')

    print()

    escolha = input('Escoha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <= qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')
    
    print()

print('Acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas')