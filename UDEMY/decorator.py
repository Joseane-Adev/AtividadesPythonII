#funçoes decoradores
'''
decorar = adicionar / remover / restringir e alterar

'''
#funçao decoradora - 
def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)

        return resultado
    return interna

def inverte(string):
    return string[::-1]#fatiamento

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_parametro = criar_funcao(inverte)
invertida = inverte_string_parametro('123')
print(invertida)
