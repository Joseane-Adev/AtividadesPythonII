#contador 
x =1
#acumulador_notas

acumulador_notas = 0

#laço de repetição
while x <= 3:
    media = float(input(f'Digite a {x} nota:'))
    
    acumulador_notas += media
    x += 1

print(f'Suas notas foram {acumulador_notas} - A media das suas notas é: {acumulador_notas / 3: 2f}')

