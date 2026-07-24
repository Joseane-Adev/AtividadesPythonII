lista = [a * 2 for a in range(10)]
print(lista)

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
print(*nova_lista, sep='\n')