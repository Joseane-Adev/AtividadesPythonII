#closure, funçoes que retornam outrass funçoes

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


escreva_bomdia = criar_saudacao('Bom dia')
escreva_pergunta = criar_saudacao('TUDO BEM?')

for nome in ['Ane', 'Marcelo', 'Caio']:
    print(escreva_bomdia(nome))
    print(escreva_pergunta(nome))
