#multiplos de 4
with open('multiplos.txt', 'w') as multiplos:
    with open('pares.txt') as pares:
        for linha in pares.readlines():
            if int(linha) % 4 == 0:
                multiplos.write(linha)

'''
with open('imares.txt', 'w') as impares:
    with open('pares.txt', 'w') as pares:
        for x in range(0,50):
            if x % 2 == 0:
                pares.write(f'Numero par: {x}\n')
            else:
                impares.write(f'Impar {x}\n')'''