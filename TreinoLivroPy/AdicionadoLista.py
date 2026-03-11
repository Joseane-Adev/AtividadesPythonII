lista = []

while True:
    numero = int(input('DIGITE UM NUMERO QUALQUER:'))
    if numero == 0:
        print('Você digitou o numero de saída que é o:' , numero)
        break
    lista.append(numero)

    contador = 0
    while contador < len(lista):
        print(lista[contador])
        contador += 1
