number1 = int(input('Digite o primeiro numero: '))
number2 =int(input('Digite o segundo numero: '))

resultado = 0

contador = 0

while contador < number2:
    resultado += number1
    contador += 1


print(f'Multiplicação de {number1} * {number2} = {resultado}')


