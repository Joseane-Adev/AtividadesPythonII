#pesquisar dois valores
lista = [1,2,6,9,12,34,78,97]

valor1 = int(input('Digite um valor qualquer: '))
valor2 = int(input('Digite um novo valor: '))

posiçao = 0
pos1 = -1
pos2 = -1

while posiçao < len(lista):
    #comparar valores
    if lista[posiçao] == valor1:
        pos1 = posiçao
        print('Valor 1 encontrado primeiro')
    elif lista[posiçao] == valor2:
        pos2 = posiçao
        print('Valor 2 encontrado primeiro')
    '''
    
    if valor1 and valor2 in lista:
        print('Os dois valores foram encontrados')
        break
    else:
        print('Nenhum valor encontrado!')
        break
    '''
        
    posiçao += 1

#sAÍDA DIZENDO A POSIÇÃO NA LISTA

if pos1 != -1:
    print(f'O {valor1} foi encontrado na posição {pos1}')
else:
    print(f'O {valor1} não foi encontrado!')

if pos2 != -1:
    print(f'O {valor2} foi encontrado na posição {pos2}')
else:
    print(f'O {valor2} não foi encontrado!')


