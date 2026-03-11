'''
Constantes e Variáveis em Python
 constantes = não mudam o valor
 variaveis = mudam o valor

'''

velocidade = 30 

local_carro = 100

RADAR = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou = velocidade > RADAR
carro_passou_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_radar and  velocidade_carro_passou

if velocidade_carro_passou > RADAR:
    print('Velocidade passou do radar')
if carro_passou_radar:
    print('carro passou no radar')
if carro_multado:
            print('carro multado')


