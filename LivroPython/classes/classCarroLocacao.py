from classeCarros import Carro, Cliente

class Locacao:
    def __init__(self, cliente, carro, dias_alugado):
        self.cliente = cliente #objeto guardado da classe cliente
        self.carro = carro #objeto carro
        self.dias_alugado = dias_alugado
    
    def pagamento(self):
        valor = self.dias_alugado * self.carro.diaria
        return f' Valor a ser pago: R$: {valor} '
    
    def __str__(self):
        return f'Cliente: {self.cliente.nome} | Carro: {self.carro.modelo} | Dias: {self.dias_alugado} | Valor: {self.pagamento()}'
   
        

carro1 = Carro('Gol', 2002 , 50)
pessoa1 = Cliente('Ana', 233245567)
locador1 = Locacao(pessoa1, carro1, 2)
print(locador1)
