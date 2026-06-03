import sys

arquivo = sys.argvs[1]

arquivo = open('arquivo', 'r')

for linha in arquivo:
    print(linha)

arquivo.close()
