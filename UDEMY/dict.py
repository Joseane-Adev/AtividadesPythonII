#dicionario

pessoa = {
    'nome': 'Ane',
    'sobrenome': 'Alves',
    'age': 32
}

print(pessoa['age'])
'''
print('-------------')

for chave in pessoa:
    print(chave, pessoa[chave])'''

pessoas = {}
pessoas['nome'] = 'Joseane'
print(pessoas['nome'])

#metodos

#len - retorna as chaves quantidade
print(len(pessoa))
#keys - iteravel com as chaves
print(list(pessoa.keys()))
#values - valores
print(list(pessoa.values()))
#items - APARECE A LISTA E VALOR
print(list(pessoa.items()))
#setdefault - adiciona se a chave não existe
print(pessoa.setdefault('endereço', 'Raimunda diociina'))
#copy - retorna uma copia rasa
#deepcopy - é mais complexo e profundo
d1 = {
    'c1': 1,
    'C2': 2,
}
d2 = d1.copy()
d2['c1'] = 800
print(d2) # alterado
print(d1)
#get - obtém uma chave
print(pessoa.get('nome'))
#pop - apaga o item com chave especificada (del)= deleta
nome = pessoa.pop('nome')
print(nome)
#popitem - paga o ultimo item
ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)
#update -atualiza um dict com outro
pessoa.update({
    'sobrenome': 'novo valor',
})
print(pessoa)
pessoa.update(nome = 'Joseane', age  = 31)
print('------', pessoa)