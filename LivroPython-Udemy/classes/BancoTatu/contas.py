
class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.operacoes = [] #aqui vai ser colocado as operaçoes feitas como saque e deposito
        #self.deposito(saldo) duplica o valor so saldo, porque não coloquei o self.saldo = 0
        if saldo > 0:
          self.operacoes.append(['SALDO INICIAL', saldo])
    
    #exibi o numero da conta corrente e o saldo
    def resumo(self):
        print(f'Conta número: {self.numero} | Saldo: {self.saldo:10.2f}')
        for cliente in self.clientes:
            print(f'Cliente: {cliente.nome} | Telefone: {cliente.telefone}')
    
    #permite retirar dinheiro
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE',valor])
        else:
            self.operacoes.append(['SALDO INSUFICIENTE', valor])
        
        

    #acrescenta ao valor do saldo
    def deposito(self,valor):
        self.saldo += valor
        return self.operacoes.append(['DEPOSITO', valor])
    
    #mostrar o extrato
    def extrato(self):
        print(f'Extrato CC: {self.numero}\n')
        for operacao in self.operacoes:
            print(f'{operacao[0]:10s} {operacao[1]:10.2f}')

        print(f'\n Saldo: {self.saldo:10.2f}\n')