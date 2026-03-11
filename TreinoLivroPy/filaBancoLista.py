#SIMULAÇAO DE FILA DE BANCO
ultimo = 0
fila = list(range(1, ultimo + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite 1 para adicionar um cliente à fila')
    print('2 para realizar atendimento ou 3 para sair da fila')

    operador = input('Qual atendimento deseja? ( 1 | 2 | 3 ): ')
    if operador == '1':
        ultimo += 1
        fila.append(ultimo)
    elif operador == '2':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido!')
        else:
            print('Fila vazia!')
    elif operador == '3':
        print('Você saiu da fila!')
        break

    else:
        print('Operação inválida!Digite um dos numeros : 1 | 2 | 3')