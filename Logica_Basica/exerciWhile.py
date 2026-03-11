frase = 'Python linguagem de programação'


print(frase.count('p'))

#indice

i = 0

#iteração na string

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    quantas_vezes_letra_apareceu_atual =frase.count(letra_atual)
    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

    

print(f'A letra que apareceu mais vezes foi a letra:  "{letra_apareceu_mais_vezes}" '
      f'que apareceu {qtd_apareceu_mais_vezes} vezes')
