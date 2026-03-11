while True:

    operador = input('Escolha um operador: (+ - * /): ')
    valor = int(input('Digite qual numero deseja ver a tabuada: '))

    numero = 0
    while numero <= 10:
        if operador == '+':
                print(f'{numero} + {valor} = {numero + valor}')
        elif operador == '-':
            print(f'{numero} - {valor} = {numero - valor}')
        elif operador == '*':
            print(f'{numero} * {valor} = {numero * valor}')
        elif operador == '/':
                print(f'{numero} / {valor} = {numero / valor}')
        else:
             print('Digite um operador válido!')
    
    
        numero += 1
    valor += 1

    sair = input('Deseja sair? S/ N: ')
    if sair == 'S':
         print('Você saiu da calculadora!')
         break
    else: 
         print('Vamos continuar calculando!')
         continue
         
    



    


    


    
       