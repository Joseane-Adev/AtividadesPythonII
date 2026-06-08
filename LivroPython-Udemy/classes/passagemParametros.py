class Televisão:
    def __init__(self, canal_min, canal_max, canal_inicial = None):
        #atributos
        self.ligada = False
        self.canal_min = canal_min
        self.canal_max = canal_max

        if canal_inicial is None:
            self.canal = canal_min
        else: 
            if canal_inicial < canal_min:
                self.canal = canal_min
            elif canal_inicial > canal_max:
                self.canal = canal_max
            else:
                self.canal = canal_inicial


    def muda_canal_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1
            return self.canal
    def muda_canal_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1
            return self.canal
class ControleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao    

    def liga(self):
        self.televisao.ligada= True

    def desliga(self):
        self.televisao.ligada = False   
    
    def canal_mais(self):
        return self.televisao.muda_canal_cima()
    def canal_menos(self):
        return self.televisao.muda_canal_baixo()

tv = Televisão(2,14)
controle = ControleRemoto(tv)

print(f'Ligando a Tv')
controle.liga()
print(f'Tv ligada? {tv.ligada}')
print(f'Canal inicial = {tv.canal}')

print(f'Canal aumentar: {controle.canal_mais()}')
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