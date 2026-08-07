#dir
#hasattr checa se um objeto está em determinado lugar
#getattr
#checar um metodo se existe
string = 'Ane'
metodo = 'lower'

if hasattr(string, 'upper'):
    print('EXISTE UPPER')
    print(getattr(string, metodo)())
else:
    print('Não existe o metodo', metodo)


