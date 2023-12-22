# try, except, else e finally

try:
    print('ABRIR ARQUIVO')
    # 8/0
except ZeroDivisionError:
    print('DIVIDIU ZERO')
else: # Só é executado quando não ocorre nenhum erro
    print('NÃO DEU ERRO')
finally: # O finally sempre será executado
    print('FECHAR ARQUIVO')