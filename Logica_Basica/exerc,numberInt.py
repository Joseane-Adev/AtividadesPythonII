'''
O programa pede ao usuario para digitar um numero inteiro
as condiçoes verificam se o numero é dividido por 2  com resto 0,
então é o par, se não é ímpar.
O except trata o erro de nao ser um numero inteiro.
'''
try: 
    number = int(input('Digite um numero: '))

    if number % 2 == 0:
        print('O numero é par')
    else:
        print('o numero é impar')
except:
    print('Digite um  numero inteiro ')