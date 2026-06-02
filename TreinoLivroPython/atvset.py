#crie duas listas e compare
A = [1,2,3]
B= [1,3,4]

#valores comuns
valores_comum = set(A) & set(B) 
print(valores_comum)

#valor que so existe na primeira
diferenca = set(A) - set(B)
print(diferenca)

#valor que so existe na segunda lista
diferenca2 = set(B) - set(A)
print(diferenca2)

#lista com os elementos não repetidos das duas listas
C = set(A) | set(B)
print(C)

#a primeira lista sem os elementos repetidos da segunda 
primeira_lista = set(A) - set(B)
print(primeira_lista)

#Segunda atividade, comparar duas listas 

lista1 = [1,2,3,4,]
lista2 = [4,5,1]

nao_mudaram = set(lista1) & set(lista2)
print('Não mudaram' , nao_mudaram)

novos = set(lista2) - set(lista1)
print('Novos elemntos' , novos)

removidos = set(lista1) - set(lista2)
print('Removidos: ', removidos)
