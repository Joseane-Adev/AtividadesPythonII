

lugares_vagos = [10,2,1,3,0,20]
quantidade_vendas = [0,0,0,0,0,0]


#loop principal
while True:
    sala = int(input(f'Qual sala deseja entrar? (0 sai) : Tem {len(lugares_vagos)} salas: '))
    #condiçoes de saída e validação
    if sala == 0:
        print('Fim')
        break
    if sala > len(lugares_vagos) or sala < 1:
        print('Sala inválida')
    elif lugares_vagos[sala - 1] == 0:
        print('Sala lotada')
    else:
        #compra de ingressos
        lugares = int(input(f'Quantos lugares você deseja? ( Tem {lugares_vagos[sala - 1]} LUGARES VAZIOS)'))
        
        if lugares > lugares_vagos[sala - 1]:
            print('Esse numero de lugares não está disponível')
        elif lugares < 0:
            print('Numero inválido')
        else:
            lugares_vagos[sala - 1] -= lugares
            quantidade_vendas[sala - 1] += lugares 
            print(f'{lugares} lugares vendidos')

        
        
        #relatorio das salas
        print('----------------------------')
        print('Utilização das salas')

        for x, (vagos, vendidos) in enumerate(zip(lugares_vagos, quantidade_vendas)):
            print(f'Sala {x + 1} - {vagos} lugar(es) vazio(s) ---|---{vendidos} ingressos vendidos')