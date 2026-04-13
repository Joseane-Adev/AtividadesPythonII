l = [10, 20,30]

def pesquisa(lista, valor):
    if valor in lista:
            return f'A posição do número é: {lista.index(valor)}'
    return None

print(pesquisa(l, 30))

#calcular a media de um valor de uma lista
# somar os valores da lista
def media(l):
    total = 0 # contador
    for x in l:
        total += x
    return total / len(l)

print(f'a média da lista é: {media(l):.0f}')

#fatorial

def fat(numero):
    fatorial = 1
    x = 1
    while x <= numero:
        fatorial *= x
        x += 1
    return fatorial

print(fat(4))