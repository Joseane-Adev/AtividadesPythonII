#variaveis livres + nonlocal

def fora(x):
    s = x
    def dentro():
        print(locals()) #tudo o que pode acessar
        #print(dentro.__code__.co_freevars)
        return s
    return dentro


dentro1 = fora(10)
print(dentro1())

