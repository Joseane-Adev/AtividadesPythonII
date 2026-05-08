#adicionar a tarefa
import os

def limpar():
    os.system('cls')

def menu():
    print('1-Adicionar Tarefa')
    print('2-Listar Tarefa')
    print('3-Remover Tarefa')
    print('4-Sair')

def opcao():
    while True:
        numero = int(input('Escolha sua opção: '))
        if numero == 1:
            adicionaTarefa()
        elif numero == 2:
            listarTarefa()
        elif numero == 3:
            removerTarefa()
        elif numero == 4:
            sair()
        else: 
            print('Digite uma opção entre 1 e 4')

lista = []
def adicionaTarefa():
    limpar()
    tarefa = input('Digite a tarefa: ').lower()
    print(f'{tarefa} registrada!')
    lista.append(tarefa)
    menu()
    

#listar a tarefa
def listarTarefa():
    #mostrar a lista
    print('-------Lista de Tarefas-------')
    for indice,item in enumerate(lista):
        print(f'[{indice}]{item}')
    print('-------------------------------')
        

# remover uma tarefa
def removerTarefa():
    #mostrar a lista e depois escolher qual quer apagar
    listarTarefa()
    escolha = int(input('escolha o numero da tarefa que quer apagar'))
    tarefa_removida = lista[escolha]
    del lista[escolha]
    print(f'Removido da lista:  {tarefa_removida}')
    
#sair
def sair():
    pass
menu()
opcao()



