#geradores

lista = [1,2,3,4]
i = iter(lista)
print(next(i))#retorna o elemento da função

#gerador de numeros
def gerador_numeros():
    contador = 0
    while True:
        yield contador
        contador+=1

#essa repetição gera uma sequencia de numeros infinita
for x in gerador_numeros():
    print(x)


#print(next(g)) #saída 0, mostra um de cada vez, tem que chamar o next(proximo)

#não apareceu saída no console
def gerador_fibo():
    p = 0
    x = 0

    while x < 10:
        yield x
        p, x = x, x + p

print([x for x in gerador_fibo()])
print(list(gerador_fibo()))

#Generator Comprehensions

#list
print((x for x in range(10) if x % 3 == 0))

for y in (x for x in range(10) if x % 3 ==0):
    print(y)


#exercicio gerar numeros primos

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gerador_primos(limite):
    for num in range(2, limite + 1):
        if eh_primo(num):
            yield num

# Exemplo: todos os primos até 50
print(list(gerador_primos(10)))
