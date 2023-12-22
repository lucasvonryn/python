# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('divizão por zero.')
    return True

def so_aceito_int_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(n, d):
    so_aceito_int_float(n)
    so_aceito_int_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(9, '0'))