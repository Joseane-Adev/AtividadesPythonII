string = 'ABC'
lista = ['Ana', 'Maria']
tupla = 'python', 'é', 'legal'

#desempacotamento funçoes

for nome in lista:
    print(nome, end= ' ')

print(*lista)
print(*string)