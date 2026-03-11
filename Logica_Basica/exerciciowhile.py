'''

iterando strings com while

'''

nome = 'JOSEANE ALVES' # ITERAVEIS

tamanho_nome = len(nome)

print(tamanho_nome)

contador_nome = 0
novo_nome = ''
while contador_nome < len(nome):
    letra = nome[contador_nome]
    novo_nome += f'-{letra}'
    contador_nome += 1


print(f'Seu novo nome é : {novo_nome}')

          