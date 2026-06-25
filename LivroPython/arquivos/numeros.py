with open('impares.txt', 'w') as impares:
    with open('pares.txt', 'w') as pares:
        for x in range(0, 20):
            if x % 2 == 0:
                pares.write(f'Numero par: {x}\n')
            else:
                impares.write(f'Impar {x}\n')

#em uma unica linha

with open('impares.txt', 'w') as impares, open('pares.txt', 'w') as pares:
        for x in range(0, 10):
            if x % 2 == 0:
                pares.write(f'Numero par: {x}\n')
            else:
                impares.write(f'Impar {x}\n')

#imparpar
#exercicio
with open('numerosParImpar.txt', 'w') as numeros:
    for n in range(0,10):
            if n % 2 == 0:
                numeros.write(f'Par {n}\n')
            else:
                numeros.write(f'Impar: {n}\n')

#exercicio 2
with open('impares.txt', 'r') as primeiro, open('pares.txt', 'r')as segundo, open('saida.txt', 'w')as saida:
         for linha in primeiro:
              saida.write(f'Primeira lista: {linha}')
         for linha in segundo:
              saida.write(f'Segunda lista: {linha}')

#exercicio3
with open('pares.txt', 'r') as pares:
     with open('inversoPares.txt', 'w') as inversoPares:
        linhasInversas = pares.readlines()
        for numero in reversed(linhasInversas):
            inversoPares.write(numero)

