#ler duas strings , verificar se a segunda ocorre dentro da primeira e imprimir a posição do inicio

string1 = 'AABBEFAATT'
string2 = 'BE'

if string2 in string1:
    print(f'Resultado de {string2} encontrado na posiçao ,{string1.find(string2)} , de {string1}')

#escrever duas strings e gerar a terceira com os caracteres comuns as duas strings lidas

palavra1 = 'AAACTBF'
palavra2 = 'CBT'

letrasComuns = set(palavra1) & set(palavra2)
resultado = "".join(letrasComuns) #transformar em string
print(resultado)

#exercicio 7.3
#leia duas strings, gere uma terceira com os caracteres diferentes de ambas 

letras1 = 'CTA'
letras2 = 'ABC'

diferenca = set(letras1) ^ set(letras2)
print(''.join(diferenca))

#exerc 7.4
#leia uma string e imprima quantas vezes cada caracter aparece
string = 'TTAAC'

for letras in set(string):#colocou a string dentro  de um conjunto para não repetir cada char
    quantidade = string.count(letras)
    print(f'{letras}: {quantidade}')

#exercicio 7.5
#ler duas strings , gerar um aterceira, retirar da segunda os caracteres repetidos da primeira

string_Um = 'AATTGGAA'
string_Dois = 'TG'

string_Tres = []
for letra in string_Um:
    if letra not in string_Dois:
        string_Tres += letra

print(string_Tres)

#exercicio 7.6 
#leia tres stringd. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelo da terceira

numero1 = 'AATTCGAA'
numero2 = 'TG'
numero3 = 'AC'

#criar um dicionario
resultado = {}

for indice in range(len(numero2)):
    resultado[numero2[indice]] = numero3[indice]

#substituindo
numero4 = ''
for l in numero1:
    if l in resultado:
        numero4 += resultado[l]
    else:
        numero4 += l
print(numero4) 

#exercicio 7.7 pedir ao usuario que escreva uma frase e imprima quantas vogais tem

frase = input('Digite uma frase: ')
vogais = 'aeiou'

contagem = {}

for i in frase.lower():

    if i in vogais:
        contagem[i] = contagem.get(i, 0) + 1

print('Quantidade de vogais: ', contagem)