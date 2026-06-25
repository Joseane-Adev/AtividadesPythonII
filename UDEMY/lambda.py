'''lista = [10,2,5]
lista.sort()
print(lista)
'''
lista = [
    {'nome': 'Vivi', 'sobrenome': 'Alves'},
    {'nome': 'Maria', 'sobrenome': 'Sousa'},
]

def exibir(lista):
    for item in lista:
        print(item)

li1 = sorted(lista, key=lambda item: item['nome'])

exibir(li1)