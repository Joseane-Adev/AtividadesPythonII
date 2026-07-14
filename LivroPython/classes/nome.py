from functools import total_ordering

@total_ordering
class Nome:
    def __init__(self,nome):
        if nome is None or not nome.strip():
            raise ValueError('Nome não pode ser nulo ou em branco')

        self.nome = nome
        self.chave = Nome.criaChave(nome)
    
    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return f'<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.nome} Chave: {self.chave}>'

    def __eq__(self, outro):
        print('__eq__Chamado')
        return self.nome == outro.nome
    
    def __lt__(self, outro):
        print('__lt__ Chamado')
        return self.nome < outro.nome

    def criaChave(nome):
        return nome.strip().lower()#tira os espaços e as letras ficam minusculas

#eq é igual os valores
# lt  menor que
A = Nome('Egito')
A == Nome('Egito') # eq chamado true

A != Nome('Egito') # eq chamado false

A > Nome('Egito') #lt chamado (false) e eq chamado

A < Nome('Egito') # lt chamado 

A <= Nome('Egito') 

A >= Nome('Egito')
