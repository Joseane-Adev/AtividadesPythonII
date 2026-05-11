def valida_inteiro(msg,minimo,maximo):
    while True:
        try:
            valor = int(input(msg))
            if valor >= minimo and valor <= maximo:
                return valor
            else:
                print(f'Digite um valor entre{minimo} e {maximo}')

        except ValueError:
            print('Você deve digitar um numero inteiro')
