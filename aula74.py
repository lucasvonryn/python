"""
Closure e funções que retornam outras funções
"""

def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao} {nome}!'
    return saudar

falar_bom_dia = saudacao('Bom dia')
falar_boa_noite = saudacao('Boa noite')

for nome in ['Lucas', 'Ewelin', 'Carol', 'Milena', 'Silvana']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
