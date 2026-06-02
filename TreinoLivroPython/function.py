EMPRESA = 'Unidos venceremos'

def imprime():
    print(EMPRESA)
    #print('-' * len(empresa))

imprime()

a = 5
def muda_e_imprime():
    global a
    a= 7
    print(f'Variavel dentro da função: {a}')
print(f'Variavel a fora da função: {a}')
muda_e_imprime()
print(f'variavel a depois de mudar: {a}')


#FATORIAL

def fatorial(n):
    print(f'Calculando o fatorial de {n}')
    if n == 0  or n == 1:
        print(f'fatorial de {n} = 1')
        return 1
    else:
        fat = n *fatorial(n-1)
        print(f'Fatorial de {n} = {fat}')
        return fat

fatorial(4)
print('--------------------------------')
#funçao recursiva fibonaci

'''
def fibonaci(n):
    if n <= 1:
        return n
    else:
        resultado = fibonaci(n-1) + fibonaci(n - 2)
        print(f'fibonaci de {n} = fibonaci {n-1} + fibonaci {n - 2} = {resultado}')
        return resultado

fibonaci(5)'''