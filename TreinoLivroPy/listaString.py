frutas =  ['maçã', 'uva', 'morango']

print(f' A liste tem o tamanho de: {len(frutas)}')
print(frutas[0][1])

frutas[1]

#leitura de lista e impressão
'''
compras = []

while True:
    produto = input('Escreva o nome do produto: ')
    if produto == 'fim':
        print('Você saiu do programa!')
        break
    compras.append(produto)
    

    for x in compras:
        print(x)
'''

#imprimindo lista letra por letra

lista = ['morango', 'uva', 'manga']

for fruta in lista:
    for letra in fruta:
        print(letra, end = '|')



    