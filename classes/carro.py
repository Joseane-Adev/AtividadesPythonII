class Carro():
     def __init__(self, modelo,ano,cor,cliente,preco):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.cliente = cliente
        self.preco = preco
        self.parcela = 0
        self.pagamento = None
     
     def personaliza(self):
          print('='*70)

     def mostrar_info_carros(self):
          info = (
                  f"Modelo: {self.modelo}\n"
                  f"Ano: {self.ano}\n"
                  f"Cor: {self.cor}\n"
                  f"Preço: R${self.preco:.2f}\n"
          )
          return info
          
     def carroBoleto(self):
          self.personaliza
          entrada = int(input('Digite o valor da entrada para comprar o carro: '))
          carro_entrada = self.preco - entrada
          print(f'Com a entrada de {entrada} você só irá pagar {carro_entrada}')
          self.personaliza()

          opcoes = ('Opçoes de meses')
          print(opcoes.center(45))
          print('[1]-36 meses')
          print('[2]- 24 meses')
          print('[3]- 12 meses')
          meses = int(input('Escolha o numero que se refere aos meses quer pagar o carro?'))
          self.personaliza()
          if meses == 1: 
               #pagamento é o valor da parcela
               pagamento = float(carro_entrada / 36)
               self.parcela = pagamento
               print(f'Você irá pagar pelo {self.modelo} R$:{pagamento:5.2f} em 36 meses')
          elif meses == 2:
               pagamento = float(carro_entrada / 24 )
               print(f'Você irá pagar pelo {self.modelo} R${pagamento:5.2f} em 24 meses')
          elif meses == 3:
               pagamento = float(carro_entrada / 12 )
               print(f'Você irá pagar pelo {self.modelo} R${pagamento:5.2f} em 12 meses')
          else:
               print('Opção inválida')
          

     def carroAvista(self, menu):
          self.personaliza()
          saldo = int(input(f'{self.cliente} qual o seu saldo: '))
     
          if saldo >= self.preco:
               print(f'É possível compra o carro e sobra: {saldo - self.preco}')
               self.pagamento = 'À vista'
          else:
               print(f'Saldo insuficiente falta: {self.preco - saldo}')
               
          
     


        

               
          

    
    
    
        