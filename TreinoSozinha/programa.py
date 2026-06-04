import sys

# Pega o nome do arquivo passado como argumento
arquivo_nome = sys.argv[1]

# Abre o arquivo em modo leitura
with open(arquivo_nome, 'r') as arquivo:
    for linha in arquivo:
        print(linha, end="")
