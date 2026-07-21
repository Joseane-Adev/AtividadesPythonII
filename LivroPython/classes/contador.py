class Contador:
    instancias = 0 #atributo da classe

    def __init__(self):
        self.contador = 0
        Contador.instancias += 1
    
    def incrementa(self):
        self.contador += 1

a = Contador()
b = Contador()

print(Contador.instancias)#acessar  o valor de instancias
print('A = ', a.contador)
b.contador += 1
print('b = ', b.contador)
print('A = ', a.contador)