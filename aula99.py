# from sys import path

# import aula99_package.modulo
# from aula99_package import modulo
# # from aula99_package.modulo import soma_do_modulo
# from aula99_package.modulo import *

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# from aula99_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# # fala_oi()

import aula99_package

from aula99_package import soma_do_modulo, falar_oi

print(soma_do_modulo(10, 20))
falar_oi()
