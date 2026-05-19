#verificar tipos dos elementos da lista 
lista = ['olá', 2, False, ['oi'], {'A':1}]

for x in lista:
    print(type(x))

# programa 8.26 lista com niveis

def imprima_lista(lista, nivel=0, caractere='*',espaços = 2):
    linha = caractere * nivel

    for x in lista:
        if isinstance(x, int):
            print(f'{linha} {x}')
        else:
            imprima_lista(x, nivel + espaços, caractere, espaços)

imprima_lista([10, [3,2], [400, [1,5],100], 11],
              caractere= '*',
              espaços= 3)

#list comprehension indica como a lista vai ser criada
#formula
'''
cariavel = var for var in "type'
'''
l = [x for x in range(15)]
print(l)

z = [x * 3 for x in range(11)]
print(f'A tabuada de 3 é: {z}')

#com string

lista_vogal = [x.upper() for x in 'abcdef']
print(lista_vogal)

#numeros pares list comprehension

par = [x for x in range(11) if x % 2 == 0]
print(f'Esses numeros são pares de 0 até 10 {par}')

#outra forma sem listcomprehension
pares = list(range(0, 12, 2))
print(pares)

#inversao de tupla

tupla = [(a,b) for *a,b in [(1,2,3),(3,4,5)]]
print(tupla)