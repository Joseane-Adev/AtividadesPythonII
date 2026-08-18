#modulos padrão do python

# inteiro
import sys
print(sys.platform)
#sys.exit()#saie do programa

#parte do modulo
#from sys import exit, platform

#python sobescreve, então musa o nome do modulo
import sys as s
sys = 'algo' # correto é não usar o nome do modulo como variavel
print(s.platform)
print(sys)


from sys import platform as pf, exit as ex
print(pf)

#vantagem - reservar nomes para o codigo
#desvantagem - pode ficar fora do padrão da linguagem

#má prática = from nome_modulo import *
#Vantagem e desvantagem =importa tudo de um modulo
from sys import *