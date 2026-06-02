#dicionario com estoque e operaçao de vendas

produtos = {
    'batom' : [10 , 7],
    'sombra': [20, 5],
    'delineador': [10, 3.1]
}
while True:

    venda = input('Qual produto deseja comprar? ')
    quantidade = int(input('Quantos deseja comprar'))

    if venda not in produtos:
        print('Produto não encontrado!')
        continue

    total = 0
    print('Vendas:\n')

    preco = produtos[venda][1]
    custo = preco * quantidade

    print(f'O produto: {venda} | Quantidade : {quantidade} | Preço: {preco} = Total: {custo:6.2f}')
        # atualizar a quantidade subtraindo vendida do estoque 
    produtos[venda][0] -= quantidade
    total += custo

    print(f' Custo Total: {total:21.2f}\n')
    
    '''
    print('Estoque: \n')
    for chave, dados in produtos.items():
        print('Descrição: ', chave)
        print('Quantidade: ' , dados[0])
        print(f'Preço: {dados[1]:6.2f}\n')'''


    