#função que multiplica todos os argumentos não nomeados, retorne o total para variavel e mostre o valor da variavel.
from functools import reduce
import operator

def multiplica(*args):
   resultado =reduce(operator.mul, args, 1) # o 1 é para dizer que começa pelo 1
   return resultado

valores = multiplica(5,2,3)
print(f'A multiplicação é: {valores}')

#funçao que diz se é par ou impar
numero = int(input('Digite um numero e descubra se é impar ou par: '))

def epar_impar(numero):
        
        conta = numero % 2 == 0
     
        if conta:
            return f'O {numero} é par'
        return f'O {numero} é ímpar'
    

print(epar_impar(numero))

#funçoes de primeira classe
def saudacao(msg, nome):
     return f'{msg}, {nome}!'

def executa(funcao, *args):
     return funcao(*args)

print(executa(saudacao,'Olá', 'Ane'))
# a função executa recebe três parametros 
#a função e a msg e o nome