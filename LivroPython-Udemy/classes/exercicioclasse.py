#crie um programa para representar estados e cidades . Cada estado tem um nnome, sigla e cidade.
#cada cidade tem população
#crie um programa de testes que crie tre estados com algumas cidades em cada um. exiba a população de cada estado
# como soma da população da cidade

class Estado():
    def __init__(self,estado, sigla):
        self.estado = estado
        self.sigla = sigla
        self.cidades = []
    
    def adiciona_cidades(self, cidade):
        self.cidades.append(cidade)
    
    def soma_populacao(self):
        valor_populacao = 0
        for cidade in self.cidades:
            valor_populacao += cidade.populacao
        return valor_populacao
    
    def __str__(self):
        return  f'{self.estado} ({self.sigla}) | População: {self.soma_populacao()}'

class Cidade():
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao


estado1 = Estado('Ceará','CE')
estado1.adiciona_cidades(Cidade('Juazeiro', 1000))
estado1.adiciona_cidades(Cidade('Crato', 500))
print(estado1)

        