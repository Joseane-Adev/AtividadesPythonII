import random

#gerar numeros de 0 até 9 aleatorio
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))#gerar numeros aleatorios


multiplica_cpf = [10, 9,8,7,6,5,4,3,2] #lista de valores a serem multiplicados por cada numero para dar o primeiro digito

soma_digito1 = 0 #contador

#percorrer os numeros da string e somar cada posição em uma 
for digito1, multiplicador_digito1 in zip(nove_digitos,multiplica_cpf):
    valor = int(digito1) * multiplicador_digito1
    #print(f'{digito} X {multiplicador_digito1} = {valor}')
    soma_digito1 += valor
    

#operaçoes da soma de todos os digitos por 10 e divisão
resultado_cpf = (soma_digito1 * 10) % 11

#operaçao ternaria
resultado_digito1 = resultado_cpf if resultado_cpf <= 9 else 0
'''
if resultado_cpf > 9:
    print(f'O primeiro digito é 0')
else:
    print(f'O primeiro digito é:  {resultado_cpf}')
'''
print(f'O primeiro digito é: {resultado_digito1}')

#pegar o segundo digito do cpf
dez_digitos = nove_digitos + str(resultado_digito1) #soma os nove digitos gerados + o primeiro digito do  cpf
contagem_digito2 = [11,10,9,8,7,6,5,4,3,2]#lista do segundo digito do 11 até 2
contador_soma_digito2 = 0

#digito2 = os nove numeros do cpf + o primeiro digito
#contagem2 = é a lista com os valores a serem multiplicados pelos dez digitos

for digito2, contagem2 in zip(dez_digitos,contagem_digito2):
    valor2 = int(digito2) * contagem2
    #print(f'{digito2} X {contagem2} = {valor2}')
    contador_soma_digito2 += valor2 # contador recebe a soma dele mesmo + a multiplicaçao dos digitos pela lista
    
    
resultado_digito2 = (contador_soma_digito2 * 10) % 11 # calculo que pega a soma multiplicado por 10 e o resultado pega o resto da / de 11

digito_cpf2 = resultado_digito2 if resultado_digito2 <= 9 else 0
print(f'O segundo digito é: {digito_cpf2}')

cpf_gerado = f'{nove_digitos}{resultado_digito1}{resultado_digito2}' # mostra os noves numeros, primeiro digito e segundo digito
print(cpf_gerado)