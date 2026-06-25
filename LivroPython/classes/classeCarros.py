class Carro:
    def __init__(self,modelo, ano, diaria):
        self.modelo = modelo
        self.ano = ano
        self.diaria = diaria
    '''
    def __str__(self):
        return f'Modelo do carro: {self.modelo} | Ano: {self.ano} | Diária: {self.diaria}'

carro1 = Carro('Gol', 2002 , 50)
print(carro1)'''

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    '''
    def __str__(self):
        return f'Nome do locador(a): {self.nome} CPF: {self.cpf}'

pessoa1 = Cliente('Ana', 233245567)
print(pessoa1)
'''
