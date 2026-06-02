#split = divide uma string
#join = une a string


frase = 'olá mundo da, programaçao'
lista_palavras = frase.split(',')

lista_palavras_corrigidas = []

for i, frase in enumerate(lista_palavras):
    lista_palavras_corrigidas.append(lista_palavras[i].strip())#strip corta os espaços do começo e fim

#print(lista_palavras)
#print(lista_palavras_corrigidas)
frase_unidas = '-'.join(lista_palavras_corrigidas)
print(frase_unidas)