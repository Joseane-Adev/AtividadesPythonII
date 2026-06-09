class Televisão:
    #metodo especial init(constructor) com os parametros do metodo
    def __init__(self, canal_min, canal_max, canal_inicial = None):
        #atributos
        self.ligada = False
        self.canal_min = canal_min
        self.canal_max = canal_max

        #condiçoes
        '''
        Se o canal atual for None = 0, o canal recebe o canal min que será passado na
        instancia da chamada da classe
        '''
        if canal_inicial is None:
            self.canal = canal_min
        else: 
            #se o canal inicial é menor que o minimo, o canal recebe o valor min passado
            if canal_inicial < canal_min:
                self.canal = canal_min
            #se o canal inicial for maior que  o canal maximo, o canal irá receber o valor do canal maximo passado na chamada da classe
            elif canal_inicial > canal_max:
                self.canal = canal_max
            #senão canal receberá o canal do inicio
            else:
                self.canal = canal_inicial
    
    #metodo da classe Televisão
    def ligada(self):
        self.ligada = True
    
    def desliga(self):
        self.desligada = False
    

    def muda_canal_baixo(self):
        #se a tv está ligada e o canal - 1 for maior queo canal minimo
        if self.ligada and self.canal - 1 >= self.canal_min:
            self.canal -= 1
            #canal recebe ele mesmo - 1
            return self.canal # retorna o canal
        
    def muda_canal_cima(self):
        #se a tv está ligada e o canal que está + 1 for menor ou igual ao canal max
        # o self.canal + 1 garante que não ultrapasse o limite de canal
        if self.ligada and self.canal + 1 <= self.canal_max:
            self.canal += 1 #canal recebe ele mesmo somado + um
            return self.canal

class Pilha:

    #metodo de inicialização com parametro energia com valor padrao se não receber nada
    def __init__(self, energia=100):
        self.energia = energia
    
    def consumo(self,consumo):
        #se o parametro do metodo for maior que a energia,
        #consumo recebe o valor de energia
        if consumo > self.energia:
            consumo = self.energia
        self.energia -=consumo
        #energia é reduzida pelo valor consumido e retorna
        return consumo      
class ControleRemoto:
    #constructor init com parametro tv e pilha
    def __init__(self, televisao,pilha):
        #atributos
        self.televisao = televisao 
        self.pilha = pilha   
    
    def liga(self):
        #se pilha tiver energia, consome uma unidade de energia, então está ligada:
        if self.pilha.consumo(1):
            self.televisao.ligada= True

    def desliga(self):
        #se a pilha tiver energia, consome 1 e será desligada
        if self.pilha.consumo(1):
            self.televisao.ligada = False   
    
    def canal_mais(self):
        #Se a pilha tiver energia, consome 1 unidade
        # e pede para a TV mudar o canal para cima
        if self.pilha.consumo(1):
            return self.televisao.muda_canal_cima()
    def canal_menos(self):
        #Se a pilha tiver energia, consome 1 unidade
        # e pede para a TV mudar o canal para baixo
        if self.pilha.consumo(1):
            return self.televisao.muda_canal_baixo()

#instâncias das classes com os valores passados como parametros
tv = Televisão(2,14)#canal min e canal max
pilha = Pilha(10) # energia da pilha
controle = ControleRemoto(tv,pilha) #recebe o objeto tv e pilha

print(f'Ligando a Tv')
controle.liga()
print(f'Tv ligada? {tv.ligada}')
print(f'Canal inicial = {tv.canal}')
print(f'Energia pilha: {pilha.energia}')


print(f'Canal aumentar: {controle.canal_mais()}')
print(f'Canal aumentar: {controle.canal_mais()}')
print(f'Canal aumentar: {controle.canal_mais()}')
print(f'Canal aumentar: {controle.canal_mais()}')
print('*' *40)
print(f'Canal inicial = {tv.canal}')
print(f'Canal aumentar: {controle.canal_mais()}')
print(f'Energia pilha: {pilha.energia}')

print(f'Canal aumentar: {controle.canal_mais()}')
print(f'Canal inicial = {tv.canal}')
print(f'Energia pilha: {pilha.energia}')
#print(f'Mudando canal para baixo {tv.muda_canal_baixo()}')

print('Desligando a tv')
controle.desliga()
print(f'Desligando a tv? {tv.ligada}')


#instância
'''
tv = Televisão(2,99)
print(tv.canal)
tv2= Televisão(2,99,10)
print(tv2.canal)

for x in range(0,100):
    tv.muda_canal_cima()
print(f'canal: {tv.canal}')

for x in range(0,100):
    tv.muda_canal_baixo()
print(f'Canal baixo: {tv.canal}')
'''