
class Telefone:
    def __init__(self, numero, tipo=None):
        self.numero = numero
        self.tipo = tipo
    
    def __str__(self):
        tipo = self.tipo or ''
        return f'{self.numero} {tipo}'
    
    def __eq__(self, value):
        return self.numero == value.numero and (
            (self.tipo == value.tipo) or (
                self.tipo is None or value.tipo is None
            )
        )
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter

    def numero(self, valor):
        if valor is None or not valor.strip():
            raise ValueError('Numero não pode ser None ou em branco')
        self.__numero = valor