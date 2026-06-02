#operadores in e not in

nome = 'Joseane'

#print(nome[-1])
#print(nome[2])

print ('J' in nome) #True, está no nome
print('z' not in nome) #não está no nome

nome1 = input('Digite seu nome:')
encontrar= input('Qual letra deseja encontrar?')

if encontrar in nome1:
    print(f'A letra {encontrar} está no nome {nome1}')
else:
    print(f'A letra {encontrar} não está no nome {nome1}')