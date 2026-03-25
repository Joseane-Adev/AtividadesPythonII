tupla = (1,2,3)


for elemento in tupla:
    print(elemento)

#empacotamento
print('-----------------')
a, b, c = 10,30,20
a, b = b,a
print(a)

#tupla a partie de listas
lista = [1,2,3,4]

t = tuple(lista)
print(t)

#tupla com lista

tupla1 = ('a','b',[1,2,3])
print(len(tupla1))
#print(tupla1[2]) #mostra a lista da tupla

#desempacotar valores
*d, e = [1,2,3,4]
print('valores',d)
print('valores',e)