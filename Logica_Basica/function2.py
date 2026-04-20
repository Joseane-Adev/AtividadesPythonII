#nomeando função
def palavra():
    print('palavra')

palavra()

def numeros(a, b):#parametros
    calculo = a * b
    print(f'O valor de {a} * {b} é: {calculo}')

numeros(2,3)#argumentos

#argumento nomeado ( tem nome)
def soma(x, y):#definição de função
    print(f'{x=} {y=} = {x + y}')

soma(x=2, y=8)#argumneto nomeado
#sempre que nomear um argumento precisa nomear os outros

#argumento não nomeado(sem nome)
#argumento na mesma ordem
soma(1, 2)

