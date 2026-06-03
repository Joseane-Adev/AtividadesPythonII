arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#with

with open('numeros.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha)

#parametros linha de comando
import sys
print(f'Numero de parametros: {len(sys.argv)}')
for x, w in enumerate(sys.argv):
    print(f'Parametro {x} = {w}')