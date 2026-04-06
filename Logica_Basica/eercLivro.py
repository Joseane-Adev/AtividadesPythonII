#imprima numeros impares

'''numero_user = int(input('Digite o ultimo número a ser imprimido: '))
inicio = 1

while inicio <= numero_user:
    if inicio % 2 != 0:
        print(inicio)
    inicio += 1
'''
# escrever os multiplos de 3

'''user = int(input('Digite  o ultimo numero: '))

numero = 0

while numero <= user:
    if numero % 3 == 0:
        print(f'Numeros multiplos de 3 é : {numero}')
    numero += 1
'''
#Tabuada
while True: 

    

    numero = int(input('Qual numero da tabuada você quer fazer: '))
    x = 0
    while x <=10:
         print(f'{numero} x {x} = {numero * x}')
         x += 1
    
    sair = input("Deseja sair? [S]Sim/[N]Não: ").strip().upper()#strip remove espaços inicio e fim e upper letras maiuscula
    if sair == 'S':
        print('Você saiu!')
        break
    
       


     




    



#msg = input('Deseja sair? Sim/Não: ')


