from functools import total_ordering

@total_ordering
class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo

    #exibe o nome do tipo
    def __str__(self):
        return f'({self.tipo})'

    #metodo eq e lt para ativar a comparação por tipo
    def __eq__(self, value):
        if value is None:
            return False
        return self.tipo == value.tipo
    
    def __lt__(self, other):
        return self.tipo < other.tipo
     