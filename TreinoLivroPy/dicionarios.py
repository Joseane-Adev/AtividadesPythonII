tabela = { 'Manga': 4.00,
            'Uva': 2.20,
            'Caju': 3.40}

print(tabela['Caju'])
tabela['Caju'] = 1.5
print(f'Novo preço: {tabela['Caju']}')
print(tabela)

#para saber se existe a chave no dicionario
print('morango' in tabela)
print('Uva' in tabela)

#obter lista com as chaves do dicionario

print(tabela.keys())
print(tabela.values())

