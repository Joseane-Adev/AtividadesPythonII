valor = float(input('Digite o valor a pagar: '))

cedulas = 0
moedas = 0
atual = 1000 # começa pela maior cedula
#CONVERTE PARA CENTAVOS
apagar= int(round(valor * 100))

while True:

    quantidade = apagar // atual
    apagar = apagar % atual

    if quantidade > 0:
        if atual >= 100:
            print(f'{quantidade} cedulas de R$: {atual / 100: .2f}')
        else: 
            print(f'{quantidade} moedas de R${atual / 100: .2f}')
        
        
        if apagar == 0:
            break

        #apagar -= atual
        #cedulas += 1
        #moedas += 1
    
    else:
        if atual == 1000:
            atual = 500
        elif atual ==500:
            atual = 100  
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0

        

        
