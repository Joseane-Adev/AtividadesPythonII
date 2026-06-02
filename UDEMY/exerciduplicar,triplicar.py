#função que duplica, triplica e  quadruplicam o numero recebido como parametro
'''
def duplicar(numero):
    return numero * 2
def triplicar(numero):
    return numero * 3
def quadruplica(numero):
    return numero * 4

print(duplicar(2))
print(triplicar(3))
print(quadruplica(5))

'''
numero = int(input('Qual numero deseja multiplicar? '))
multiplicador = int(input('Por qual numero quer multiplicar? '))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

multiplicar = criar_multiplicador(multiplicador)
print(multiplicar(numero))

