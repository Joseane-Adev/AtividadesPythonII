from datetime import datetime
agenda = []
alterada = False

def pede_nome(msg = 'Nome: '):
    nome = input(msg)

    if nome  == '':
        return 'Vazio, preencha o espaço'
    return nome

def pede_telefone(numero= 'Telefone: '):
    telefone = input(numero)
    if telefone == '':
        return 'Preencha com o numero: '

    return telefone

def data_aniversario(msg = 'Digite a data de aniversário: (dia/mês/ano)'):
    data = input(msg)
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return data
    except ValueError:
        print('Digite uma data válida: dia/mes/ano')
        return 'Data inválida'
#para mostrar o que foi escrito em nome e telefone
def mostra_dados(indice, nome, telefones, data_aniversario):
    print(f'Indice: {indice} | Nome: {nome} | Data aniversario: {data_aniversario}')
    for tipo, numero in telefones:
        print(f"   {tipo}: {numero}")


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

def pede_tipo(msg="Tipo (fixo/celular): "):
    tipo = input(msg).strip().lower()
    if tipo == "":
        return "desconhecido"
    return tipo

def novo():
    '''
    funçao para cadastrar contato novo, onde chamo a funçaõ de pede o nome e pede telefone
    depois pego a lista vazia de agenda e adiciono o nome e telefone
    '''
    global agenda,alterada
    
    nome = pede_nome()
    '''
    verificação se o nome já existe na agenda ele apresenta a mensagem.
    '''
    for nome_duplo in agenda: 
        if nome_duplo[0] == nome:
          print(f'{nome} já existe')
          return
          
    telefones = []
    while True:
        tipo = input("Tipo de telefone (fixo/celular): ").strip().lower()
        numero = pede_telefone()
        telefones.append([tipo, numero])
        
        continuar = input("Deseja adicionar outro telefone? (s/n): ").strip().lower()
        if continuar != "s":
            break
    aniversario = data_aniversario()
    agenda.append([nome, telefones, aniversario])
    alterada = True # foi alterada

def apaga():
    '''
    a variavel nome, chama a funçao de pedir o nome
    a variavel p. chama a função de pesquisa nome com parametro  variavel nome
    if a variavel p nao é None(não encontrado) se foi encontrado delete da agenda na posição de pesquisar nome o nome do contato
    senao avise não encontrado
    '''
    global agenda,alterada
    nome = pede_nome()
    p = pesquisa_nome(nome)
    if p is not None:
            decisão = input('Deseja excluir esse contato? (Sim | Não) :').capitalize()
            if decisão == 'Sim':
                del agenda[p]
                print(f'Contato apagado {nome}')
                alterada = True
            else:
                print('Contato não excluido!')
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
        decisao = input('Deseja alterar? (Sim | Não): ').capitalize()
        if decisao == 'Sim':
            mostra_dados(nome, telefone)
            nome = pede_nome()
            telefone = pede_telefone()
            agenda[p] = [nome, telefone]
            alterada = True #agenda alterada
        else:
            print('NÃO ALTERADO!')
    else:
        print('Nome não encontradao')

def lista():

    '''
    imprime o nome agenda
    para i indice e x elemento em enumerate gerando uma tupla, ja que saõ dois valores (telefone e nome)
    imprima a posicao do indice
    chama mostra dados passa o nome e telefone da tupla
    '''
    print('\Agenda\n\n------')
    for i, x in enumerate(agenda):
        print(f'Contato: {i}')
        mostra_dados(i, x[0], x[1], x[2])
    print('------\n')

def ler():
    '''
    agenda é uma varivel de fora para acessar usamos global
    variavel chama a funçao pedir o nome do arquivo

    abertura de arquivo, tipo leitura
    cria a lista de agenda vazia
    Para cada linha do arquivo:
    - Remove espaços extras. strip()
    - Separa em nome e telefone usando o delimitador "#".split(#)
    - Adiciona [nome, telefone] à lista agenda.
    '''
    global agenda, alterada
    try: 
       
        nome_arquivo = pede_nome_arquivo()
        with open(nome_arquivo, 'r', encoding='UTF-8') as arquivo:
            agenda = []
            for linha in arquivo.readlines():
                nome, telefone = linha.strip().split('#')
                agenda.append([nome, telefone])

            agenda.sort()
            alterada = False
            
            with open('agenda_lida.txt', 'r', encoding='utf-8') as agenda_atualizada:
                agenda_atual = agenda_atualizada.read().strip()
                return agenda_atual
    except Exception as erro:
        print(f'Ocorreu um erro ao ler arquivo')



def grava():
    global agenda,alterada
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for i in agenda:
            arquivo.write(f'{i[0]}#{i[1]}\n')
        alterada = False
    

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
        if alterada:
            decisao = input("Agenda foi modificada. Deseja salvar antes de sair? (Sim | Não): ").capitalize()
            if decisao == "Sim":
                grava()
        print("Saindo...")
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