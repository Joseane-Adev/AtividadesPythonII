
'''
lista = [2, 5,8, 10]

menor = lista[0]

for x in lista:
    if x < menor:
        menor = x
print(f'O menor valor da lista é: {menor}')
'''
#Exercicio lista de temperaturas
listaT = [ -10, -8, 0, 1, 2, 5, -2, -4]

temperaturaMaior = listaT[0]
temperaturaMenor = listaT[0]
temperaturaMedia = sum(listaT) / len(listaT)

for x in listaT:
    if x < temperaturaMenor:
        tempertauraMenor = x
    elif x > temperaturaMaior:
        temperaturaMaior = x
      
print(f'A menor temperatura foi: {temperaturaMenor}')
print(f'A temperatura maior é: {temperaturaMaior}')
print(f'A temperatura média foi de: {temperaturaMedia}')

