produto = {
    'nome': 'Caneta',
    'preco': 2.5,
    'categoria': 'Escritorio'
}
#for key, value in produto.items():
    #print(key, value)

#dicionario comprehension
dc = {
    chave: valor.lower()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

print(dc)

#set comprehension
s1 = {
    i for i in range(10)
}
print(s1)
