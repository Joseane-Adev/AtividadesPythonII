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
    
    def muda_canal_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1
    
#instância
tv = Televisão(2,99)
print(tv.canal)
tv2= Televisão(2,99,10)
print(tv2.canal)
'''
for x in range(0,100):
    tv.muda_canal_cima()
print(f'canal: {tv.canal}')

for x in range(0,100):
    tv.muda_canal_baixo()
print(f'Canal baixo: {tv.canal}')
'''