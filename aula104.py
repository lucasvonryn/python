# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax sugar" (Açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'o seu resultado foi {resultado}')
        print('ok, você foi decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverte_string('123')
print(invertida)