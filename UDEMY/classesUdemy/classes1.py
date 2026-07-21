#metodos em instancias 

class Carro:
    def __init__(self, veiculo, cor, ano):
        self.veiculo = veiculo
        self.cor = cor
        self.ano = ano
    
    def acelerar(self):
        print(f'{self.veiculo} está acelerando')

carro1 = Carro('BYD', 'branco', 2025)
print(carro1.veiculo, carro1.cor, carro1.ano)
carro1.acelerar()

#sobre o self
'''
nome dado por convenção, quando queremos referenciar a propria instancia
todo comportamento criada na classe o primeiro parametro é o self
na classe o self é a propria instancia
'''
#escopo da classe e métodos

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    variavel = 'valor' #essa variavel faz parte do escopo do init
    print(variavel)

coruja = Animal(nome='Coruja')
print(coruja.nome)

class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando #começa por false
    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando')
            return

        print(f'{self.nome} está filmando')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar')
            return
        print(f'{self.nome} está fotografando')
    
    def desligar(self):
        if not self.filmando:
            print(f'Não está filmando')
            return
        print(f'{self.nome} está parando de filmar')


c1 = Camera('Canon')
c2 = Camera ('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.desligar()