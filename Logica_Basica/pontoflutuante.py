import decimal
#modulo

n1 = decimal.Decimal('0.1')#mostra muitas casas decimais
n2 = decimal.Decimal('0.5')#passe em string
numeros = n1 + n2
print(numeros)
print(f'{numeros:.2f}')
print(type(round(numeros, 2)))#round primeiro valor é a var e o segundo é quantiddae de casas

