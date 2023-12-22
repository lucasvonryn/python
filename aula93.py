# Try, except, else e finally
# a = 18
# b = 0
# c = a / b
# b = 0
# print(b[0])

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
# except ZeroDivisionError:
#     print('Dividiu por zero')
# except NameError:
#     print('Nome b não está definido')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('Mensagem:', error)
#     print('Nome:', error.__class__.__name__)
except Exception as error:
    print('Nome do erro:', error.__class__.__name__)

print('CONTINUAR')