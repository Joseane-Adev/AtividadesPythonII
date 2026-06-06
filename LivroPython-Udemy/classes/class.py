class Televisão():
    def __init__(self):
        self.ligada = False
        self.canal = 2
    
    def muda_canal_baixo(self):
        self.canal -= 1
    def muda_canal_cima(self):
        self.canal += 1

tv = Televisão()
tv.muda_canal_cima()
print(tv.canal)

tv.muda_canal_baixo()
print(tv.canal)