class ListaUnica:
    def __init__(self,elemento_classe):
        self.lista = [] #lista vazia
        self.elemento_classe = elemento_classe
    
    #tamanho
    def __len__(self):
        return len(self.lista)
    
    def __iter__(self):
        return iter(self.lista)
    
    def __getitem__(self, posicao):
        return self.lista[posicao]
    
    def indiceVálido(self, indice):
        return indice >= 0 and indice < len(self.lista)
    
    def adiciona(self,elemento):
        if self.pesquisa(elemento) == -1:
            self.lista.append(elemento)
    
    def remove(self, elemento):
        self.lista.remove(elemento)
    
    def pesquisa(self, elemento):
        self.verifica_tipo(elemento)
        try:
            return self.lista.index(elemento)
        except ValueError:
            return -1
    
    def verifica_tipo(self, elemento):
        if not isinstance(elemento, self.elemento_classe):
            raise TypeError('Tipo inválido')
    
    def ordena(self, chave= None):
        self.lista.sort(key=chave)

