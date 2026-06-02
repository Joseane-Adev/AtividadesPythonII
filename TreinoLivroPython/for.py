lista = [ 1,3,5,6]

valor = int(input('Digite um numero para ser encontrado: '))


for x in lista:
    if x == valor:
        print(f'{valor} foi encontrado!')
        break
else:
    print(f'{valor} não encontrado!')
   
        
