codigo = int(input('Digite o codigo do produto: '))
quantidade_comprada = int((input('Digite a quantidade comprada: ')))

while codigo != 0:


    if codigo == 1:
      preco = 0.50
    elif codigo == 2:
       preco = 1.00
    elif codigo == 3:
       preco = 4.00
    elif codigo == 5:
       preco = 7.00
    elif codigo == 9 :
       preco = 8.00
    else:
       print('Código não encontrado')

    total_compras = preco * quantidade_comprada
    print(f'O total de compras foi de: {total_compras} reais!')
    break

   





    