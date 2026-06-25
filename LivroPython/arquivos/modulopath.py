import os
import os.path
'''
#imprime nomes de diretorios
for a in os.listdir('.'):
    if os.path.isdir(a):
        print(f'{a}/')
    elif os.path.isfile(a):
        print(a)

'''

#verificar se já existe arquivo ou diretorio
'''
if os.path.isdir('LivroPython'):
    print('É um diretorio e existe')
else:
    print('Não existe e não é diretorio')

'''
#ESSE MODELO PERCORRE TODAS AS LISTA E DIZ O QUE CADA UM É (ARQUIVO OU DIRETORIO)
'''arquivo = input('Digite o nome do arquivo ou diretório: ')

for arquivo in os.listdir('.'):
    if os.path.isdir(arquivo):
        print(f'{arquivo} É um diretório')
    elif os.path.isfile(arquivo):
        print(f'{arquivo} É UM ARQUIVO')
'''
#ESSE MODELO É SÓ PARA DIZER SE É ARQUIVO PU DIRETORIO O QUE FOI PERGUNTADO
arquivo = input('Digite o nome do arquivo ou diretório: ')

if os.path.isdir(arquivo):
    print(f'{arquivo} É um diretório')
elif os.path.isfile(arquivo):
    print(f'{arquivo} É UM ARQUIVO')
