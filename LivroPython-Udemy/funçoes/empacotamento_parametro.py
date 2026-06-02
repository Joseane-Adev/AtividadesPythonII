def soma(a,b):
    print(a+b)

lista = [2,3]
soma(*lista)#estou desempacotando a lista, usando os valores como parametro.

def barra(n=10, c='*'):
    print(c * n)

l = [[5,'-'], [10, '*'], [5], [6, '.']]

for x in l:
    barra(*x)# desempacotando os valores da lista

# Função soma com numero indeterminado de parametros

def calculo(*args):
    contador = 0
    for x in args:
        contador += x
    return contador

print(calculo(10,5,2))

#imprime maior coom numero inderteminado de parametros

def imprime_maior(msg, *numeros):
    maior = None #não tem valor definido
    for i in numeros:
        if maior is None or maior < i:
            maior = i
    print(msg, maior)

imprime_maior('O numero maior é:', 5,10,4,50)

#função lambda, função sem nome com parametro

#recebe um valor e calcula o dobro
a = lambda x : x * 2
print(a(5))

#lambda mais de um parametro

aumento = lambda a, b: (a*b / 100)
print(aumento(300, 2))

#exemplo metodo sort

L = ['A', 'b', 'C', 'D']
L.sort()
print('Lista ordenada: ',L)

L.sort(key =lambda x: x.lower())
#mudou o criterio de ordenação da lista, independente de maiscula ou minuscula
print(L)
