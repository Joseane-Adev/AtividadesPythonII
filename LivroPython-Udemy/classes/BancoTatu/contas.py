
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
    
    #metodo para imprimir se é possivel sacar ou não
    def verifica_saque(self,valor):
        if self.saldo >= valor:
            print('True, É POSSÍVEL SACAR!')
        else:
            print('False, NÃO É POSSIVEL SACAR!')
            
    #permite retirar dinheiro
    def saque(self,valor):
        
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE',valor])
            self.verifica_saque(valor) #chamando o metodo dessa classe
            #return True
           
        else:
            self.operacoes.append(['SALDO INSUFICIENTE', valor])
            #return False
            self.verifica_saque(valor)

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

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo =0, limite =0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite
    
    def saque(self,valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            super().verifica_saque(valor)
            #referencia a classe mãe
        else:
            self.operacoes.append(['Você não tem: ', valor])
            super().verifica_saque(valor)
            
    #reescrita do metodo de verificação
    def verifica_saque(self,valor):
        resultado = super().verifica_saque(valor) #na variavel, chamei o metodo da classe mãe
        return resultado
    
    #reescrita do metodo de extrato para exibir o limite e o saldo disponivel
    def extrato(self):
        super().extrato()#chamar o metodo la da classe conta
        print(f'Seu Limite é de: {self.limite}') #imprimir
        print(f'Total disponivel para saque: {self.saldo}')