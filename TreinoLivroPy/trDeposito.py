contador = 0

acumulador_deposito = 0

while contador < 5:
    deposito_inicial = float(input('Digite o valor inicial do depósito: '))
    acumulador_deposito += deposito_inicial

    contador += 1
    

    taxa_poupanca = acumulador_deposito * 5 /100
    total_ganho = acumulador_deposito + taxa_poupanca
 

print(f'O valor total depositado foi de: {acumulador_deposito} e o valor da taxa de poupança é: {taxa_poupanca}')
print(f'O valor total ganho foi de: {total_ganho}')
