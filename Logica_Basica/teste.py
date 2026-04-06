while True:
    n1 = int(input("Primeiro número: "))
    n2= int(input('Segundo número: '))
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Comparar numeros
    ''')
    op =int(input('Qual o operador?  '))
    if op == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif op == 2 :
        mul = n1 * n2
        print(f'{n1} * {n2} = {mul}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')

    sair = input('Deseja sair? [S]sim [N]não? ').strip().upper()
    if sair == 's':
        print('Você saiu do programa!')
        break
    else:
        continue
