
class Carro():
     def __init__(self, modelo,ano,cor,cliente,preco):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.cliente = cliente
        self.preco = preco

     
     def carroBoleto(self):
          entrada = int(input('Digite o valor da entrada para comprar o carro: '))
          carro_entrada = self.preco - entrada
          print(f'Com a entrada de {entrada} você só irá pagar {carro_entrada}')
          
          opcoes = ('Opçoes de meses')
          print(opcoes.center(40))
          print('[1]-36 meses')
          print('[2]- 24 meses')
          print('[3]- 12 meses')
          meses = int(input('Em quantos meses quer pagar o carro?'))
          if meses == 1:
               pagamento = float(carro_entrada / 36)
               print(f'Você irá pagar pelo {self.modelo} R$:{pagamento:5.2f} em 36 meses')
          elif meses == 2:
               pagamento = float(carro_entrada / 24 )
               print(f'Você irá pagar pelo {self.modelo} R${pagamento:5.2f} em 24 meses')
          elif meses == 2:
               pagamento = float(carro_entrada / 12 )
               print(f'Você irá pagar pelo {self.modelo} R${pagamento:5.2f} em 12 meses')
          else:
               print('Opção inválida')
          

     def carroAvista(self):
          saldo = int(input(f'{self.cliente} qual o seu saldo: '))

          if self.preco >= saldo:
               print('É possível compra o carro')
          elif self.preco <= saldo:
               print(f'É possível comprar o carro e sobra:{saldo - self.preco} ')
          else:
               print(f'Saldo insuficiente falta: {self.preco - saldo}')
     
     

    
    
    
        