class Validacao():
    staticmethod
    def valida_nome():
        while True:
            nome = input('Digite o seu nome: ')
            if not nome.replace(' ', '').isalpha():#isalpha para todos char forem string
                    print('Nome inválido, apenas letras!')
            else:
                return nome.title()
    
