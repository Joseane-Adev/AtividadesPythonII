#imprimir as linhas de um arquivo
def imprimir_linhas(linhas_arquivo, linha_inicial, linha_final):
    with open('linhas.txt', 'r') as l:
        linhas = l.readlines()
        for x in range(linha_inicial - 1, linha_final):
            print(linhas[x], end='')