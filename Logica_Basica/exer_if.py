primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite um segundo valor: '))

#condição

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior que o {segundo_valor} segundo valor.')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor {segundo_valor} é maior que o {primeiro_valor} primeiro valor')
elif primeiro_valor == segundo_valor:
    print('Números iguais!')
else:
    print('Digite um numero válido')