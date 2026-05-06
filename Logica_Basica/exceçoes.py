#Exceções
'''
nome = ['Ana', 'Maria', 'Carlos']

#percorrendo a lista
for i in range(3):
    try:
        a = int(input('digite o indice a imprimir: '))
        print(nome[a])
    except ValueError:
        print('Digite um numero!')
    finally:
        print(f'Tentativa: {i + 1}')#contar as tentativas 
'''

#EXEMPLO
def épar(numero):
    try:
        return numero % 2
    except Exception:
        raise ValueError('Valor inválido')

print(épar('b'))