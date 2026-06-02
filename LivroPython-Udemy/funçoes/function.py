#declarar funçao
def multiplica(a,b):
    #print(f'A multiplicação de {a} X {b} é: {a * b}')
    return a * b
print(multiplica(10,5))

#retorna se é par ou impar

x = int(input('Digite um numero: '))

def numero(x):
    if x % 2 == 0:
        return 'É par'
    else:
        return 'É impar'

print(numero(x))

#exercicios retorne o maior de dois numeros

a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor'))

def numeros(a,b):
    if a > b:
        return 'maior numero é: ',a
    else:
        return 'Maior numero é: ' ,b

print(numeros(a,b))

#exercicios receber dois numeros e retorna TRue se o primeiro numero for multiplo do segundo

x =int(input('Digite o primeiro numero: ')) 
y =int(input('Digite o segundo numero: '))

def multiplo(x, y):
    if y == 0:
        return 'Não é possível dividir por 0'
    elif x % y == 0:
        return True
    else:
        return False

print(multiplo(x,y))

#retornar o lado de um quadrado

lado = int(input('Digite um lado do quadrado: '))

def area(lado):
    A = lado ** 2 #elevado ao quadrado é lado x lado
    return A
print(f'A área do quadrado é: {area(lado)}')

#exercio  retornar a base e altura de um triangulo e retornar a area

base = int(input('Digite a base do triângulo: '))
altura = int(input('Digite a altura do triângulo: '))

def calculaArea(base, altura):
    area = (base * altura) / 2
    return area

print(f'A área do triãngulo é: {calculaArea(base,altura):.0f}')

