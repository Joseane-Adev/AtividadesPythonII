import random

for x in range(10):
    print(random.uniform(15, 25))

#jogo da lotto
#gera 6 numeros aleatorios, tipo jogo de loteria
print(random.sample(range(1, 60),6))

#embaralhar
a = list(range(1,11))
random.shuffle(a)
print('------------',a)