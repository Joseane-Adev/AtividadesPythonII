notas = [0,0]
somaNotas = 0
i = 0

#condição
while i < len(notas):
    notas[i] = float(input('Digite a nota: '))
    somaNotas += notas[i]
    i += 1
media = somaNotas / i
print(f'Suas notas são: {notas} A média é: {media}')


if media > 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')





