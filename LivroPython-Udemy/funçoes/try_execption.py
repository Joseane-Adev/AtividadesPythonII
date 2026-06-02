'''#try - tentar executar o codigo
except - se der erro, faça isso
'''

numero_str = input('Vou dobrar o numero que você digitar:')

#print(numero_str.isdigit())# verifica se é um numero

try:

    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
except:
    print('Por favor, digite um número.')


