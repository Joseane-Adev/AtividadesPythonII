#armazenar todas as contas
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = [] #armazenar as contas
    
    #metodos
    def abre_conta(self, conta):
        self.contas.append(conta)
    
    #listar contas
    def lista_contas(self):
        for tipo_conta in self.contas:
            tipo_conta.resumo()