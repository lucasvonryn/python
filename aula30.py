"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60  # velocidade atual do carro
local_carro = 99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

passou_limite_vel_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and passou_limite_vel_radar_1

if passou_limite_vel_radar_1:
    print('Velocidade do carro passou do limite do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print('O carro foi multado pois passou no radar 1 acima da velocidade permitida')