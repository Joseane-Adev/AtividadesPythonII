
while True:

    
    number1 = int(input('Digite o primeiro número: '))
    number2 = int(input('Digite o segundo número: '))
    operador =input('Qual operador deseja usar ( + - * / ) ?: ')

    if operador == '+':
        print(f'{number1} + {number2} = {number1 + number2}')
    elif operador == '-':
        print(f'{number1} - {number2} = {number1 - number2}')
    elif operador == '*':
        print(f'{number1} * {number2} = {number1 * number2}')
    elif operador == '/':
        print(f'{number1} / {number2} = {number1 / number2}')
    else:
        print('Digite um operador!')
    
    sair = input('Deseja sair? Sim ou Não: ')
    if sair == 'Sim':
        print('Você saiu do programa')
        break
    else:
        continue