#sem usar partial
import operator
import math
from functools import partial
'''
def executa(operacao, simbolo, numero1, numero2):
    resultado = operacao(float(numero1), float(numero2))
    print(f'O resultado de: {numero1} {simbolo} {numero2} é: {resultado}')

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo numero: ')
simbolo = input('Digite o operador: ').strip()

if simbolo == '+':
    executa(operator.add, simbolo, numero1, numero2 )
elif simbolo == '-':
    executa(operator.sub, simbolo, numero1, numero2)
elif simbolo == '*':
    executa(operator.mul, simbolo, numero1, numero2)
elif simbolo == '/':
    executa(operator.truediv, simbolo, numero1, numero2)
else:
    print('Digite um operador válido')

'''
#com partial
def executa(operacao, simbolo, numero1, numero2):
    resultado = operacao(float(numero1), float(numero2))
    print(f'O resultado de: {numero1} {simbolo} {numero2} é: {resultado}')

operaçoes = {
    '+': partial(executa, operator.add, '+'),
    '-': partial(executa, operator.sub, '-'),
    '*': partial(executa, operator.mul, '*'),
    '/': partial(executa, operator.truediv, '/'),
    '**':partial(executa, operator.pow, '**' ),
    '%': partial(executa, operator.mod, '%')
}

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo numero: ')
simbolo = input('Digite o operador: ').strip()

if simbolo in operaçoes:
    operaçoes[simbolo](numero1, numero2)
else:
    print('operação inválida')

number = math.ceil(3.253)
print(number)

number2 = math.trunc(3.423)
print(number2)

