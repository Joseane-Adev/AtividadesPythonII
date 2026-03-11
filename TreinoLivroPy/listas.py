#fazer uma lista
predio = [0,1,2,3] 

#troca de numero da lista
predio[0] = 'oi'
print(predio)

#notas de aluno

notas = [10,10,10,10]
soma = 0
i = 0

while i < 4:
    soma += notas[i]
    i += 1
print(f'Média de notas é: {soma / i:4.2f}')


print('..............................................')
lista = [1,2,3]
#referindo a uma nova copia de lista
lsNova = lista[:]

lsNova[0] = 'oi'
print(lista)
print(lsNova)
#fatiamneto de listas
print(lista[0:-2])
print(lista[-2])

len(lista)
lista.append('mundo')
print(lista)