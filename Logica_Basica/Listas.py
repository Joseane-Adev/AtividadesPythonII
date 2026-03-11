lista = [] #lista vazia

lista1 = [123, True , 'Ana', []]
lista1[-2] = 'joseane'
print(lista1)
print(lista1[2].upper(), type(lista1[1]))

lista3 = [1,2,3,4]
#numero = lista3[0] #pega o primeiro valor da lista
#del lista3[0]
#print(numero)
#print(lista3)
lista3.append(100)
ultimo_valor =lista3.pop(1)
print(lista3, 'Removido', ultimo_valor)

lista4 = [10,20,30,"Ana", 40, 50]
lista4.append('BBB')
lista4.insert(0, 'Oi')
print(lista4)

listaA = [1,2,3,4,5,6,7]
listaB = ['oi', 'Ana']
#concatenando
lista_nova = listaA + listaB
#usando o extend
listaA.extend(listaB)
print(listaA)

#Cuidado dados mutaveis
lista_a = ['Ana', 'Joseane']
lista_b = lista_a.copy() #aparece a lista original

lista_a[0] = 'OLá'

print(lista_a)
print(lista_b)

lista5 = ['Ana', 'Joseane','abc']

for nome in lista5:
    print(nome, type(nome))