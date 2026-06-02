#palavra = input('Digite a palavra secreta: ').lower().strip()#trasformei a string em minuscula e removi espaços
lista_de_palavras = ['jogo', 'programaçao', 'computador', 'python'] # lista com algumas palavras 

numero = int(input('Digite um numero: ')) #pergunta um numero ao usuario para procurar a palavra na lista
indice = (numero * 776) % len(lista_de_palavras) #pega o indice da palavra
palavra = lista_de_palavras[indice].lower().strip() #trasforma a lista em minuscula e remove espaços

for x in range(100):#Apagar a palavra ou as letras já mostradas, evitando que o jogador veja informações antigas.
    print()#limpar o jogo

digitadas = []
acertos = []
erros = 0

#essa lista cria o boneco
boneco = [
    ['X===:===X'],
    ['X   0'] ,
    ['X  \|/'],
    ['X   |'],
    ['X  / \ '],
    ['X===:===X']
]


while True:
    senha = ''
    for letra in palavra:
        if letra in acertos:
            senha += letra
        else:
            senha += '.'
    print(senha)

    if senha == palavra:#quando você acerta a palavra
        print('Você acertou!')
        break

    tentativa = input('\nDigite uma letra: ').lower().strip()
    
    if tentativa in digitadas:
        print('Você já tentou esta letra!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    

    for i in range(len(boneco)):
        if i <= erros:
            print(''.join(boneco[i]))
    else:
        print('x')

    if erros == len(boneco) - 1:
        print('Enforcado')
        print(f'Essa era a palavra: {palavra}')


    #montar o boneco
    '''
    linha2 = ''
    if erros == 2:
        linha2 = '|'
    elif erros == 3:
        linha2 = '\|'
    elif erros >= 4:
        linha2 = '\|/'
    print( f'X{linha2}')
    linha3 = ''
    if erros == 5:
        linha3 += '/'
    elif erros >= 6:
        linha3 += '/\ '
    print(f'X{linha3}')
    print('X\n===========')
    if erros == 7:
        print('Enforcado')
        print(f'Essa é a palavra secreta: {palavra}')
        break  
'''

