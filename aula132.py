# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # private protected public
        self._cor = cor
        self._cor_tampa = None
        self._cor_tinta = None
        self._espessura = None

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

    @property
    def cor_tinta(self):
        return self._cor_tinta

    @cor_tinta.setter
    def cor_tinta(self, valor):
        self._cor_tinta = valor

    @property
    def espessura(self):
        return self._espessura

    @espessura.setter
    def espessura(self, valor):
        self._espessura = valor


caneta = Caneta('Azul')
caneta.cor = 'Transparente'
caneta.cor_tampa = 'Azul'
caneta.cor_tinta = 'Preta'
caneta.espessura = 2
print(f'Cor da caneta: {caneta.cor}')
print(f'Cor da tampa da caneta: {caneta.cor_tampa}')
print(f'Cor da tinta da caneta: {caneta.cor_tinta}')
print(f'Espessura da caneta: {caneta.espessura} mm')