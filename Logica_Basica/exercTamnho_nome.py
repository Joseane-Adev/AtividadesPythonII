name = input('Digite seu nome: ')
tamanho_nome = len(name)

if tamanho_nome > 1:

    if tamanho_nome <= 4 :
        print(f'Seu nome tem {tamanho_nome} letras, seu nome é curto!')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print(f'Seu nome tem {tamanho_nome} letras, seu nome é normal!')
    else:
        print(f'Seu nome tem {tamanho_nome} letras, seu nome é grande!')
else:
    print('Digite mais de uma letra')