#operator walrus

soma = 0.0

while(valor := input('digite fim ou um numero qualquer: '))!='fim':
    soma += float(valor)

print(f'A soma dos numeros digitados é: {soma}')


#com f-string

lista = [1,2,4,2]
print(f'Valores da lista {lista} tem {(tamanho := len(lista))} elementos que somados são{(soma := sum(lista))} e tem média de {soma/ tamanho}')