numeros = [10,3,6,9,11,4]
pares = []
impares = []

for x in numeros:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print('Os pares são: ', pares)
print('Os ímpares são: ', impares)