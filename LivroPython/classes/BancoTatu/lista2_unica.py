from collections import UserList
class ListaUnica(UserList):
    def __init__(self,elemento_classe, enumerable = None):
        super().__init__(enumerable) #acessar userlist
        self.elemento_classe = elemento_classe
    
    #adicionar
    def append(self, item):
        self.verifica_tipo(item)
        if item not in self.data:
            super().append(item)
    
    def __setitem__(self, posicao, item):
        self.verifica_tipo(item)
        if item not in self.data:
           super().__setitem__(posicao, item)
    
    def extend(self, iterable):
        for item in iterable:
            self.verifica_tipo(item)
            if item not in self.data:
                super().append(item)#adiciona um por um
                
    def verifica_tipo(self, item):
        if not isinstance(item,self.elemento_classe):
            raise TypeError('TIPO INVÁLIDO')
    
