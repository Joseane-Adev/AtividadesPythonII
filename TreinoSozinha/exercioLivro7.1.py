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

