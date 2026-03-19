frase = input('Digite uma frase: ')

dicionario = {}

for char in frase:
    if char in dicionario:
        dicionario[char] += 1
    else:
        dicionario[char] = 1

print(dicionario)