produto1 = ['sombra',5, 0.30]
produto2 = ['batom', 10 , 0.50]
produto3 = ['pincel', 2, 0.20]

compras = [produto1, produto2 , produto3]
for x in compras:
    print(f'Produto: {x[0]}')
    print(f'Quantidade: {x[1]}')
    print(f'Preço: {x[2]}')
    print('------------')

