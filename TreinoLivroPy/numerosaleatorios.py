import random
'''
for x in range(5):
    print(random.randint(1,100))
'''
#sdivinhando o numero

numero = random.randint(1,10)

tentativas = 0
limite = 3
while True:
        try:
            x = int(input('Escolha um numero entre 1 e 10: ')) 
            if x == numero:
                print('Você acertou!')
                break
            else:
                tentativas += 1
                print('Você errou')

                if tentativas == limite:
                    print('Não tem mais chances!')
                    break
        except ValueError:
            print('Digite um valor válido')

            




