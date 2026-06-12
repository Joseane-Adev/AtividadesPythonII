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

#ler um arquivo e criar um dicionario em que cada chave é uma palavra e cada valor é 
#o numero de ocorrencias no arquivo
palavras = ['programação' ,'python' ,'desenvolvedora']

with open('palavras.txt', 'w') as lista_palavras:
    for palavra in palavras:
        lista_palavras.write(palavra + '\n')
   

with open('palavras.txt', 'r') as dicionario:
    leitura = dicionario.readlines()

contagem= {}
for linha in leitura:
    palavra = linha.strip()
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)

