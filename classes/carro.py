class Carro():
     def __init__(self, modelo,ano,cor,cliente,preco):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.cliente = cliente
        self.preco = preco
     
     def personaliza(self):
          print('='*70)

     def mostrar_info_carros(self):
          titulo_info = 'Informaçoes'
          info = (
                  f"{titulo_info.center(45)}\n"
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
               pagamento = float(carro_entrada / 36)
               print(f'Você irá pagar pelo {self.modelo} R$:{pagamento:5.2f} em 36 meses')
          elif meses == 2:
               pagamento = float(carro_entrada / 24 )
               print(f'Você irá pagar pelo {self.modelo} R${pagamento:5.2f} em 24 meses')
          elif meses == 3:
               pagamento = float(carro_entrada / 12 )
               print(f'Você irá pagar pelo {self.modelo} R${pagamento:5.2f} em 12 meses')
          else:
               print('Opção inválida')
          

     def carroAvista(self):
          self.personaliza()
          saldo = int(input(f'{self.cliente} qual o seu saldo: '))

          if self.preco >= saldo:
               print('É possível compra o carro')
          elif self.preco <= saldo:
               print(f'É possível comprar o carro e sobra:{saldo - self.preco} ')
          else:
               print(f'Saldo insuficiente falta: {self.preco - saldo}')
          self.personaliza()
     
          
          


'''

#para criar o contrato
     def extrato_compra(self):
          with open('arquivo_compra.txt', 'w' ,encoding='utf-8') as contrato:
               contrato.write(coloque as aspas
          <!DOCTYPE html>
          <html lang= 'pt-BR>
          <head>
          <meta charset = 'utf-8'>
          <title>Contrato</title>
          </head>
          <body>)coloque aspas
               contrato.write(f'<h2>Contrato Concessionária Dream</h2>')
               contrato.write(f'<p>Nome do cliente: </p> {self.cliente}')
               contrato.write(f'<p>Informaçoes do carro: </p> {self.mostrar_info_carros()}')
               contrato.write(f'Pagamento:')     
               contrato.write('</body></html>')
   
        



'''

               
          

    
    
    
        