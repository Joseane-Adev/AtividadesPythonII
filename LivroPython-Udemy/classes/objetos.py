class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.marca = 'AOC'
        self.tamanho = 42
print('TV Quarto')
tv_quarto = Televisão()
print(tv_quarto.ligada)
print(tv_quarto.canal)
print(tv_quarto.marca)
print(tv_quarto.tamanho)

print('=' * 40)
print('TV sala')
tv_sala = Televisão()
tv_sala.ligada = True
tv_sala.canal = 10
tv_sala.marca = 'samsung'
tv_sala.tamanho = 50

print(f'Telivisão ligada? {tv_sala.ligada}')
print(f'Canal: {tv_sala.canal}')
print(f'Marca: {tv_sala.marca}')
print(f'Tamanho: {tv_sala.tamanho} polegadas')
