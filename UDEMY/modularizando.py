#primeiro modulo executado é __main__
import sys

print('Modulo', __name__)

print(*sys.path, sep='\n')

#recarregando modulos, é carregado uma vez
import importlib #para recarregar o modulo

import modulariazando_m

print(modulariazando_m.var)

for i in range(5):
    importlib.reload(modulariazando_m) # recarregar o modulo
    print(i)

print('fim')