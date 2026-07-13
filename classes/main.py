from carro import Carro
from validaçoes import Validacao
import webbrowser
import os
class Menu():
    
    def personaliza(self):
        print('=' * 70)
    
    def menu(self):
        while True:
            self.personaliza()
            titulo = 'Concessionária Dream'
            print(titulo.center(45))

            self.cliente = Validacao.valida_nome()
               
        
            self.personaliza()
            titulo_car = 'Carros à venda!'
            print(titulo_car.center(45))
            carros_disponiveis = [
                    Carro("Fiat Uno", 2020, "Branco", self.cliente, 35000),
                    Carro("Chevrolet Onix", 2022, "Preto", self.cliente, 55000),
                    Carro("Toyota Corolla", 2023, "Prata", self.cliente, 120000),
                    Carro("Honda Civic", 2021, "Cinza", self.cliente, 95000),
                    Carro("Hyundai HB20", 2022, "Azul", self.cliente, 58000),
                    Carro("Ford Ka", 2018, "Branco", self.cliente, 28000),
                    Carro("Jeep Compass", 2023, "Preto", self.cliente, 160000),
                    Carro("Renault Kwid", 2021, "Laranja", self.cliente, 42000),
                    Carro("Nissan Kicks", 2022, "Prata", self.cliente, 110000)
                ]
                
            for indice, carro in enumerate(carros_disponiveis, start=1):
                print(f'[{indice}] | {carro.modelo} | R${carro.preco:.2f}')
            self.personaliza()
            while True:
                try:
                    escolha_car = int(input('Escolha o numero do carro: '))
                    if 0 <= escolha_car <= len(carros_disponiveis):
                        self.carro_escolhido = carros_disponiveis[escolha_car - 1]
                        self.carro_escolhido.mostrar_info_carros()
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('Digite um apenas o número')
                   


                    #chamar o menu de informaçoes do carro é a instancia do carro escolhido
        
                
            self.personaliza()
            comprar = input('Deseja comprar? Sim | Não: ').capitalize()
            if comprar == 'Sim':
                    print('Formas de pagamento:')
                    print('1- Boleto')
                    print('2- À vista')
            while True:
                    try:
                        pagamento = int(input('Qual a forma de pagamento? '))
                        if pagamento == 1:
                            self.carro_escolhido.carroBoleto()
                            self.carro_escolhido.pagamento = 'Boleto'
                            self.extrato_compra()
                            self.resumo_compra()
                            #self.carro_escolhido.extrato_compra()
                            break
                        elif pagamento == 2:
                            self.carro_escolhido.carroAvista(self)
                            self.carro_escolhido.pagamento = 'À vista'
                            self.extrato_compra()
                            self.resumo_compra()
                            break
                        else:
                            print('Opção inválida')
                    except ValueError:
                         print('Digite um número!')
            else:
                   print('Volte sempre')
            self.personaliza()

    def resumo_compra(self):
                self.personaliza()
                titulo = 'Contrato Concessionária Dream'
                print(titulo.center(45))
                print(f'Nome do cliente: {self.cliente}')
                print(f'\n{self.carro_escolhido.mostrar_info_carros()}')
                print(f'Pagamento: {self.carro_escolhido.pagamento}')
                if self.carro_escolhido.parcela:
                     print(f'Valor da parcela: {self.carro_escolhido.parcela:.2f}')
    
    
    #para criar o contrato
    def extrato_compra(self):
        
          contrato_arquivo = 'contrato_arquivo.html'
          with open(contrato_arquivo, 'w' ,encoding='utf-8') as contrato:
               contrato.write(f'''
          <!DOCTYPE html>
          <html lang= 'pt-BR'>
          <head>
          <meta charset = 'utf-8'>
          <title>Contrato</title>
          <style>
                body {{
                    font-family: Georgia, serif;
                    background-color: #1CA9C9;
                    color: #444;
                    line-height: 1.6;
                    padding: 40px;
                }}
                .container {{
                    background: #fff;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 0 15px rgba(0,0,0,0.2);
                    max-width: 800px;
                    margin: auto;
                }}
                h2 {{
                    text-align: center;
                    color: #444;
                }}
                .destaque {{
                    font-weight: bold;
                    color: #222;
                }}
                .info {{
                    margin-top: 20px;
                }}
            </style>
          </head>
          <body>
          <div class="container">
                <h2>Contrato Concessionária Dream</h2>
                <p><span class="destaque">Nome do cliente:</span> {self.cliente}</p>
                <div class="info">
                    <p><span class="destaque">Informações do carro:</span><br>{self.carro_escolhido.mostrar_info_carros().replace("\n","<br>")}</p>
                    <p><span class="destaque">Parcelas:</span> {self.carro_escolhido.parcela:.2f}</p>
                    <p><span class="destaque">Tipo de pagamento:</span> {self.carro_escolhido.pagamento}</p>
                </div>
            </div>
        </body>
        </html>
        ''')
               os.startfile(contrato_arquivo)
         
          
                

            

        

        
        