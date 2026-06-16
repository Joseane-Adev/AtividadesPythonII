agenda = []

def pede_nome():
    return input('Nome: ')

def pede_telefone():
    return input('Telefone: ')

#para mostrar o que foi escrito em nome e telefone
def mostra_dados(nome, telefone):
    print(f'Nome: {nome} | Telefone: {telefone}')


def pede_nome_arquivo():
    return input('Nome do arquivo: ')

#pesquisa se o nome está na lista
def pesquisa_nome(nome):
    onome = nome.lower() # transforma o nome em minuscula
    for a, b in enumerate(agenda): #percorre com enumerate
        if b[0].lower() == onome: #compara o nome  armazenado b[indice] com a variavel que transformou em minusculo
            return a # se encontrar retorna o a posição do nome na lista
    return None # se não encontrar retorna None

#b[0] é o nome armazenado no contado da agenda, b é o elemento da lista

def novo():
    '''
    funçao para cadastrar contato novo, onde chamo a funçaõ de pede o nome e pede telefone
    depois pego a lista vazia de agenda e adiciono o nome e telefone
    '''
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

def apaga():
    '''
    a variavel nome, chama a funçao de pedir o nome
    a variavel p. chama a função de pesquisa nome com parametro  variavel nome
    if a variavel p nao é None(não encontrado) se foi encontrado delete da agenda na posição de pesquisar nome o nome do contato
    senao avise não encontrado
    '''
    nome = pede_nome()
    p = pesquisa_nome(nome)
    if p is not None:
        del agenda[p]
    else:
        print('Não encontrado')

def altera():
    '''
    variavel p = psquisa nome como parametro, chama a funçao pede nome
    se p não é None(nao encontrado):
    variavel nome recebe agenda o elemento nome e a posiçao primeira referente a nome
    variavel telefone recebe agenda, o elemnto telefone e a segundo indice que é o telefone
    imprime encontrado, chama a funçao para mostrar os dados encontrados

    variavel nome chama a funçao pede nome e pede telefone para fazer alteração
    a agenda recebe os elementos nome e telefone atualizados

    senão:
    imprime nome não encontrado
    
    '''
    p = pesquisa_nome(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Encontrado')
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print('Nome não encontradao')

def lista():
    print('\Agenda\n\n------')
    for i, x in enumerate(agenda):
        print(f'Posição: {i}')
        mostra_dados(x[0], x[1])
    print('------\n')

def ler():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'r', encoding='UTF-8') as arquivo:
        agenda = []
        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split('#')
            agenda.append([nome, telefone])

def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for i in agenda:
            arquivo.write(f'{i[0]}#{i[1]}\n')

def tamanho_agenda():
    print(f'Tamanho da agenda: {len(agenda)}')


def valida_faixa(pergunta,inicio, fim):
    while True:
        try:
            valor= int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')

def menu():
    print("""
          1 - Novo
          2 - Altera
          3 - Apaga
          4 - Lista
          5 - Grava
          6 - Lê
          7 - tamanho agenda

          0 - sai
          """)
    
    return valida_faixa('Escolha uma opção', 0, 7)
while opcao:= menu():
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        ler()
    elif opcao == 7:
        tamanho_agenda()