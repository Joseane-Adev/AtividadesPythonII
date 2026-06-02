#dicionario sem valor padrão
x = {}

for letra in "amor":
    if letra in x :
        x[letra] = x[letra] + 1
    else:
        x[letra] = 1
print((x))

#com valor padrão

x = {}

for letra in 'ajuda':
    x[letra] = x.get(letra, 0) + 1
print(x)