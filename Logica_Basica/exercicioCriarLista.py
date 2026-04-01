
lista_compras = []

while True:
    opcao = input('Selecione uma opção : [i]Inserir | [a]Apagar | [l]Listar | [s] Sair: ')

    if opcao == 'i':
        valor = input('Produto para cadastrar na lista: ')
        lista_compras.append(valor) #guardar os valores na lista

    elif opcao == 'l':
        for valor in enumerate(lista_compras):
            print(valor)

    elif opcao == 'a':
        indice_apagar = int(input('Escolha o indice da lista para apagar: '))
        if indice_apagar >= len(lista_compras) or indice_apagar < 0:
            print('Não foi possível apagar esse índice da lista!')
        else:
            removido = lista_compras.pop(indice_apagar)
            print(f'Você apagou o item: {removido} da lista')
    elif opcao == 's':
        print('Você saiu do programa')
        break
    else:
        print('Essa opção não existe')





