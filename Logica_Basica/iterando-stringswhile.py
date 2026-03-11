frase = 'Esse é um exercicio de iterar string com while'

letra = input('Digite qual letra você quer saber que mais aparece na frase: ')

i = 0
apareceu_mais_vezes = 0
letra_que_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    qtd_letras_apareceu_atual = frase.count(letra_atual)
    
    if apareceu_mais_vezes < apareceu_mais_vezes:
        apareceu_mais_vezes = qtd_letras_apareceu_atual
        letra_que_mais_apareceu = letra_atual
    
    print(letra_atual)
    i += 1

print(f'A letra que mais apareceu foi a letra "{letra_que_mais_apareceu}" que apareceu {apareceu_mais_vezes} vezes')