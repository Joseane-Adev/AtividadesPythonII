from carro import Carro

class Menu():
    
    def personaliza(self):
        print('=' * 70)
    
    def menu(self):
        while True:
            self.personaliza()
            titulo = 'Concessionária Dream'
            print(titulo.center(45))
            self.cliente = input('Digite seu nome: ')

        
            self.personaliza()
            titulo_car = 'Carros à venda!'
            print(titulo_car.center(45))
            carros_disponiveis = [
                    Carro("Fiat Uno", 2020, "Branco", self.cliente, 35000),
                    Carro("Chevrolet Onix", 2022, "Preto", self.cliente, 55000),
                    Carro("Toyota Corolla", 2023, "Prata", self.cliente, 120000)
                ]
            
            for indice, carro in enumerate(carros_disponiveis, start=1):
                print(f'[{indice}] | {carro.modelo} | R${carro.preco:.2f}')
            self.personaliza()
            escolha_car = int(input('Escolha o numero do carro: '))
            self.carro_escolhido = carros_disponiveis[escolha_car - 1]

                #chamar o menu de informaçoes do carro é a instancia do carro escolhido
            self.carro_escolhido.mostrar_info_carros()
            
            self.personaliza()
            comprar = input('Deseja comprar? Sim | Não: ').capitalize()
            if comprar == 'Sim':
                 print('Formas de pagamento:')
                 print('1- Boleto')
                 print('2- À vista')
                 pagamento = int(input('Qual a forma de pagamento? '))
                 if pagamento == 1:
                    self.carro_escolhido.carroBoleto()
                    self.carro_escolhido.pagamento = 'Boleto'
                    self.resumo_compra()
                    #self.carro_escolhido.extrato_compra()
                 elif pagamento == 2:
                    self.carro_escolhido.carroAvista()
                    self.carro_escolhido.pagamento = 'À vista'
                    self.resumo_compra()
                    #carro_escolhido.extrato_compra()
                 else:
                    return 'Opção inválida'
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


            

        

        
        