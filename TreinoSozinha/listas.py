produtosLista = []

while True:

    if len(produtosLista) > 6:
         print('só pode guardar 5 produtos')
    
    produto = input('Qual item deseja guardar? ')
    produtosLista.append(produto)

    if produto.lower() == 'sair':
         print('Você saiu do programa')
         break
    
    for indice, elemento in enumerate(produtosLista):
         print(f'Posição: {indice} Produto guardado: {elemento}')

    print(produtosLista)