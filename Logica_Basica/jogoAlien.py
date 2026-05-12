import random

def menu():
    print('Um alienigena está escondido atrás da arvore.'
    'Cada árvore foi numerada de um a 100.''Você tem 3 tentativas para adivinhar ' \
    'a árvore que o alinígena se esconde')
    print('*' *40)
    print('1 - Modo fácil (100 vidas)')
    print('2 - Modo médio (80 vidas)')
    print('3 - Modo difícil (75 vidas)') 
    escolha = int(input('Escolha o numero de dificuladade do jogo!'))

    if escolha == 1:
         print('Você começou o jogo com 100 vidas!')
         encontra_alien(100)
    elif escolha == 2:
         print('Você começou o jogo com 80 vidas!')
         encontra_alien(80)
    elif escolha == 3:
         print('Você começou o jogo com 75 vidas!')
         encontra_alien(75)
    else:
         print('Digite um  numero do menu: ')

def encontra_alien(total_vidas):  
        vidas = total_vidas #o jogador começa com 100 vidas
        numeros = random.randint(1,100) #gera valores entre 1 e 100, para escolher onde está o alien
        lista_palpites = [] #lista para armazenar os palpites
        
        while vidas > 0:
            try:
                 palpite = int(input('Digite um numéro que você acha que está o alienígena: '))
                #recebe o numero para achar o alien
            except ValueError:
                 print('Digite um numero!')

            #Se meu palpite está na lista de palpites, o numero já existe, continue senão
            #guarda o numero na lista.
            if palpite in lista_palpites:
                    print('Você já digitou esse numero')
                    continue
            else:
                    lista_palpites.append(palpite)

            ataque_alien = random.randint(5,20)
            #valor gerado para perder vidas entre 5 e 20
        
            if palpite == numeros:
                print(f'Você acertou! Você tem {vidas} vidas')
                break
            elif palpite != numeros:  
                vidas -= ataque_alien 

                if vidas < 0:
                    vidas = 0   
                print(f'Você foi atacada e perdeu {ataque_alien} vidas. Você tem {vidas}')
                if vidas == 0:
                    print('VOCÊ NÃO TEM MAIS VIDAS')
                    break
    

menu()

    