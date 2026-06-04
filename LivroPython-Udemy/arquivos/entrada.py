with open('entrada.txt', 'w') as entrada:
    
    entrada.write('; não deve ser impressa\n')
    entrada.write('= \n')
    entrada.write('> alinhada á direita\n')
    entrada.write('* centralizada\n')


#PROCESSAMENTO
largura = 79
with open('entrada.txt') as arquivoentrada:
    for linha in arquivoentrada.readlines():

        if linha[0] == ';':
            continue
        elif linha[0] == '=':
            print('=' * 40)
        elif linha[0] == '>':
            print(linha[1:].rjust(largura))
        elif linha[0] == '*':
            print(linha[1:].center(largura))
        else:
            print(linha)