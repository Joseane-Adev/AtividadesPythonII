'''lista = [10,2,5]
lista.sort()
print(lista)
'''
lista = [
    {'nome': 'Vivi', 'sobrenome': 'Alves'},
    {'nome': 'Maria', 'sobrenome': 'Sousa'},
]

def exibir(lista):
    for item in lista:
        print(item)

li1 = sorted(lista, key=lambda item: item['nome'])

exibir(li1)

#lambda complexo
#essa função executa uma função com parametros *args
def executa(funcao, *args):
    return funcao(*args)# return função(parametros)

def soma (x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

#cariavel recebe a funçao multiplica e o (multiplicador)
#duplica = cria_multiplicador(5)

duplica = executa(
    #executa a primmeira funçao cria multiplicador, depois
    # a segunda funçao multiplica
    # o que ela faz o return e por ultimo o 
    #ultimo o parametro que a primeira funçao precisa
    lambda mult: lambda num: mult * num , 5
)

print(duplica(5)) #imprime a variavel com o parametro da segunda funçao 

print(
    #chama a funçao executa para a funçao de soma que é
    # funçao lambda parametros(x,y) : o que ela faz e os valores no final
    executa(
        lambda x, y : x + y, 10, 3
    )
)
'''
Aqui a função executa 
a função lambda  sem nome  recebe os paramtros *args 
que irá somar os *args,
parametros passados.
'''
print(
   executa(
       lambda *args: sum(args),
       10,20,30
   )
)