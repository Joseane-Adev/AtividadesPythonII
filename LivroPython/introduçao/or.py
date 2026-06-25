entrada = input('[E]entrar ou [S]air? ')
senha= input('Digite a senha: ')


senha_permitida ='1234'
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Entrou no sistema')
else:
    print('Saiu do sistema')

