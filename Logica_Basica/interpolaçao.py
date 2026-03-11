nome = 'Ane'
preco = 12.13299
variavel = '%s, o preço é %f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (12, 12))

# %s - string
# %f - float
# %d - int
# %X - hexadecimal maiusculo, %x - hexadecimal minusculo
#(caractere)(><^)(quantidade)
# > ESQUERDA
# < - DIREITA
# ^ - CENTRO    
# Sinal - + ou -
#conversion flags - !r !s !a

var11 = 'ABC'
print(f'{var11:@>5}')
