from functools import reduce
import operator

funcao =reduce(min, [2,1,9,4])
print(funcao)

max_funcao = reduce(max, [6,7,3,9])
print(max_funcao)

#o add soma a lista
op = reduce(operator.add, [1,2,3])
print(op)

#somar elementos da lista sum
soma = sum([1,2,3,2])
print(soma)

#filter

lista = list(filter(lambda x : x % 2 == 0, [5,6,2,12,11]))
print(lista)

#comprehensions
comprehension = [a for a in [13,16,19] if a % 2 == 0]
print(comprehension)