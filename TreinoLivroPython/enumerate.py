lista = [1,2,3,4]

x = 0
for i in lista:
    print(f'[{x}] {i}')
    x += 1

print('---------------------------------------------')
#função enumerate

lista2 = list(range(5,51,5))
for z, e in enumerate(lista2):
    print(f'[{x}] {e}')

print('....................................')

L = [5,9,13]
for z in enumerate(L):
    x, e = z
    print(f'[{x}] {e}')
    print(z)

#verificando maior valor
print('////////////////////////////////')
lista3 = [5,7,13,45]
maximo = lista3[0]
for x in lista3:
    if x > maximo:
        maximo = x
print(f'O maior valor foi: {maximo}')

