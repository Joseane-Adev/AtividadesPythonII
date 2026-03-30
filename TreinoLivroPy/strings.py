l = list('Oi mundo')
print(l[2])
print(l[1])
l[0] = 'o'
print(l)

#elemento join
s = "".join(l)
print(s)

#verificação de string

name = 'Joseane Alves'
print(name.startswith('Ane')) # começa com esse nome?
print(name.endswith('Alves')) #termina com esse nome?

print('---------------------------------')
print(name.lower().startswith('joseane')) #minusculo
print(name.upper().endswith('alves')) #maisculo

#operador in

nome = 'Amalia'
print('ANE' in nome) #Ane está in nome?
print('a A' in nome) # erro = false

print('------------------------------')
#se está contida not in
s = 'Todos caminhos me levam a programaçao'
print('todos' not in s.lower()) #false pois ele está, entao o operador not in nega
print('CAMINHOS' not in s.upper())
print('os' not in s.lower())

#contagem

palavra = ' eu amo, amo muito programacao'
print(palavra.count('amo')) #conta quantas vezes tem a palavra
print('Essa letra aparece:', palavra.count('a'), 'vezes')

#count com listas
lista = [1,2,3,4,5,1]
print(lista.count(1))

#pesquisa de string ( find)
x = 'OLA MUNDO'
print(x.lower().find('do')) # posiçao da primeira letra 7
print(x[4:])# a partir da posiçao 4 até o final

#rfind busca da direita p/ esquerda
print(x.rfind('A'))
print(x[2:6]) # A MU
print(x.upper().find('MUNDO', 0, 9)) # 4
#print(x.upper().index('z')) #lança uma exceção ValueError
print(x.rindex('A')) #mostra a posição
#PESQUISA DE TODAS AS OCORRENCIAS
frase = 'Eu sou desenvolvedora python, sou apaixonada por IA'
x = 0

while(x > -1):
    #palavra = input('Qual palavra quer verificar a posição?')
    x = frase.find('sou',x)
    if x >= 0:
        print(f'Posição da palavra é: {x}')
        x += 1
    

