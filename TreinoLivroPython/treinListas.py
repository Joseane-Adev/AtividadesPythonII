#fazer um program QUE LEIA DUAS LISTAS E QUE GERE UMA TERCEIRA COM OS ELEMENTOS DAS DUAS PRIMEIRA

lista1 = [1,2,3]
lista1 += [5,6,7] #adicionei elemntos à primeira lista

print(lista1)
print('...........................')
listaNova = lista1
listaNova.append(['oi', 'mundo'])
print(listaNova)

#FAÇA UM PROGRAMA QUE PERCORRA DUAS LISTAS E GERE UM TERCEIRA SEM ELEMENTOS REPETIDOS.

frutas1 = ['uva', 'manga', 'banana']
frutas2 = ['banana' , 'caju', 'morango']

lista3 = []

for fruta in frutas1 + frutas2: #para fruta está em fruta1 e fruta2
    if fruta not in lista3:#se o fruta nao está lista3
        lista3.append(fruta) #adicioneo fruta na lista3

print(lista3)
print(len(lista3))
del lista3[0]
print(lista3)

lista3.pop(-1)
print(lista3)

lista4 = ['oi']
lista4.pop(0)
print(lista4)





    

