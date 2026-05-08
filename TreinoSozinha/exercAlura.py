#dizer quais numeros são pares

lista = [1,2,3,4,5,6]

pares = filter(lambda x: x % 2 == 0, lista)
print(lista)
print(f'Nuúmeros pares: {list(pares)}')

#Calculadora com lambda
soma = lambda n1, n2 : n1 + n2
subtrai = lambda n1,n2: n1 - n2
mult = lambda n1,n2: n1*n2
div= lambda n1,n2: n1/n2

while True:
    try: 
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo numero: '))
        operador = input('Escolha um operador |+| |-| |*| |/| :')

        if operador == '+':
            print(F'O resultado é: {soma(n1, n2)}')
        elif operador == '-':
            print(f'O resultado é: {subtrai(n1,n2)}')
        elif operador == '*':
            print(f'O resultado é: {mult(n1,n2)}')
        elif operador == '/':
            print(f'O resultado é: {div(n1,n2)}')
        else:
             print('Operador inválido')

    except ValueError:
            print('Digite apenas números')
    except ZeroDivisionError:
            print('Não existe divisão por 0')
    
    sair = input('Deseja sair? Sim | Não: ').lower()
    if sair == 'sim':
         print('Você saiu do programa!')
         break
    else: 
         continue

#DESCONTO COM PORCENTAGEM

#digite a porcentagem de desconto
porcentagem = float(input('Digite a porcentagem de desconto: '))
valor = float(input('Digite o valor da compra: '))
    
def calculaDesconto():
    desconto = (porcentagem / 100) * valor
    valorFinal = valor - desconto
    return valorFinal

print(f'Preço final com desconto: {calculaDesconto()}')