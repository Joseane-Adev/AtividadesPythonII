#center = centraliza a string
palavra = 'programação'
resultado = 'X' + palavra.center(20, '-') +'X'
print(resultado)

#completar à esquerda ljust
#completar a direita rjust
novo = palavra.rjust(20, '*')
print(f'{'python' :.^30}')#com f-string

#split quebra a pertir de um caractere

s= 'um tigre, dois tigres'
sNovo = s.split(',')
print(sNovo)

#exercicio imprimir as palavras da frase digitada

frase = input('Digite uma frase: ')

novaFrase = frase.split()
print(novaFrase)