import sys
iterable = ['Eu', 'tenho','__iter__']
iterator = iter(iterable)
print(next(iterator))
#iterator trabalha com iteravel, tem o metodo iter e next
#generator expression, funçoes que sabem pausar
#não salva todos os valores na memoria, entrega por valores

generator = (n for n in range(10))
print(sys.getsizeof(generator))#ver o tamanho
for n in generator:
    print(n)
print(generator)


