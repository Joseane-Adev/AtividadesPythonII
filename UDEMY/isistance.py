#isistance = para saber se objeto é de determinado tipo
# é instancia de?
lista = ['a', 1, 1.2, True, [0,1,2], (1,2), {0,1}, {'NOME': 'ANE'}]
for item in lista:
    if isinstance(item, set):
        item.add(100)
        print(f'Set: {item, isinstance(item,set)}')

    elif isinstance(item, str):
        print(item.capitalize())

    elif isinstance(item, (int,float)):
        print(f'Numero: {item, item * 2}')
    else:
        print(f'Outro: {item}')



