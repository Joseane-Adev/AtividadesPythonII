import pprint
'''
lista = [a * 2 for a in range(10)]
print(lista)'''

def p(valor):
    pprint.pprint(valor, sort_dicts=False, width=40)
#mapeamento de dados list comprehension
pessoas = [
    {'nome': 'Ane', 'idade': 30},
    {'nome': 'Maria', 'idade': 25}
]

nova_lista = [
    {**valor} #desempacotando
    #{'nome': valor['nome'], 'idade': valor['idade']}
    for valor in pessoas
]

#p(nova_lista)
#print(*nova_lista, sep='\n')

lista = [x for x in range(10) if x < 5]
print(lista)

#filtro na lista
'''
Antes do for é mapeamento: pegar um dado, à esquerda é filtro, o que posso ou não conter na lista

'''
#list comprehension com mais de um for

lista1= []
for x in range(3):
    for z in range(3):
        lista1.append((x,z))

lista1 = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
print(lista1)
