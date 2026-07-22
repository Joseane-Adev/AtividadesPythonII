a, b = 1, 2
a, b = b, a # inverte os valores
print(a, b)
'''
a, b = pessoa.items()
print(a, b)
'''
#items vai mostrar uma tupla com os valores, só values é so a chave

#args - argumentos não nomeados
#kwargs - argumentos nomeados


pessoa = {
    'nome': 'Ane',
    'sobrenome': 'Alves',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.5,
}
'''
** vai extrair do dicionario
'''
#aqui temos um desempacotamento de um dicionario
dados_completos = {**pessoa, **dados_pessoa}
print('*' *40)
#print(dados_completos)

def mostra_argumentos_nomeados(*args, **kwargs):
    print ('Não nomeados', args)
    for chave, valor in kwargs.items():
        print(chave, valor)


#mostra_argumentos_nomeados(10, nome= 'MARIA')
mostra_argumentos_nomeados(**dados_completos)