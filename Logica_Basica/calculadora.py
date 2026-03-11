'''
Calculadora com while

'''
while True:

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operador = input('Digite o operador (+  -  *  / ): ')

    if operador == '+':
        print(f'Sua soma de {num1} + {num2} = {num1 + num2}')
    elif operador == '-':
        print(f'o resultado da subtração de : {num1} - {num2} = {num1 - num2}')
    elif operador == '*':
        print(f'O resultado da multiplicação de: {num1} * {num2} = {num1 * num2}')
    elif operador == '/':
        print(f'O resultado da divisão de: {num1} / {num2} = {num1 / num2}')
    else:
        print('Digite um operador válido!')


    sair = input('Você quer sair? (s/n):')
    if sair == 's':
        print('Você saiu!')
        break
    else: 
        continue