class Televisão():
    def __init__(self):
        self.ligada = False
        self.canal = 2
    
    def muda_canal_baixo(self):
        self.canal -= 1
        return self.canal
    def muda_canal_cima(self):
        self.canal += 1
        return self.canal
