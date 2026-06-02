# digite seu nome
name = input('Digite seu nome: ')

# digite sua idade
idade = (input('Digite sua idade: '))

if name and idade:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')

    if ' ' in name:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')

    print(f'Seu nome tem {len(name)} letras')
    print(f'A primeira letra do seu nome é: {name[0]}')
    print(f'A ultima letra do seu nome é {name[-1]}')

else:
    print('Desculpe, você deixou campos vazios')