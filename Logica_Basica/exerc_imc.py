nome = input('Digite seu nome:')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)

#condiçoes
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 24.9:
    print('Peso normal')
elif imc <= 25.0 and imc > 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")

print(f'{nome} seu IMC é de: {imc:.2f}')