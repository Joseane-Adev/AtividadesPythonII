cpf = ('364.408.470-07'.replace('.', '').replace('-', ''))# removi os caracteres do cpf
nove_digitos = cpf[:9] #buscar somente nove digitos, fatiamento do 0 ao 9
multiplica_cpf = [10, 9,8,7,6,5,4,3,2] #lista de valores a serem multiplicados por cada digito do cpf

soma_digitos1 = 0 #contador
#percorrer os numeros da string e somar cada posição em uma 
for digito1, multiplicador in zip(nove_digitos,multiplica_cpf):
    valor = int(digito1) * multiplicador
    #print(f'{digito} X {multiplicador} = {valor}')
    soma_digitos1 += valor
    

#operaçoes da soma de todos os digitos por 10 e divisão
resultado_cpf = (soma_digitos1 * 10) % 11


#operaçao ternaria
resultado_digito = resultado_cpf if resultado_cpf <= 9 else 0
'''
if resultado_cpf > 9:
    print(f'O primeiro digito é 0')
else:
    print(f'O primeiro digito é:  {resultado_cpf}')
'''
print(f'O primeiro digito é: {resultado_digito}')

#pegar o segundo digito do cpf
dez_digitos = nove_digitos + str(resultado_digito)
contagem_digito2 = [11,10,9,8,7,6,5,4,3,2]
contador_soma_digito2 = 0

#coleta = soma_digitos1 + resultado_digito
for digito2, contagem2 in zip(dez_digitos,contagem_digito2):
    valor2 = int(digito2) * contagem2
    #print(f'{digito2} X {contagem2} = {valor2}')
    contador_soma_digito2 += valor2 
    

resultado_digito2 = (contador_soma_digito2 * 10) % 11

digito_cpf2 = resultado_digito2 if resultado_digito2 <= 9 else 0
print(f'O segundo digito é: {digito_cpf2}')

#validar cpf
cpf_gerado = f'{nove_digitos}{resultado_digito}{resultado_digito2}'

if cpf == cpf_gerado:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')