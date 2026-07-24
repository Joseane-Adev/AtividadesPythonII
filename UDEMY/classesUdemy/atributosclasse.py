class Pessoa:
    ano_atual = 2026 #atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano(self):
        return Pessoa.ano_atual - self.idade
dados = {'nome': 'Ana', 'idade':32} #dicionario
p1 = Pessoa(**dados) #desempacotamento do dicionario
p2 = ('Helena',12)
#p1.__dict__['nome'] = 'Alves'
print(p1.__dict__) #mostra o dicionario
print(vars(p1)) #mostra o dicionario
'''
print(p1.get_ano())
print(Pessoa.ano_atual)
print(p1.__dict__)'''

'''
__dict__ 

'''