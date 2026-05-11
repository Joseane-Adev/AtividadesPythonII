from entrada import valida_inteiro

lista = []
for x in range(3):
    lista.append(valida_inteiro('Digite um número: ',0, 20))
print(f'Soma: {sum(lista)}')