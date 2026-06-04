#criar um arquivo que exiba os nomes um a um
nomes = [
    "Luiz Alves",
    "Marcela Alves",
    "Ane Alves",
    "Caio Ricardo",
    "João Pedro",
    "Maria Clara",
    "Fernanda Souza",
    "Carlos Eduardo",
    "Paula Martins",
    "Rafael Gomes"
]
#primeiro ele escreve no arquivo listanomes
with open('lista_nomes.txt', 'w') as arquivo_nome:
    for nome in nomes:
        arquivo_nome.write(nome + '\n')

#gerar apenas em um arquivo

with open( 'lista_nomes.txt', 'r') as lista_nomes:
    with open('arquivo_nomes.txt', 'w') as arquivo:
        nomes = lista_nomes.readlines()
        for nome in nomes:
            arquivo.write(nome)


