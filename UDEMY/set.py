
conjunto = set()
conjunto = {1,2,3,3}

teste = 1 in conjunto
print(teste)

#MÉTODOS ÚTEIS
#add, update, clear, discard

x = set()
x.add('Ane')
x.update(('OLÁ', 1,2))#de forma iterada
#x.clear()#limpar o conjunto
x.discard('OLÁ')
print(x)

#operadores
a ={0,1,2}
b = {1,2,3}
#união
conjunto_novo = a | b
print(conjunto_novo)
#intersection, retorna os elementos em comum
interseccao = a & b
print(interseccao)
#diferença
difer = a -b
print(difer)


