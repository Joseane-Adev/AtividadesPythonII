
print('****Descubra se o numero é primo ou não****')


while True:

    numero = int(input('Digite um numero qualquer: '))

    if numero < 2 :
        print('Não é primo!')
    elif numero == 2:
        print('Único numero primo par é o: ', numero)
    elif numero % 2 == 0:
        print('Não é numero primo!')
    else:
        print('Numero primo!')

#ERRO#

#ler um numero e imprimir os primeiros numeros primos
"""_
    
while True:

    x = int(input('Digite um numero para saber os numeros primos'))
    guarda_primos = []

    if x < 2:
        print('Esse numero é menor que 2')
    elif x == 2:
        print('Unico numero primo par!')
    elif x %  2 == 0:
        print('Não é primo') 
    else:     
        print('Numero primo')
    
    guarda_primos += 1
    print(guarda_primos)
"""
    






