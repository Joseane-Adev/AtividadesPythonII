import os


palavra_secret = 'amigo'
guarda_letra = ''
tentativas = 0

while True:

   
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('digite só uma letra!')
        continue

    if letra_digitada in palavra_secret:
        guarda_letra += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secret:
        if letra_secreta in guarda_letra:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '#'
    
    print('Palavra formada é:', palavra_formada)
    
    if palavra_formada == palavra_secret:
        os.system('cls')
        print('Você ganhou!')
        print('A palavra secreta era: ', palavra_secret)
        print('Tentativas: ', tentativas) #contador
        guarda_letra = ''
        tentativas = 0