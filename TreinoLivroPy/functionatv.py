#escreva uma função para validar uma variavel string
'''
def valida_string(palavra, minimo, maximo):
    while True:
        user = input(palavra)
        if len(user) <= minimo or len(user) >= maximo:
            return True
        else:
            return False

palavra = (valida_string('Digite uma palavra: ',5,10))
print(palavra)'''
'''
def valida_lista(lista_palavras):
    palavra = input('Digite uma palavra: ')

    if palavra in lista_palavras:
        print(f'A palavra {palavra} está na lista')
        return True
    else:
        print(f'Essa palavra não está na lista!')
        return False

lista = ['python', 'programacao', 'uva', 'noite']
print(valida_lista(lista))'''

def recebe_string():
    while True:
        opcao = input('Digite uma letra: ').lower()


        if len(opcao) == 1 and opcao.isalpha():
            return opcao
        else: 
            print('Entrada inválida, digite novamente')

print(recebe_string())