#valores truthy e falsy, mutáveis e imutáveis
#mutáveis = [ lista], {dict}, set()
#imutáveis = () tupla ''- string, None, False, range(0,10)

lista = [1,2]
dic = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste', falsy('TESTE'))
print(f'{lista= }', falsy(lista))
print(f'{flutuante=}', falsy(flutuante))






