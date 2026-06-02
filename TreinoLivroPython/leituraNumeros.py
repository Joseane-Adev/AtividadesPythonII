n = 0
contador_number = 0

while True:
    number = int(input('Digite qualquer numero ou 0 para sair.'))
    if number == 0:
        print('Você saiu do programa.')
        break
    
     #acumulador
    n += 1
    contador_number += number

soma = contador_number // n


print("Quantidade de numeros lidos:", n , 'A média dos numeros digitados é de:', soma)
