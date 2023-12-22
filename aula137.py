# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome


class Motor:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.fabricante.nome, fusca.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.fabricante.nome,   gol.nome, gol.motor.nome)

palio = Carro('Palio')
fiat = Fabricante('Fiat')
motor_1_6 = Motor('1.6')
palio.fabricante = fiat
palio.motor = motor_1_6
print(palio.fabricante.nome, palio.nome, palio.motor.nome)

ranger = Carro('Ranger')
ford = Fabricante('Ford')
motor_3_2 = Motor('3.2')
ranger.fabricante = ford
ranger.motor = motor_3_2
print(ranger.fabricante.nome, ranger.nome, ranger.motor.nome)