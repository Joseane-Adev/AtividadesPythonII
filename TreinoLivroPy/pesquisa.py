#pesquisa sequencial
lista = [20, 2, 5,54,6,8,100]

valor = int(input('Digite um valor a ser procurado: '))

posição = 0

while posição < len(lista) :
    if lista[posição] == valor:
        posiçãoEncontrado = True
        print('Você encontrou o numero da lista')
        break
    posição += 1

if True:
    print(f'O {valor} foi achado na posição {posição}')
else:
    print(f'O {valor} não foi encontrado')
