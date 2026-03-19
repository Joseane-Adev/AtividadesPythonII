frutas = {
    'uva' : 2.2,
    'manga': 3.5,
    'cajá': 2.10,
    'Morango': 4.60}


while True:
    produto = input('Digite o nome do produto: ')

    if produto in frutas:
        print(f'Preço do produto é: {frutas[produto]:.2f}')
    else:
        print('Produto não existe')


del frutas['uva']